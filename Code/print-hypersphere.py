import pickle
import argparse
import algorithm

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="model file", required=1)
parser.add_argument('-d', help="use old model", action='store_true', default=False)
parser.add_argument('-t', help="print threshold only", action='store_true', default=False)
args = parser.parse_args()

file_model = args.m
is_deprecated = args.d
print_thresholds= args.t

model = pickle.load(open(file_model, "rb"))

if is_deprecated:
    algorithm.print_hyperspheres(model)
else:
    if print_thresholds:
        algorithm.print_hyperspheres_thresholds(model.hyperspheres)
    else:
        algorithm.print_hyperspheres(model.hyperspheres)

