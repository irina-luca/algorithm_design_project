#!/bin/bash


measure="jaccard"
echo "$measure"

k=100
r=1000
metric=0
echo "k = $k"

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
                    echo "Experiments/Experiment_2-6-5_rerank-recall/Models/clustered-$n-$c-$cl-$i.model" > Experiments/Experiment_2-6-5_rerank-recall/model.config
                    echo "Data/Experiment_2-6-5/clustered-$n-$c-$cl-$i.test" > Experiments/Experiment_2-6-5_rerank-recall/test.config
                    python measurements-main.py -m "Experiments/Experiment_2-6-5_rerank-recall/model.config" -t "Experiments/Experiment_2-6-5_rerank-recall/test.config" -k $k -r $r -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-6-5_rerank-recall/NewResults/$measure.k$k.r$r.clustered-$n-$c-$cl-$i.result"

                done
        done
    done
done


# if I increase k by a factor of 10, I decrease q by a number of 10