#!/bin/bash

number_of_clusters_in_dataset=( 2 4 8 16 32 64 128 256 )
hypersphere_count=( 64 )
sample_sizes=( 10000 )


for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
            do
            for cl in "${number_of_clusters_in_dataset[@]}"
                do
                    echo "START training Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.train"
                    python train-cli.py -i "Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.train" -m "Experiments/Experiment_2-6-5/Models/clustered-$n-$c-$cl-$i.model" -c $c > "Experiments/Experiment_2-6-5/Results/training-results.result"
                    echo "FINISHED training Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.train"
                    printf "\n"
                done
            done
    done
done