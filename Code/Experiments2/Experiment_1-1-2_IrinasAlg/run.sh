#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 8 16 32 64 )
i=$1
for n in "${sample_sizes[@]}"
do
    for c in "${hypersphere_count[@]}"
    do
        echo "${n} ${i} ${c}"
        python train-cli.py -i "Data/Experiment_1-1-2/new_profi/profi-${n}-$i.test" -m "Experiments2/Experiment_2-6-1_IrinasAlg/ModelsNew/profi-$n-${i}-c$c.model" -c $c > "Experiments2/Experiment_2-6-1_IrinasAlg/TrainingResultsNew/profi-${n}-$i-c$c.result"
    done
done