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
                    echo "START: Sample Generation, Experiment_1-1-5 => Data/Experiment_1-1-5/random-$n-$i-$c-$d.train"
                    python sample-generator.py -o "Data/Experiment_1-1-5/random-$n-$i-$c-$d.train" -n $n -f $d -s $i
                    echo "END: Sample Generation, Experiment_1-1-5 => Data/Experiment_1-1-5/random-$n-$i-$c-$d.train"
                    printf "\n"
                done
            done
    done
done