#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 2 4 8 16 32 64 128 256 )
i=$1
for n in "${sample_sizes[@]}"
do
    for c in "${hypersphere_count[@]}"
    do
        echo "${n} ${i} ${c}"
        python train-cli.py -i "Data/Profinew/Experiment_1-1-2/profi-${n}-$i.train" -m "Experiments2/Experiment_1-1-2-notraining/Models/profi-$n-${i}-c$c.model" -c $c > "Experiments2/Experiment_1-1-2-notraining/Results/profi-${n}-$i-c$c.result"
    done
done