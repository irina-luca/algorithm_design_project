measure="jaccard"
echo "$measure"

k=100
metric=0
echo "k = $k"
python measurements-main.py -m "Experiments/Experiment_2-6-4/model.config" -t "Experiments/Experiment_2-6-4/test.config" -k $k -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-6-4/Results/$measure-for-256d.k$k.result"


# if I increase k by a factor of 10, I decrease q by a number of 10