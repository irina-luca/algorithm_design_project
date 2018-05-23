echo "Generating d-60 c-32"
python sample-generator.py -n 10000 -f 60 -s 1 -c 32 -o Data/Metrics/random_10000_d60_cl32_1.train
python sample-generator.py -n 10000 -f 60 -s 2 -c 32 -o Data/Metrics/random_10000_d60_cl32_2.train
python sample-generator.py -n 10000 -f 60 -s 3 -c 32 -o Data/Metrics/random_10000_d60_cl32_3.train
python sample-generator.py -n 10000 -f 60 -s 4 -c 32 -o Data/Metrics/random_10000_d60_cl32_4.train
python sample-generator.py -n 10000 -f 60 -s 5 -c 32 -o Data/Metrics/random_10000_d60_cl32_5.train
python sample-generator.py -n 10000 -f 60 -s 6 -c 32 -o Data/Metrics/random-10000_d60_cl32.test

echo "Generating d-257 c-32"
python sample-generator.py -n 10000 -f 257 -s 1 -c 32 -o Data/Metrics/random_10000_d257_cl32_1.train
python sample-generator.py -n 10000 -f 257 -s 2 -c 32 -o Data/Metrics/random_10000_d257_cl32_2.train
python sample-generator.py -n 10000 -f 257 -s 3 -c 32 -o Data/Metrics/random_10000_d257_cl32_3.train
python sample-generator.py -n 10000 -f 257 -s 4 -c 32 -o Data/Metrics/random_10000_d257_cl32_4.train
python sample-generator.py -n 10000 -f 257 -s 5 -c 32 -o Data/Metrics/random_10000_d257_cl32_5.train
python sample-generator.py -n 10000 -f 257 -s 6 -c 32 -o Data/Metrics/random-10000_d257_cl32.test

