measure="jaccard"
echo "$measure"

k=10
metric=0
echo "k = $k"
#python measurements-main.py -m "Experiments/Experiment_2-5-1/model.config" -t "Experiments/Experiment_2-5-1/test.config" -k $k -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-5-1/Results/$measure.k$k.result"

k=100
echo "k = $k"
#python measurements-main.py -m "Experiments/Experiment_2-5-1/model.config" -t "Experiments/Experiment_2-5-1/test.config" -k $k -b 10 -q 1000 -mi $metric > "Experiments/Experiment_2-5-1/Results/$measure.k$k.result"

k=1000
echo "k = $k"
#python measurements-main.py -m "Experiments/Experiment_2-5-1/model.config" -t "Experiments/Experiment_2-5-1/test.config" -k $k -b 10 -q 100 -mi $metric > "Experiments/Experiment_2-5-1/Results/$measure.k$k.result"