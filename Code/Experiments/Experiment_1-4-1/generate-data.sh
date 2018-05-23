echo "Generating experiment 1.4.1 data"
clusters=(2 4 8 16 32 64)
dimensions=(2 4 8 16 32 64 128)

for cl in "${clusters[@]}"
do
	for d in "${dimensions[@]}"
		echo "${cl} ${i}"
		python sample-generator.py -n 10000 -f $d -s 1 -c $cl -o Data/experiment_1-4-1_d${d}_cl${cl}.train
	done
done
