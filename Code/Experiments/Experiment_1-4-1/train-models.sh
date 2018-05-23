echo "Training experiment 1.4.1 models"
clusters=(2 4 8 16 32)
dimensions=(2 4 8 16 32 64 128)
spheres=(2 4 8 16 32 64 128)
for cl in "${clusters[@]}"
do
	for d in "${clusters[@]}"
    	do
        	echo "${cl} ${i}"
        	python train-cli.py -i Data/experiment_1-4-1_d257_cl${cl}_i${i}.train -m Experiments/Experiment_1-4-1/Models/cl${cl}_i${i}.model -c 128
		
		python print-hyperspheres.py -m Experiments/Experiment_1-4-1/Models/cl${cl}_i${i}.model > Experiments/Experiment_1-4-1/Results/cl${cl}_i${i}.result
    	done
done


for cl in "${clusters[@]}"
do
	for d in "${dimensions[@]}"
		echo "${cl} ${i}"
		python sample-generator.py -n 10000 -f $d -s 1 -c $cl -o Data/experiment_1-4-1_d${d}_cl${cl}.train
	done
done
