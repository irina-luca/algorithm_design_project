echo "Training experiment 1.3.2 models"
hyperspheres=(2 4 8 16 32 64 128 256)

for c in "${hyperspheres[@]}"
do
	for i in $(seq 1 5)
    	do
        	echo "${c} ${i}"
        	python train-cli.py -i Data/Experiment_1-3-2/experiment_1-3-2_d257_${i}.train -m Experiments/Experiment_1-3-2/Models/c${c}_i${i}.model -c ${c} 
		
		python print-hypersphere.py -m Experiments/Experiment_1-3-2/Models/c${c}_i${i}.model > Experiments/Experiment_1-3-2/Results/c${c}_i${i}.result
    	done
done
