#!/usr/bin/env bash

metric=$1
measure=$2
i=$3
q=$4
k=100

echo "$measure ($metric), k = $k, i=$i, q = $q"
python measurements-main.py -m "Experiments2/Experiment_2-5-2/model.conf" -t "Experiments2/Experiment_2-5-2/test-$i.conf" -k $k -b 10 -q $q -mi $metric > "Experiments2/Experiment_2-5-2/Results/$measure.k$k-$i.result"