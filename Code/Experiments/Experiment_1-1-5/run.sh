#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 128 )
number_of_dimensions=( 2 4 8 16 32 64 128 256 )

for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            for d in "${number_of_dimensions[@]}"
            do
                echo "START training && Storing results for => Data/Experiment_1-1-5/random-$n-$i-$c-$d.train"
                python train-cli.py -i "Data/Experiment_1-1-5/random-$n-$i-$c-$d.train" -m "Experiments/Experiment_1-1-5/Models/random-$n-$i-$c-$d.model" -c $c > "Experiments/Experiment_1-1-5/Results/random-$n-$i-$c-$d.result"
                echo "FINISHED training && Storing results for => Data/Experiment_1-1-5/random-$n-$i-$c-$d.train"
                printf "\n"
            done
        done
    done
done