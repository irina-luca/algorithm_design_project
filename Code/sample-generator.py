import argparse
import numpy as np
import string
from sklearn.datasets import make_blobs

# Example: 
# > python sample-generator.py -n 1000 -f 10 -s 1 -c 5
# > python sample-generator.py -n 1000 -f 257 -s 1 -c 8 -o "Data\Samples\random-1000-1_clusters-8.train"
# > python sample-generator.py -n 10000 -f 257 -s 1 -c 8 -o "Data\Samples\random-10000-1_clusters-8.train"
# > python sample-generator.py -n 1000 -f 257 -s 1 -o "Data\Samples\random-1000-1_clusters-0.train"
# > python sample-generator.py -n 10000 -f 257 -s 1 -o "Data\Samples\random-10000-1_clusters-0.train"

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", help="elements in the dataset", type=int, nargs='?', const=1, default=100)
parser.add_argument("-f", help="features in the dataset", type=int, nargs='?', const=1, default=4)
parser.add_argument("-s", help="random seed value", type=int, nargs='?', const=1, default=-1)
parser.add_argument("-c", help="number of clusters", type=int, nargs='?', const=1, default=0)
parser.add_argument("-std", help="number of stddev", type=int, nargs='?', const=1, default=1)
parser.add_argument("-o", help="output file", nargs='?', const=1)
args = parser.parse_args()

delimiter = " "
n = args.n
f = args.f
seed = args.s
name = args.o
clusters = args.c
std = args.std
# No seed by default.
if seed > -1:
	np.random.seed(seed)
clustered_seed = 12321

# Default name
if not name:
	name_tmpl = string.Template("Data/random-dataset-$number-$features-$clusters.csv")
	name = name_tmpl.substitute(number=str(n), features=str(f), clusters=str(clusters))

def generate_data(n, f, output):
	data = np.random.rand(n,f)
	np.savetxt(name, data, delimiter=delimiter, fmt="%1.2f", newline="\n")
	print("filename:\t" + name)


# small std => more clustered data, while bigger std => points more distributed from each other
# clusters are always going to be located in the same place, because we use the clustered_seed, which is constant
def generate_clustered_data(n, f, c, clustered_seed, std, seed=None):
	np.random.seed(clustered_seed)
	centers = np.random.uniform(-10,10,(c,f))
	data, labels = make_blobs(n_samples=n, n_features=f, cluster_std=std,
                              centers=centers, shuffle=True, random_state=seed)
	np.savetxt(name, data, delimiter=delimiter, fmt="%1.2f", newline="\n")
	print("filename:\t" + name)
	

if clusters > 0:
	generate_clustered_data(n, f, clusters, clustered_seed, std, seed)
else:
	generate_data(n, f, name)
