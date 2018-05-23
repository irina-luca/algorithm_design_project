measure="and"
echo "$measure"

k=10
metric=2
echo "k = $k"
#python measurements-main.py -m "Experiments/Experiment_2-5-1/model.config" -t "Experiments/Experiment_2-5-1/test.config" -k $k -b 10 -q 3500 -mi $metric > "Experiments/Experiment_2-5-1/Results/$measure.k$k.result"

k=100
echo "k = $k"
#python measurements-main.py -m "Experiments/Experiment_2-5-1/model.config" -t "Experiments/Experiment_2-5-1/test.config" -k $k -b 10 -q 350 -mi $metric > "Experiments/Experiment_2-5-1/Results/$measure.k$k.result"

k=1000
echo "k = $k"
#python measurements-main.py -m "Experiments/Experiment_2-5-1/model.config" -t "Experiments/Experiment_2-5-1/test.config" -k $k -b 10 -q 35 -mi $metric > "Experiments/Experiment_2-5-1/Results/$measure.k$k.result"
