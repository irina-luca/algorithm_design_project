#!/usr/bin/env bash

k=100
i=$1
python measurements-main.py -m "Experiments2/Experiment_2-6-1/model.conf" -t "Experiments2/Experiment_2-6-1/test-$1.conf" -k $k -b 10 -q 10000 -mi 0 > "Experiments2/Experiment_2-6-1/Results/norerank-$1.result"