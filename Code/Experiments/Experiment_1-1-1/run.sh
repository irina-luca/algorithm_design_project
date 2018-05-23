#!/bin/bash

sample_sizes=( 1000 10000 100000 )
hypersphere_count=( 128 )

for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            echo "Data/Experiment_1-1-1/profi-${i}_$n.train"
            python train-cli.py -i "Data/Experiment_1-1-1/profi-${i}_$n.train" -m "Experiments/Experiment_1-1-1/Models/profi-${i}_$n-$c.model" -c $c > "Experiments/Experiment_1-1-1/Results/profi-${i}_$n-$c.result"
            echo "FINISHED training && Storing results for => Data/Experiment_1-1-1/profi-${i}_$n.train"
        done
    done
done