echo "10000-test"
tail -n +1 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-1.test
echo "[DEBUG] First done"
tail -n +10000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-2.test
tail -n +20000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-3.test
tail -n +30000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-4.test
echo "[DEBUG] Fourth done"
tail -n +40000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-5.test
echo "10000-train"
tail -n +50000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-1.train
tail -n +60000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-2.train
tail -n +70000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-3.train
tail -n +80000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-4.train
tail -n +90000 Data/descriptors-decaf-reduced-and-normalized.data | head -10000 > Data/profi-10000-5.train
echo "100000-test"
tail -n +100000 Data/descriptors-decaf-reduced-and-normalized.data | head -100000 > Data/profi-100000-1.test
tail -n +200000 Data/descriptors-decaf-reduced-and-normalized.data | head -100000 > Data/profi-100000-2.test
tail -n +300000 Data/descriptors-decaf-reduced-and-normalized.data | head -100000 > Data/profi-100000-3.test
tail -n +400000 Data/descriptors-decaf-reduced-and-normalized.data | head -100000 > Data/profi-100000-4.test
tail -n +500000 Data/descriptors-decaf-reduced-and-normalized.data | head -100000 > Data/profi-100000-5.test
