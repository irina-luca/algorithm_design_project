#!/usr/bin/env bash
k=100
metric=3
measure="hamming"
echo "$measure"

python measurements-main.py -m "Experiments/Experiment_2-5-2/model.config" -t "Experiments/Experiment_2-5-2/test.config" -k $k -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-5-2/Results/$measure.k$k.result"