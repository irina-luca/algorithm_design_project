#!/usr/bin/env bash

metric=$1
measure=$2
k=$3

echo "$measure ($metric), k = $k"
python measurements-main.py -m "Experiments2/Experiment_2-5-1/model.conf" -t "Experiments2/Experiment_2-5-1/test.conf" -k $k -b 10 -q 10000 -mi $metric > "Experiments2/Experiment_2-5-1/Results/$measure.k$k.result"