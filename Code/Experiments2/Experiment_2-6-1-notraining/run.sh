#!/usr/bin/env bash

k=100
i=$1
python measurements-main.py -m "Experiments2/Experiment_2-6-1-notraining/model.conf" -t "Experiments2/Experiment_2-6-1-notraining/test-$1.conf" -k $k -b 10 -q 1000 -mi 0 > "Experiments2/Experiment_2-6-1-notraining/Results/norerank-$1.result"