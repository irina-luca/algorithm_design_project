import numpy as np
import operator
from hypersphere import Hypersphere
from distance_functions import *
from sklearn.neighbors import NearestNeighbors
import pickle
import time
import math
import sys

# Micro avereraged precision
def calculate_precision(sample, hyperspheres, k, metric):
    total_matches = 0
    bit_vectors = []
    for i, tuple in enumerate(sample):
        bit_vectors.append(__dec_to_bit(hyperspheres, tuple))

    bit_vectors = np.asarray(bit_vectors)
    
    # print "timer start on calc ground truth"
    # time_start = time.time()
    euclidean_nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean').fit(sample)
    euclidean_indices = euclidean_nbrs.kneighbors(sample, return_distance=False)
    bit_nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto', metric=SHD_distance).fit(bit_vectors)
    bit_indices = bit_nbrs.kneighbors(bit_vectors, return_distance=False)

    for pair in zip(euclidean_indices, bit_indices):
        sample_row_matches = len(np.intersect1d(pair[0], pair[1]))
        total_matches += sample_row_matches
    print "total matches => " + str(total_matches)
    # end_time = time.time() - time_start
    # print ("Final time #%(end_time)s" % locals())
    return float(total_matches) / (k * len(sample))


def calculate_recall(sample, hyperspheres, k):
    """ Returns a list of tuples where [0] is the retrieved samples and [1] is the recall """
    batch_size = 1000
    sample_size = sample.shape[0]
    start_time = time.time()
    bit_vectors = []
    for i, tuple in enumerate(sample):
        bit_vectors.append(__dec_to_bit(hyperspheres, tuple))


    print "[DEBUG] Setting up nn data structure (sample) ..."
    euclidean_nbrs = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean').fit(sample)
    print "[DEBUG] Finding actual nn ..."
    euclidean_indices = euclidean_nbrs.kneighbors(sample, return_distance=False)


    print "[DEBUG] Setting up nn data structure (bits) ..."
    bit_nbrs = NearestNeighbors(n_neighbors=sample_size, algorithm='auto', metric='jaccard').fit(bit_vectors)
    print "[DEBUG] Finding approximated nn (bits) ..."
    bit_indices = bit_nbrs.kneighbors(bit_vectors, return_distance=False)

    steps = []
    x_reading = 1
    while (x_reading * 2) < sample_size:
        x_reading *= 2
        steps.append(x_reading)
    steps.append(x_reading * 2)

    print "[DEBUG] Building reverse index ..."
    sys.stdout.write("[DEBUG] Process (t:" + str(sample_size) + "): ")
    reverse_indices = np.zeros((sample_size, k), dtype=int)
    for i, euc_neighbors in enumerate(euclidean_indices):
        if i % 100 == 0:
            sys.stdout.write(str(i) + " ")
            sys.stdout.flush()
        for j, euc_neighbor in enumerate(euc_neighbors):
            reverse_indices[i, j] = next(index for index, cell in enumerate(bit_indices[i]) if cell == euc_neighbor)
    print ""
    recalls = []
    for retrieved_samples in steps:
        recall_sum = 0
        for sample in reverse_indices:
            recall_sum += len([1 for index in sample if index < retrieved_samples])
        avg_recall = recall_sum / float(sample_size * k)
        recalls.append((retrieved_samples, avg_recall))
    print "[DEBUG] Duration: ", str(time.time() - start_time), "seconds."
    return recalls


def calculate_recall_with_batch_processing(sample, hyperspheres, k):
    """ Returns a list of tuples where [0] is the retrieved samples and [1] is the recall """
    batch_size = 10
    sample_size = sample.shape[0]
    start_time = time.time()
    bit_vectors = []
    for i, tuple in enumerate(sample):
        bit_vectors.append(__dec_to_bit(hyperspheres, tuple))


    print "[DEBUG] Setting up nn data structures ..."
    nbrs_euc = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean').fit(sample)
    nbrs_bit = NearestNeighbors(n_neighbors=sample_size, algorithm='auto', metric='jaccard').fit(bit_vectors)

    # Split input into batches
    data_batches = zip(__split(sample, batch_size),
                       __split(bit_vectors, batch_size))

    reverse_indices = []
    # Find nn for batches sequentially.
    sys.stdout.write("[DEBUG] Batch (t:" + str(len(data_batches)) + "): ")
    for i, batch in enumerate(data_batches):
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()
        start_time = time.time()
        euc_batch, bit_batch = batch

        # Find nn for batch i.
        euc_indices = nbrs_euc.kneighbors(euc_batch, return_distance=False)
        bit_indices = nbrs_bit.kneighbors(bit_batch, return_distance=False)

        # Calculate reverse index for batch i.
        reverse_indices_batch = __calc_reverse_index(euc_indices, bit_indices, k)
        reverse_indices.extend(reverse_indices_batch)

    print ""
    steps = []
    x_reading = 1
    while (x_reading * 2) < sample_size:
        x_reading *= 2
        steps.append(x_reading)
    steps.append(x_reading * 2)

    recalls = []
    for retrieved_samples in steps:
        recall_sum = 0
        for reverse_index in reverse_indices:
            recall_sum += len([1 for index in reverse_index if index < retrieved_samples])
        avg_recall = recall_sum / float(sample_size * k)
        recalls.append((retrieved_samples, avg_recall))
    print "[DEBUG] Duration: ", str(time.time() - start_time), "seconds."
    return recalls


def calculate_quality_measures(sample, hyperspheres, k, batch_size, query_size, measurement_index, r=None):
    """ Returns a list of tuples where [0] is the retrieved samples and [1] is the recall """
    metric = ''

    # Not rerank recall
    if not r:
        print "[DEBUG] NOT RERANK_RECALL"
        r = k
    else:
        print "[DEBUG] RERANK_RECALL"

    if measurement_index == 0:
        metric = 'jaccard'
    if measurement_index == 1:
        metric = SHD_distance
    if measurement_index == 2:
        metric = AND_distance
    if measurement_index == 3:
        metric = 'hamming'

    print "[DEBUG] MEASURE:", measurement_index
    sample_size = sample.shape[0]
    if query_size == -1:
        query_size = sample_size
    bit_vectors = []
    for i, tuple in enumerate(sample):
        bit_vectors.append(__dec_to_bit(hyperspheres, tuple))

    nbrs_euc = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean').fit(sample)
    nbrs_bit = NearestNeighbors(n_neighbors=sample_size, algorithm='auto', metric=metric).fit(bit_vectors)

    # Split input into batches
    #print len(sample.shape)
    data_batches = zip(__split(sample[:query_size], batch_size),
                       __split(bit_vectors[:query_size], batch_size))

    reverse_indices = []
    # Find nn for batches sequentially.
    sys.stdout.write("[DEBUG] Batch (t:" + str(len(data_batches)) + "): ")
    for i, batch in enumerate(data_batches):
        sys.stdout.write(str(i) + " ")
        sys.stdout.flush()

        euc_batch, bit_batch = batch

        # Find nn for batch i.
        euc_indices = nbrs_euc.kneighbors(euc_batch, return_distance=False) # query_size x k
        bit_indices = nbrs_bit.kneighbors(bit_batch, return_distance=False) # query_size x n

        # Calculate reverse index for batch i.
        reverse_indices_batch = __calc_reverse_index(euc_indices, bit_indices, k) # query_size x k
        reverse_indices.extend(reverse_indices_batch)

    print ""
    steps = []
    x_reading = 1
    while (x_reading * 2) < sample_size:
        x_reading *= 2
        steps.append(x_reading)
    steps.append(x_reading * 2)

    recalls = []
    for retrieved_samples in steps:
        recall_sum = 0.
        for reverse_index in reverse_indices:
            found = len([1 for index in reverse_index if index < retrieved_samples * (r / k)])
            if found >= retrieved_samples:
                found = retrieved_samples
            recall_sum += found
        avg_recall = float(recall_sum) / float(query_size * k)
        recalls.append((retrieved_samples, avg_recall))

    precision_matches = 0
    for reverse_index in reverse_indices:
        precision_matches += len([1 for index in reverse_index if index < r])

    precision = float(precision_matches) / (k * query_size)
    return precision, recalls


# ===================== PRIVATE FUNCTIONS =====================
def __dec_to_bit(hyperspheres, point):
    bit_vector = []
    for i, hypersphere in enumerate(hyperspheres):
        if np.linalg.norm(point - hypersphere.center) < hypersphere.threshold:
            bit_vector.append(1)
        else:
            bit_vector.append(0)
    return bit_vector


def __split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def __calc_reverse_index(i1, i2, k):
    reverse_indices = np.zeros((len(i1), k), dtype=int)
    for i, euc_neighbors in enumerate(i1):
        for j, euc_neighbor in enumerate(euc_neighbors):
            reverse_indices[i, j] = next(index for index, cell in enumerate(i2[i]) if cell == euc_neighbor)
    return reverse_indices



# ===================== TEST FUNCTIONS =====================
def small_test_Dec_to_Bit():
    hyperspheres = [Hypersphere(np.array([1.0, 1.0]), 2.0), Hypersphere(np.array([2.0, 2.0]), 2.0)]
    point_1 = np.array([1.5, 1.5])
    point_2 = np.array([0.0, 0.0])
    point_3 = np.array([-1.0, -1.0])
    point_4 = np.array([3.0, 3.0])
    print __dec_to_bit(hyperspheres, point_1)
    print __dec_to_bit(hyperspheres, point_2)
    print __dec_to_bit(hyperspheres, point_3)
    print __dec_to_bit(hyperspheres, point_4)


def small_test_calculate_avg_precision():
    hyperspheres = [Hypersphere(np.array([1.0, 1.0]), 2.0), Hypersphere(np.array([-1.0, -1.0]), 2.0)]
    point_1 = np.array([-2., -2.])
    point_2 = np.array([2., 2.])
    point_3 = np.array([0, 0])
    point_4 = np.array([3.0, 3.0])
    test_set = []
    test_set.append(point_1)
    test_set.append(point_2)
    test_set.append(point_3)
    test_set.append(point_4)
    micro_avg_precision = calculate_precision(test_set, hyperspheres, 2)
    print "precision: " + str(micro_avg_precision)
