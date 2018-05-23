samplesizes=(10000)
samplecount=10

for size in "${samplesizes[@]}"
do
    for sample in $(seq 1 $samplecount)
    do
        echo "${size} ${sample}"
        shuf -n $size Data/descriptors-decaf-reduced-and-normalized.data > Data/profi-$size-$sample.train
    done
done