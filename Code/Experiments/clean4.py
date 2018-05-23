import pickle
import sys
import numpy as np

#[RESULT][MODEL]Experiments/Experiment_2-5-1/Models/profi-10000-1-c64.model;[SAMPLE]Data/Experiment_2-5-1/profi-100000-1.test;(2,0.00018),(4,0.00018),(8,0.00018),(16,0.00018),(32,0.00018),(64,0.00018),(128,0.00018),(256,0.00018),(512,0.00018),(1024,0.00018),(2048,0.00018),(4096,0.00018),(8192,0.00018),(16384,0.00018),(32768,0.00018),(65536,0.36648),(131072,1.0);0.00018

for line in sys.stdin:
    tokens = line.split(" ; ")
    current_model = tokens[0]
    current_sample = tokens[1]
    recall = ":".join(tokens[2].replace(" ","").replace("[","").replace("]", "").split("),(")).replace("(", "").replace(")","").replace(", ", ",")
    result = current_model + ";" + current_sample + ";" + recall + ";" + tokens[-1]
    sys.stdout.write(result)