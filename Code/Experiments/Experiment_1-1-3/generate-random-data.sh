#!/bin/bash

sample_sizes=( 1000 10000 100000 )
hypersphere_count=( 128 )

for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            echo "START: Sample Generation, Experiment_1-1-3 => Data/Experiment_1-1-3/random-$n-$i.train"
            python sample-generator.py -o "Data/Experiment_1-1-3/random-$n-$i.train" -n $n -f 257 -s $i
            echo "END: Sample Generation, Experiment_1-1-3 => Data/Experiment_1-1-3/random-$n-$i.train"
            printf "\n"
        done
    done
done