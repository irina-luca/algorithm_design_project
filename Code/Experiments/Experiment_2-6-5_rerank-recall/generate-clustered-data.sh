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
                    echo "START: Sample Generation, Experiment_2-6-5 => Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.train"
                    python sample-generator.py -o "Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.train" -n $n -f 257 -s $i -c $cl
                    python sample-generator.py -o "Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.test" -n $n -f 257 -s $i -c $cl
                    echo "END: Sample Generation, Experiment_2-6-5 => Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.train"
                    printf "\n"
                done
            done
    done
done
