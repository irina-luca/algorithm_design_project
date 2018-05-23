import numpy as np
from distance_functions import *
from hypersphere import Hypersphere
import time

### Functions ###
def normalize_data(data):
    data_normalized = []
    mins = []
    maxes = []
    for row in data.T:
        min_row = min(row)
        max_row = max(row)
        data_normalized.append([(value - min_row) / (max_row - min_row) for value in row])
        mins.append(min_row)
        maxes.append(max_row)

    return np.array(data_normalized).T, mins, maxes


def normalize_with_mins_maxes(data, mins, maxes):
    data_normalized = []
    for d, dimension in enumerate(data.T):
        data_normalized.append([(value - mins[d]) / (maxes[d] - mins[d]) for value in dimension])

    return np.array(data_normalized).T


def get_hypersphere_threshold(pivot, sample):
    distances = []
    for row in sample:
        distance = distance_euclidean(row, pivot)
        distances.append(distance)
    distances_sorted = sorted(distances)
    return Hypersphere(pivot, distances_sorted[len(distances_sorted)/2])


def compute_o_ij_old(sample, hyperspheres, c):
    o_ij = np.zeros((c, c))

    for i in xrange(c):
        for j in xrange(i+1, c):
            count_o = 0 
            for row in sample:
                # Distance measure
                distance_i = distance_euclidean(row, hyperspheres[i].center)
                distance_j = distance_euclidean(row, hyperspheres[j].center)
                if((distance_i < hyperspheres[i].threshold) and (distance_j < hyperspheres[j].threshold)):
                    count_o += 1
            o_ij[i][j] = count_o
            o_ij[j][i] = count_o
    return o_ij


def compute_o_ij(sample, hyperspheres, c):
    bit_vectors = np.zeros((len(sample), c), dtype=int)
    o_ijs = np.zeros((c, c))

    for i, row in enumerate(sample):
        for j, hypersphere in enumerate(hyperspheres):
            # Distance measure
            distance_row_pivot = distance_euclidean(row, hypersphere.center)
            if distance_row_pivot < hypersphere.threshold:
                bit_vectors[i, j] = 1

    for i in xrange(c):
        for j in xrange(i + 1, c):
            o_ij = len([1 for row in bit_vectors if row[i] == 1 and row[j] == 1])
            o_ijs[i][j] = o_ij
            o_ijs[j][i] = o_ij
    return o_ijs


### Helper Functions ###
def print_hyperspheres(hyperspheres):
    for i, hypersphere in enumerate(hyperspheres):
        print "Hypersphere #", str(i)
        print hypersphere
    print "Total spheres:", str(len(hyperspheres))

def print_hyperspheres_thresholds(hyperspheres):
    for i, hypersphere in enumerate(hyperspheres):
        print "Hypersphere #" + str(i) + ":", str(hypersphere.threshold)
    print "Total spheres:", str(len(hyperspheres))

def initialize_pivots_random(sample, c):
    return sample[np.random.randint(sample.shape[0], size=c), :]

def initialize_pivots_farthest(sample, c):
    exclusive_sample = sample.copy()
    d = exclusive_sample.shape[1]
    pivots = []

    initial_pivot = []
    for i, dimension in enumerate(exclusive_sample.T):
        dim_avg = np.average(dimension)
        initial_pivot.append(dim_avg)
    pivots.append(initial_pivot)

    for p in xrange(c - 1):
        max_distance = -1
        farthest_pivot = []
        farthest_pivot_index = -1
        for i, tuple in enumerate(exclusive_sample):
            distance_to_tuple = distance_euclidean(tuple, initial_pivot)
            if distance_to_tuple > max_distance:
                max_distance = distance_to_tuple
                farthest_pivot = tuple
                farthest_pivot_index = i
        pivots.append(farthest_pivot)
        initial_pivot = farthest_pivot
        exclusive_sample = np.delete(exclusive_sample, farthest_pivot_index, axis=0)

    return pivots


### Algorithm ###
def spherical_hashing(sample, c, error_tolerance_m, error_tolerance_s, verbose=False):
    print "starting"
    # Local vars
    m = len(sample)
    max_iterations = 20
    o_i_target = m / 2.
    o_ij_target = m / 4.

    error_tolerated_stddev_target = error_tolerance_s * o_ij_target
    error_tolerated_mean_target = error_tolerance_m * o_ij_target

    #-- Initialize p1, ..., pc with randomly chosen c data points --#

    #pivots = initialize_pivots_random(sample, c)
    pivots = initialize_pivots_farthest(sample, c)
    #-- Determine t1, ..., tc to satisfy o_i_target = m/2 --#
    print "hypersphere"
    hyperspheres = []
    for p in pivots:
        hyperspheres.append(get_hypersphere_threshold(p, sample))
    print "oij"
    #-- Compute o_ij for each pair of hashing functions --#
    o_ij = compute_o_ij(sample, hyperspheres, c)
    print "oij done"
    #-- Mask for o_ij with True below the diagonal and False everywhere else --#
    lower_diagonal_mask = np.tril(np.ones(o_ij.shape, dtype=bool), -1)
    # print print_hyperspheres(hyperspheres)
    converged = False
    iteration_count = 0
    time_start = time.time()
    time_intermediate = time.time()
    while not converged and iteration_count <= max_iterations:
        #-- Compute the force for each hypersphere --#
        force = np.zeros([c,c,sample.shape[1]])
        for i in xrange(c):
            for j in xrange(i+1, c):
                force[i,j] = np.array(1/2. * ((o_ij[i,j] - o_ij_target) / o_ij_target) * (hyperspheres[i].center - hyperspheres[j].center))
                force[j,i] = - force[i,j]

        #-- Apply average force to each of the hyperspheres' pivots --#
        for i in xrange(c):
            f_i_avg = np.mean(force[i], axis=0)
            hyperspheres[i].center += f_i_avg

        #-- Calculate threshold and update the hypersphere after applying the average force --#
        for i, pivot in enumerate(pivots):
            hyperspheres[i] = get_hypersphere_threshold(pivot, sample)

        #-- Compute o_ij for each pair of hashing functions --#
        o_ij = compute_o_ij(sample, hyperspheres, c)

        #-- Calculate convergence rules --#
        o_ij_substracted = np.abs(o_ij - o_ij_target)

        average_o_ij = o_ij_substracted[lower_diagonal_mask].mean()
        std_o_ij = o_ij[lower_diagonal_mask].std()

        iteration_count += 1
        if verbose:
            print ("Iteration #%(iteration_count)s" % locals())
            print ("mean:\t(%(average_o_ij)s => %(error_tolerated_mean_target)s)" % locals())
            print ("stddev:\t(%(std_o_ij)s => %(error_tolerated_stddev_target)s)" % locals())
            current_time = time.time() - time_intermediate
            print ("Iteration time:\t%(current_time)s seconds" % locals())
            time_intermediate = time.time()
            print "=============================="
        converged = average_o_ij <= error_tolerated_mean_target and std_o_ij <= error_tolerated_stddev_target

    if not converged:
        print ("Timeout due to reaching max iterations")
    total_time = time.time() - time_start
    print ("Total runningtime: %(total_time)s" % locals())
    return hyperspheres


#-- Iris test --#
def simple_iris_test():
    m = 100
    c = 5
    error_tolerance_m = 0.3
    error_tolerance_s = 0.3

    np.random.seed(0)  # seed, for testing
    # -- Read dataset --#
    data_file_name = "Data/Miscellaneous/iris.data.csv"
    data = np.genfromtxt(data_file_name, delimiter=",")

    # -- Normalize dataset --#
    data_normalized = normalize_data(data)

    # -- Sample m points from the dataset --#
    sample = data_normalized[np.random.randint(data_normalized.shape[0], size=m), :]
    hyperspheres = spherical_hashing(sample, c, error_tolerance_m, error_tolerance_s,
                                            True)
    # -- Print Hyperspheres --#
    print_hyperspheres(hyperspheres)

# Remove comment to test.
# simple_iris_test()

