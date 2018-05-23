#!/bin/bash

number_of_clusters_for_data_generation=( 8 16 32 )
hypersphere_count=( 4 )

for cl in "${number_of_clusters_for_data_generation[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            echo "START training && Storing results for => Data/Samples/clustered-10000-$cl-$i-$c.train"
            python train-cli.py -i "Data/Samples/clustered-10000-$cl-${i}.train" -m "Data\Models\clustered-10000-$cl-${i}.model" -c $c > "Data\Results\clustered-10000-$cl-${i}.result"
            echo "FINISHED training && Storing results for => Data/Samples/clustered-10000-$cl-$i-$c.train"
        done
    done
done