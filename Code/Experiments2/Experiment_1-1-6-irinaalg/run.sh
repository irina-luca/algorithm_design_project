#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 2 4 8 16 32 64 128 256 )
i=$1
for n in "${sample_sizes[@]}"
do
    for c in "${hypersphere_count[@]}"
    do
        echo "${n} ${i} ${c}"
        python train-cli.py -i "Data/Samples/clustered-${n}-f256-c2-$i.train" -m "Experiments2/Experiment_1-1-6-irinaalg/Models/clustered-cl2-$n-${i}-c$c.model" -c $c > "Experiments2/Experiment_1-1-6-irinaalg/Results/clustered-${n}-cl2-$i-c$c.result"
    done
done