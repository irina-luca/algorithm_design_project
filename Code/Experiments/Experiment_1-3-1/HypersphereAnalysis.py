import argparse
import numpy as np
import string
 
# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="input file", nargs='?', const=1, default=100)
parser.add_argument("-c", help="number of hyperspheres", nargs='?', const=1, default=64)

args = parser.parse_args()

delimiter = " "
input_file = args.i
hyperspheres = args.c

macro_average = 0
macro_average_std = 0
for i in xrange(1,6):
	with open(input_file + str(i) + ".result") as file:
		list_avg = []
		average = 0
		for j, row in enumerate(file):
		    	ignored1, ignored2, size = row.split(delimiter)
			if ignored1 != "Total":
				list_avg.append(float(size))

	macro_average += np.mean(list_avg)
	macro_average_std = np.std(list_avg)
macro_average = macro_average / 5
macro_average_std = macro_average_std / 5
print "("+str(float(hyperspheres)) + "," + str(macro_average) + ") +- (" + str(macro_average_std) + ")"



