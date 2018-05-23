dimension_sizes=(60,257)
sphere_sizes=(32,64,128)

for ds in "${dimension_sizes[@]}"
do
	for ss in "${sphere_sizes[@]}"
	do
		for i in $(seq 1 5)
	    do
	        echo "${ds} ${ss} ${i}"
	        python train-cli.py -i Data/Metrics/random_10000_d$ds_cl32_$i.train -m Data/Models/metric-10000_d$ds_cl32_c$ss_$i.model -c $ss
	    done
	done
done
