#!/bin/bash

sample_sizes=( 10000 )
hypersphere_count=( 2 4 8 16 32 64 128 256 )

for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        for c in "${hypersphere_count[@]}"
        do
            echo "START: Sample Generation, Experiment_1-1-4 => Data/Experiment_1-1-4/random-$n-$i.train"
            python sample-generator.py -o "Data/Experiment_1-1-4/random-$n-$i.train" -n $n -f 257 -s $i
            echo "END: Sample Generation, Experiment_1-1-4 => Data/Experiment_1-1-4/random-$n-$i.train"
            printf "\n"
        done
    done
done