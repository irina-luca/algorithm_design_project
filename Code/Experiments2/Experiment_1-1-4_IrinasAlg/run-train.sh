#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 2 4 8 16 32 64 128 256 )

for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do

            python train-cli.py -i "Data/Experiment_1-1-4/random-$n-$i.train" -m "Experiments2/Experiment_1-1-4_IrinasAlg/Models/random-$n-$i-$c.model" -c $c > "Experiments2/Experiment_1-1-4_IrinasAlg/Results/random-$n-$i-$c.result"

        done
    done
done