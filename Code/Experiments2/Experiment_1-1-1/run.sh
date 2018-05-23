#!/bin/bash

sample_sizes=( 100000 )
c=128
i=$1
for n in "${sample_sizes[@]}"
do
    echo "${n} ${i} ${c}"
<<<<<<< HEAD
    python train-cli.py -i "Data/Experiment_2-6-1/Dimension-reduced-samples/profi-${n}-$i.test" -m "Experiments2/Experiment_1-1-1/Models/profi-$n-${i}-c$c.model" -c $c > "Experiments2/Experiment_1-1-1/Results/profi-${n}-$i-c$c.result"
=======
    python train-cli.py -i "Data/Profinew/Experiment_1-1-1/profi-$n-$i.train" -m "Experiments2/Experiment_1-1-1/Models/profi-$n-${i}-c$c.model" -c $c > "Experiments2/Experiment_1-1-1/Results/profi-${n}-$i-c$c.result"
>>>>>>> d40ac720ed82ff2a9cd6dfe014a51a084beae754
done