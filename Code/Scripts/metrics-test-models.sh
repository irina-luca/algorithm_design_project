dimension_sizes=(60,257)
sphere_sizes=(32,64,128)

for ds in "${dimension_sizes[@]}"
do
	for ss in "${sphere_sizes[@]}"
	do
		shd=0
		and=0
		jaccard=0
		for i in $(seq 1 5)
	    do
	        echo "${ds} ${ss} ${i}"
	        shd_temp=python measurements-cli.py -m Data/Models/metric-10000_d$ds_cl32_c$ss_$i.model -d Data/Metrics/random-10000_d$ds_cl32.test -k 100 -me shd
	        and_temp=python measurements-cli.py -m Data/Models/metric-10000_d$ds_cl32_c$ss_$i.model -d Data/Metrics/random-10000_d$ds_cl32.test -k 100 -me and
	        jaccard_temp=python measurements-cli.py -m Data/Models/metric-10000_d$ds_cl32_c$ss_$i.model -d Data/Metrics/random-10000_d$ds_cl32.test -k 100 -me jaccard
	    	let shd = shd+shd_temp
	    	let and = and+and_temp
	    	let jaccard = jaccard+jaccard_temp
	    done
	    let shd = shd/5
	    let and = and/5
	    let jaccard = jaccard/5
	    echo "Shd: dimensions-${ds} spheres-${ss} ${shd}"
	    echo "And: dimensions-${ds} spheres-${ss} ${and}"
	    echo "Jaccard: dimensions-${ds} spheres-${ss} ${jaccard}"
	done
done
