echo "Training experiment 1.3.3 models"
clusters=(2 4 8 16 32 64)
for cl in "${clusters[@]}"
do
	for i in $(seq 1 5)
    	do
        	echo "${cl} ${i}"
        	python train-cli.py -i Data/Experiment_1-3-3/experiment_1-3-3_d257_cl${cl}_i${i}.train -m Experiments/Experiment_1-3-3/Models/cl${cl}_i${i}.model -c 64 > Experiments/Experiment_1-3-3/Results/cl${cl}_i${i}.output
		
		python print-hypersphere.py -m Experiments/Experiment_1-3-3/Models/cl${cl}_i${i}.model > Experiments/Experiment_1-3-3/Results/cl${cl}_i${i}.result
    	done
done
