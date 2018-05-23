import numpy as np
import time
from sklearn.neighbors import NearestNeighbors


def shd(x1,x2):
    shd_xor = np.bitwise_xor(np.uint64(x1), np.uint64(x2))
    shd_and = np.bitwise_and(np.uint64(x1), np.uint64(x2))
    return float(np.count_nonzero(shd_xor)) / (np.count_nonzero(shd_and) + 0.000001)


def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def calc_reverse_index(i1, i2, k):
    reverse_indices = np.zeros((i1.shape[0], k), dtype=int)
    for i, euc_neighbors in enumerate(i1):
        for j, euc_neighbor in enumerate(euc_neighbors):
            reverse_indices[i, j] = next(index for index, cell in enumerate(i2[i]) if cell == euc_neighbor)
    return reverse_indices


def batch_implementation():
    print "Starting ..."
    # Input params.
    n = 10000
    batch_size = 10
    f = 20
    k = 1
    query_size = 100

    # Setup test data.
    euc_data_full = np.random.rand(n, f)
    bit_data_full = np.random.randint(2, size=(n, f), dtype=np.bool)

    print "Data structure"
    # Setup bit NN data structure.
    nbrs_euc = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean').fit(euc_data_full)
    nbrs_bit = NearestNeighbors(n_neighbors=n, algorithm='auto', metric='jaccard').fit(bit_data_full)

    # Split input into batches
    data_batches = zip(split(euc_data_full[:query_size], batch_size),
                       split(bit_data_full[:query_size], batch_size))

    reverse_indices = []
    # Find nn for batches sequentially.
    for i, batch in enumerate(data_batches):
        start_time = time.time()
        euc_batch, bit_batch = batch
        if i%10 == 0:
            print "batch", str(i), "of", str(len(data_batches))

        # Find nn for batch i.
        euc_indices = nbrs_euc.kneighbors(euc_batch, return_distance=False)
        bit_indices = nbrs_bit.kneighbors(bit_batch, return_distance=False)

        # Calculate reverse index for batch i.
        reverse_indices_batch = calc_reverse_index(euc_indices, bit_indices, k)

        reverse_indices.extend(reverse_indices_batch)
        #print "Calculating batch took", str(time.time() - start_time), \
        #    "second (finish in ~"+str(((time.time() - start_time)*(len(data_batches)-i)/3600))+" hours)"


    # X-axis steps
    steps = []
    x_reading = 1
    steps.append(1)
    while (x_reading * 2) < n:
        x_reading *= 2
        steps.append(x_reading)

    # Add last step to get 1 recall
    steps.append(x_reading * 2)

    # Calculate Y values at X steps
    print "Begin Y-axis calculations"
    result = []
    for retrieved_samples in steps:
        recall_sum = 0
        for sample in reverse_indices:
            recall_sum += len([1 for index in sample if index < retrieved_samples])
        print recall_sum, float(query_size * k)
        avg_recall = recall_sum / float(query_size * k)
        result.append((retrieved_samples, avg_recall, recall_sum / float(query_size)))

    precision_matches = 0
    for reverse_index in reverse_indices:
        precision_matches += len([1 for index in reverse_index if index < k])

    precision = float(precision_matches) / (k * query_size)

    print result
    print precision


def all_implementation():
    print "running from command line.."
    # random binary data
    n = 10000
    batch_size = 100
    f = 257
    k = 100
    full_data = np.random.randint(2, size=(n, f), dtype=np.bool)
    search_data = np.random.randint(2, size=(batch_size, f), dtype=np.bool)
    # random data
    X = np.random.rand(n, f)
    H = np.random.rand(k, f)

    start_time = time.time()
    print "fitting"
    nbrs_euc = NearestNeighbors(n_neighbors=k, algorithm='auto', metric='euclidean').fit(X)
    nbrs = NearestNeighbors(n_neighbors=n, algorithm='auto', metric='jaccard').fit(full_data)
    # nbrs = NearestNeighbors(n_neighbors=1000, algorithm='auto', metric=shd).fit(full_data)
    print time.time() - start_time

    start_time_2 = time.time()
    print "searching1"
    bit_indices = nbrs.kneighbors(search_data, return_distance=False)
    print "searching2"
    bit_indices2 = nbrs.kneighbors(search_data, return_distance=False)
    euc_indices = nbrs_euc.kneighbors(H, return_distance=False)
    print time.time() - start_time_2

    # print bit_indices
    # print euc_indices

    # ====================================
    # X-axis steps
    steps = []
    x_reading = 1
    while (x_reading * 2) < n:
        x_reading *= 2
        steps.append(x_reading)

    # Add last step to get 1 recall
    steps.append(x_reading * 2)

    # Generate reverse indices
    print "Begin reverse index"
    reverse_indices = np.zeros((n, k), dtype=int)
    for i, euc_neighbors in enumerate(euc_indices):
        for j, euc_neighbor in enumerate(euc_neighbors):
            print i, j
            reverse_indices[i, j] = next(index for index, cell in enumerate(bit_indices[i]) if cell == euc_neighbor)

    # print reverse_indices

    # Calculate Y values at X steps
    print "Begin Y-axis calculations"
    result = []
    for retreived_samples in steps:
        recall_sum = 0
        for sample in reverse_indices:
            recall_sum += len([1 for index in sample if index < retreived_samples])
        avg_recall = recall_sum / float(n * k)
        result.append((retreived_samples, avg_recall, recall_sum / float(n)))
    print result

if __name__ == "__main__":
    #all_implementation()
    batch_implementation()



# Euclidean nn 100.000 (512) ~ 3.4 hour
# shd nn 100.000 (512) ~ 19 hour
# jaccard nn 100.000 (512) ~ 19 hour