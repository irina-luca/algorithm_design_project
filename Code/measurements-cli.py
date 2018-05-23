import argparse
import measurements
import pickle
import numpy as np
import algorithm
import distance_functions

#Example: python measurements-cli.py -m Data/hsize-10000-10-c0-sph8.model -d Data/train-dataset-10000-10-0.csv -om -k 100 -me shd
parser = argparse.ArgumentParser()

parser.add_argument("-m", help="model output file", required=1)
parser.add_argument("-d", help="input test dataset", required=1)
parser.add_argument('-om', help="use old model", action='store_true', default=False)
parser.add_argument("-k", help="number of nearest neighbours", type=int, required=1)
parser.add_argument("-me", help="metric to use with bitwise KNN", default='jaccard')
args = parser.parse_args()

is_deprecated = args.om
file_model = args.m
file_dataset = args.d
k = args.k
metric = args.me

model = pickle.load(open(file_model, "rb")) 
print "start reading file"
sample = np.genfromtxt(file_dataset, delimiter=' ')
print "end reading file"

mins = []
maxes = []

if metric == "shd":
    metric = distance_functions.SHD_distance
    print "USING SHD!!"
elif metric == "and":
    metric = distance_functions.AND_distance
    print "USING AND!!"
else:
    print "USING" + metric + "!!"

if is_deprecated:
    mins = np.zeros((sample.shape[1], 1))
    mins[:]=-10
    mins = min.flatten()
    maxes = np.zeros((sample.shape[1], 1))
    maxes[:]=10
    maxes = max.flatten()
else:
    mins = model.min
    maxes = model.max
    model = model.hyperspheres
#print mins
#print maxes
normalized_sample = algorithm.normalize_with_mins_maxes(sample, mins, maxes)
mean_avg_prec = measurements.calculate_precision(normalized_sample, model, k, metric)
print mean_avg_prec