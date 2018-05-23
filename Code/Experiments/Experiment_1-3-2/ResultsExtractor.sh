sphere_sizes=(2 4 8 16 32 64 128 256)

for c in "${sphere_sizes[@]}"
do
	python HypersphereAnalysis.py -i Results/c${c}_i -c $c >> Hyperespheres.results
done


