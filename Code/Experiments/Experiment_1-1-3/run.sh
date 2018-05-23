#!/bin/bash

sample_sizes=( 1000 10000 100000 )
hypersphere_count=( 128 )

for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            echo "START training && Storing results for => Data/Experiment_1-1-3/random-$n-$i.train"
            python train-cli.py -i "Data/Experiment_1-1-3/random-$n-$i.train" -m "Experiments/Experiment_1-1-3/Models/random-$n-$i-$c.model" -c $c > "Experiments/Experiment_1-1-3/Results/random-$n-$i-$c.result"
            echo "FINISHED training && Storing results for => Data/Experiment_1-1-3/random-$n-$i.train"
        done
    done
done