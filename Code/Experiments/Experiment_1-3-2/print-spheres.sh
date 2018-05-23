echo "Training experiment 1.3.2 models"
hyperspheres=(2 4 8 16 32 64 128 256)

for c in "${hyperspheres[@]}"
do
	for i in $(seq 1 5)
    	do
        	echo "${c} ${i}"	
		python print-hypersphere.py -m Experiments/Experiment_1-3-2/Models/Experiment_1-3-2_c${c}_i${i}.model -t > Experiments/Experiment_1-3-2/Results/c${c}_i${i}.result	
    	done
done
