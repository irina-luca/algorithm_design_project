#!/usr/bin/env bash

k=100
r=1000
i=$1
python measurements-main.py -m "Experiments2/Experiment_2-6-1/model.conf" -t "Experiments2/Experiment_2-6-1/test-$i.conf" -k $k -r 1000 -b 10 -q 10000 -mi 0 > "Experiments2/Experiment_2-6-1/Results/rerank-$i.result"