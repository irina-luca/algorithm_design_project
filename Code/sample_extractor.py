import numpy as np

# -- Randomly extract lines (tuples) from the dataset file with params: sample size == k, dataset size == n, number of samples == number_samples -- #
def sample_extractor(file_name, k, n, seed_val, number_samples):
    samples = [[] for _ in range(number_samples)]
    np.random.seed(seed_val)
    p = float(k)/n  # sampling probability
    print "sampling with probability: " + str(p)


    with open(file_name) as f:
        for i, tuple in enumerate(f):
            random_nums = [np.random.random() for _ in xrange(number_samples)]
            # print random_nums[0], random_nums[1], random_nums[2], random_nums[3], p
            for kth, sample in enumerate(samples):
                if random_nums[kth] < p:
                    samples[kth].append(tuple)
                if i % 10000 == 0:
                    print i

    for kth, sample in enumerate(samples):
        with open('Data/' + dest_folder + '/profi-' + str(kth+1) + '_' + str(k) + '.train', 'w') as g:
            for i, tuple in enumerate(sample):
                g.write(tuple)
                print tuple


# -- Try out with more seed values && k's -- #
# k_set = [10000, 100000, 500000]
k_set = [1000, 10000, 100000]
seed_val_set = [1, 2, 3, 4, 5]
number_samples = 5
n = 20172525
dest_folder = 'Experiment_1-1-1' # Do not forget tp set the destination folder!!!!

for i, k_val in enumerate(k_set):
    sample_extractor('Data/descriptors-decaf-reduced-and-normalized.data', k_val, n, seed_val_set[i], number_samples)