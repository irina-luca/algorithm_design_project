measure="jaccard"
echo "$measure"

k=100
r=1000
metric=0
echo "k = $k"
python measurements-main.py -m "Experiments/Experiment_2-6-1_rerank-recall/model.config" -t "Experiments/Experiment_2-6-1_rerank-recall/test.config" -k $k -r $r -b 10 -q 10000 -mi $metric > "Experiments/Experiment_2-6-1_rerank-recall/Results/$measure.k$k.r$r.rerankrecall.versions2.result"


# if I increase k by a factor of 10, I decrease q by a number of 10