#!/usr/bin/env bash
# Same as running the others sequentially.
k=100

metric=2
measure="and"
echo "$measure"
python measurements-main.py -m "Experiments/Experiment_2-5-2/model.config" -t "Experiments/Experiment_2-5-2/test.config" -k $k -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-5-2/Results/$measure.k$k.result"

metric=1
measure="shd"
echo "$measure"
python measurements-main.py -m "Experiments/Experiment_2-5-2/model.config" -t "Experiments/Experiment_2-5-2/test.config" -k $k -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-5-2/Results/$measure.k$k.result"

metric=0
measure="jaccard"
echo "$measure"
python measurements-main.py -m "Experiments/Experiment_2-5-2/model.config" -t "Experiments/Experiment_2-5-2/test.config" -k $k -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-5-2/Results/$measure.k$k.result"

