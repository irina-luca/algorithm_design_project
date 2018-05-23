sphere_sizes=(2 4 8 16 32 64 128 256)

for c in "${sphere_sizes[@]}"
do
	for i in $(seq 1 5)
    	do
        	echo "${c} ${i}"
        	python train-cli.py -i Data/Experiment_1-3-1/profi-10000-${i}.train -m Experiments/Experiment_1-3-1/Models/c${c}_i${i}.model -c ${c} > Experiments/Experiment_1-3-1/Results/c${c}_i${i}.output
		
		python print-hypersphere.py -m Experiments/Experiment_1-3-1/Models/c${c}_i${i}.model > Experiments/Experiment_1-3-1/Results/c${c}_i${i}.result
    done
done


