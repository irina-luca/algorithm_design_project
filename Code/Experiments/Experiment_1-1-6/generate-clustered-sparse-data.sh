#!/bin/bash

number_of_clusters_in_dataset=( 2 )
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
                    echo "START: Sample Generation, Experiment_1-1-6 => Data/Experiment_1-1-6/clustered-$n-$i-$cl-$c.train"
                    python sample-generator.py -o "Data/Experiment_1-1-6/clustered-$n-$i-$cl-$c.train" -n $n -f 257 -s $i -c $cl
                    echo "END: Sample Generation, Experiment_1-1-6 => Data/Experiment_1-1-6/clustered-$n-$i-$cl-$c.train"
                    printf "\n"
                done
            done
    done
done
