#!/bin/bash

sample_sizes=(10000)
c=128
i=$1
for n in "${sample_sizes[@]}"
do
    echo "${n} ${i} ${c}"
    python train-cli.py -i "Data/Experiment_2-6-1/Dimension-reduced-samples/profi-$n-$i.test" -m "Experiments/Experiment_1-1-1_IrinasAlg/Models/profi-$n-${i}-c$c.model" -c $c > "Experiments/Experiment_1-1-1_IrinasAlg/Results/profi-${n}-$i-c$c.result"
done