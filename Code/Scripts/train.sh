c_sizes=(512)

for c in "${c_sizes[@]}"
do
    for i in $(seq 1 5)
    do
        echo "${i} ${c}"
        python train-cli.py -i Data/Samples/gist-10000-$i.train -m Data/Models/profi-10000-$i-c$c.model -c $c
    done
done
