#!/usr/bin/env bash

k=100
i=$1
python measurements-main.py -m "Experiments2/Experiment_2-6-1_IrinasAlg/model-test.conf" -t "Experiments2/Experiment_2-6-1_IrinasAlg/test-$1.conf" -k $k -b 10 -q 10000 -mi 0 > "Experiments2/Experiment_2-6-1_IrinasAlg/Results/norerank-$1-test.result"