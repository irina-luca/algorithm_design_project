#!/usr/bin/env bash

metric=3
measure="hamming"

k=10
./Experiments2/Experiment_2-5-1/run.sh $metric $measure $k
k=100
./Experiments2/Experiment_2-5-1/run.sh $metric $measure $k
k=1000
./Experiments2/Experiment_2-5-1/run.sh $metric $measure $k