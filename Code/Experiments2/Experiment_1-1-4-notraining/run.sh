#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 2 4 8 16 32 64 128 256 )
i=$1
for n in "${sample_sizes[@]}"
do
    for c in "${hypersphere_count[@]}"
    do
        echo "${n} ${i} ${c}"
        python train-cli.py -i "Data/Samples/random-${n}-$i.train" -m "Experiments2/Experiment_1-1-4-notraining/Models/random-$n-${i}-c$c.model" -c $c > "Experiments2/Experiment_1-1-4-notraining/Results/random-${n}-$i-c$c.result"
    done
done