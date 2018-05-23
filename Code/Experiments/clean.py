import pickle
import sys
import numpy as np

# converts from form:
# MODEL=>Experiments/Experiment_2-5-1/Models/profi-10000-1-c64.model:
# SAMPLE Data/Experiment_2-5-1/profi-100000-1.test (recall;precision): [(2, 0.00031428571428571427), (4, 0.00031428571428571427), (8, 0.00031428571428571427), (16, 0.00031428571428571427), (32, 0.00031428571428571427), (64, 0.00031428571428571427), (128, 0.00031428571428571427), (256, 0.00031428571428571427), (512, 0.00031428571428571427), (1024, 0.00031428571428571427), (2048, 0.00031428571428571427), (4096, 0.00031428571428571427), (8192, 0.00031428571428571427), (16384, 0.00031428571428571427), (32768, 0.00031428571428571427), (65536, 0.2924857142857143), (131072, 1.0)] ; 0.000314285714286
# to form
# [RESULT][MODEL]Experiments/Experiment_2-6-4_rerank-recall/Models/random-10000-1-128-64.model;[SAMPLE]Data/Experiment_2-6-4/random-10000-64-1.test;(2, 0.25087),(4, 0.32725),(8, 0.42176),(16, 0.53712),(32, 0.66099),(64, 0.781),(128, 0.88269),(256, 0.9528),(512, 0.98954),(1024, 1.0),(2048, 1.0),(4096, 1.0),(8192, 1.0),(16384, 1.0);0.45734
# [RESULT][MODEL]Experiments/Experiment_2-5-1/Models/profi-10000-1-c64.model;[SAMPLE]Data/Experiment_2-5-1/profi-100000-1.test;(2,0.00018),(4,0.00018),(8,0.00018),(16,0.00018),(32,0.00018),(64,0.00018),(128,0.00018),(256,0.00018),(512,0.00018),(1024,0.00018),(2048,0.00018),(4096,0.00018),(8192,0.00018),(16384,0.00018),(32768,0.00018),(65536,0.36648),(131072,1.0);0.00018

# How to use:
# cat jaccard.k10.result.reduced | python clean.py > jaccard.k10.result.reduced.new

current_model = ""
for line in sys.stdin:
    if line.startswith("MODEL=>"):
        current_model = line.split("=>")[1][0:-2]
    elif line.startswith("SAMPLE"):
        tokens = line.split(" ")
        current_sample = tokens[1]
        recall = line[line.index("[")+1:line.index("]")].replace(" ", "")
        result = "[RESULT][MODEL]" + current_model + ";[SAMPLE]" + current_sample + ";" + recall + ";" + tokens[-1]
        sys.stdout.write(result)