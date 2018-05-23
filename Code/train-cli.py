import argparse
import train

# Example:
# python train-cli.py -i Data/gist-10000-1.train -m Data/gist-10000-1-c10.model -c 10 > Results/gist-10000-1-c10.log

# Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument("-i", help="input dataset", required=1)
parser.add_argument("-m", help="model output file", required=1)
parser.add_argument("-c", help="hypersphere count", type=int, required=1)
parser.add_argument("-em", help="error tolerance mean", type=float, nargs='?', default=0.1)
parser.add_argument("-es", help="error tolerance standard deviation", type=float, nargs='?', default=0.15)
args = parser.parse_args()

input_file = args.i
output_model = args.m
hypersphere_count = args.c
error_tolerance_m = args.em
error_tolerance_s = args.es

train.train_model(input_file, output_model, hypersphere_count, error_tolerance_m, error_tolerance_s, delimiter=' ')