#!/bin/bash

number_of_clusters_in_dataset=( 16 )
hypersphere_count=( 2 4 8 16 32 64 128 256 )
sample_sizes=( 10000 )


for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            for cl in "${number_of_clusters_in_dataset[@]}"
            do
                echo "Data/Experiment_1-1-7/clustered-$n-$i-$cl-$c.train"
                python train-cli.py -i "Data/Experiment_1-1-7/clustered-$n-$i-$cl-$c.train" -m "Experiments/Experiment_1-1-7/Models/clustered-$n-$i-$cl-$c.model" -c $c > "Experiments/Experiment_1-1-7/Results/clustered-$n-$i-$cl-$c.result"
                echo "FINISHED training && Storing results for => Data/Experiment_1-1-7/clustered-$n-$i-$cl-$c.train"
                printf "\n"
            done
        done
    done
done
