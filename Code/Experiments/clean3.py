import pickle
import sys
import numpy as np

current_model = ""
for line in sys.stdin:
    if line.startswith("[MODEL]"):
        current_model = line.split(" ")[1]
    elif line.startswith("[INFO]"):
        current_sample = line.split(" ")[1]
        tokens = line.split(" ; ")
        recall_token = tokens[1][1:-2].replace(" ", "")
        recall = ":".join(recall_token.split("),(")).replace("(", "").replace(")", "").replace(", ", ",")

        result = current_model + ";" + current_sample + ";" + recall + ";" + tokens[-1]
        sys.stdout.write(result)