import algorithm
import algorithm_improvements
import pickle
import numpy as np
from hypersphere import HypersphereModel


def train_model(input, output, c, error_tolerance_m, error_tolerance_s, delimiter=','):
    sample = np.genfromtxt(input, delimiter=delimiter, dtype=np.float64)
    print "normalizing"
    sample, min, max = algorithm.normalize_data(sample)
    model = algorithm_improvements.spherical_hashing(sample, c, error_tolerance_m, error_tolerance_s, True)

    #text_file = open(output+".txt", "w")
    #for sphere in model:
    #    text_file.write(str(sphere.center)+"\n")
    #    
    #text_file.write("\n")
    #for sphere in model:
    #    text_file.write(str(sphere.threshold)+"\n")    
    #text_file.close()    
    pickle.dump(HypersphereModel(min, max, model), open(output, "wb"))