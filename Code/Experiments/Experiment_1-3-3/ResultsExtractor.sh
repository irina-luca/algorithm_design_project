clusters=(2 4 8 16 32 64)

for cl in "${clusters[@]}"
do
	python HypersphereAnalysis.py -i Results/cl${cl}_i -c 64 >> Hyperespheres.results
done


