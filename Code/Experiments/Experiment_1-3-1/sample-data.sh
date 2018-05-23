echo "Extracting sample data for experiment 1-3-1"
samplesizes=(10000)
samplecount=5

for size in "${samplesizes[@]}"
do
    for sample in $(seq 1 $samplecount)
    do
        echo "${size} ${sample}"
        shuf -n $size Data/descriptors-decaf-reduced-and-normalized.data > Data/Experiment_1-3-1/profi-$size-$sample.train
    done
done
