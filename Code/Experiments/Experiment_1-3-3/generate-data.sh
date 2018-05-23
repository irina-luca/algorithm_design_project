echo "Generating experiment 1.3.3 data"
clusters=(2 4 8 16 32 64)

for cl in "${clusters[@]}"
do
	for i in $(seq 1 5)
    	do
        	echo "${cl} ${i}"
		python sample-generator.py -n 10000 -f 257 -s $i -c $cl -o Data/Experiment_1-3-3/experiment_1-3-3_d257_cl${cl}_i${i}.train
    		done
done
