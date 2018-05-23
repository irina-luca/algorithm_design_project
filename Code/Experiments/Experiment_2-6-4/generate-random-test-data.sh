#!/bin/bash

sample_sizes=( 10000 )
dimensions=(64)
for n in "${sample_sizes[@]}"
do
    for d in "${dimensions[@]}"
    do
        for i in $(seq 1 5)
        do
            echo "START: Sample Generation, Experiment_2-6-4 => Data/Experiment_2-6-4/random-$n-$d-$i.test"
            python sample-generator.py -o "Data/Experiment_2-6-4/random-$n-$d-$i.test" -n $n -f $d -s $i
            echo "END: Sample Generation, Experiment_2-6-4 => Data/Experiment_2-6-4/random-$n-$d-$i.test"
            printf "\n"
        done
    done
done