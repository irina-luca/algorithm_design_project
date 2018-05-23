#!/bin/bash

sample_sizes=( 10000 )
for n in "${sample_sizes[@]}"
do
	for i in $(seq 1 5)
    do
        echo "START: Sample Generation, Experiment_2-6-3 => Data/Experiment_2-6-3/random-$n-$i.test"
        python sample-generator.py -o "Data/Experiment_2-6-3/random-$n-$i.test" -n $n -f 257 -s $i
        echo "END: Sample Generation, Experiment_2-6-3 => Data/Experiment_2-6-3/random-$n-$i.test"
        printf "\n"
    done
done