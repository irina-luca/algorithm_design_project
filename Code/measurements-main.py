import argparse
import algorithm
import time
import pickle
import sys

import numpy as np

import measurements
# Example:
# python measurements-main.py -m "Experiments/Experiment_1-1-1/model.config" -t "Experiments/Experiment_1-1-1/test.config" -k 100

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="model config file", required=1)
parser.add_argument("-t", help="test config file", required=1)
parser.add_argument("-k", help="k for nn", type=int, required=1)
parser.add_argument("-b", help="batch size", type=int, nargs='?', default=10)
parser.add_argument("-q", help="query size", type=int, nargs='?', default=-1)
parser.add_argument("-r", help="nsh r", type=int, nargs='?', default=0)
parser.add_argument("-mi", help="measurements index [0=jaccard, 1=SHD, 2=AND]", type=int, nargs='?', default=0)
args = parser.parse_args()

config_model_files = args.m
config_test_files = args.t
k = args.k
batch_size = args.b
query_size = args.q
measurement_index = args.mi
r = args.r


def run_measures(models, tests, k, batch_size, query_size, measurement_index, nsh_r):
    print models
    print tests
    summaries = []
    # Iterate models
    for model_file in models:
        print "[DEBUG] Model =>", model_file
        hypersphere_model = pickle.load(open(model_file, "rb"))

        model = hypersphere_model.hyperspheres
        min = hypersphere_model.min
        max = hypersphere_model.max
        model_recalls = []
        model_precisions = []
        for ts, testing_sample in enumerate(tests):
            start_time = time.time()
            print "[DEBUG] Sample =>" + testing_sample
            sys.stdout.flush()
            sample = np.genfromtxt(testing_sample, delimiter=' ', dtype=np.float64)
            normalized_sample = algorithm.normalize_with_mins_maxes(sample, min, max)
            sample_precision, sample_recall = measurements.calculate_quality_measures(normalized_sample, model, k, batch_size, query_size, measurement_index, nsh_r)
            model_recalls.append(sample_recall)
            model_precisions.append(sample_precision)

            print ""
            print "[MODEL, SAMPLE]:", model_file, testing_sample
            print "[RECALL]", sample_recall
            print "[PRECISION] ", sample_precision
            print "[DURATION]: ", str(time.time() - start_time), "seconds."
            print ""

        summary = (model_file, zip(tests, model_recalls, model_precisions))

        print "[MODEL]", model_file, ":"
        for sample, recall, precision in summary[1]:
            print "[RESULT_CONT][MODEL]" + model_file+ ";[SAMPLE]"+sample+";"+",".join(str(x) for x in recall) + ";" + str(precision)
        print "==========================================="
        summaries.append(summary)

    print "All results: "
    for model, data in summaries:
        print "[MODEL] " + model + ":"
        for sample, recall, precision in data:
            print "[RESULT][MODEL]" + model + ";[SAMPLE]" + sample + ";" + ",".join(str(x) for x in recall) + ";" + str(precision)


models, tests = ([line.rstrip('\n') for line in open(config_model_files) if not line.startswith("#")],
                 [line.rstrip('\n') for line in open(config_test_files) if not line.startswith("#")])
run_measures(models, tests, k, batch_size, query_size, measurement_index, r)

# Old
#recall_vs_retrieved_samples(models, tests)
#precision_vs_c(models, tests)
