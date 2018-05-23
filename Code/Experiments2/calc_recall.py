import sys
import numpy as np

current_groupby_key = 0
groupby_dict_recall = dict()
groupby_dict_precision = dict()
for line in sys.stdin:
    if line.startswith("#"):
        continue

    tokens = line.split(";")
    if tokens[0]:
        current_groupby_key = tokens[0]

    model = tokens[1][tokens[1].rfind("/")+1:]
    sample = tokens[2][tokens[2].rfind("/")+1:]
    recall = [tuple(map(float, pair.split(","))) for pair in tokens[3].split(":")]
    precision = tokens[4].replace("\n", "")

    if not current_groupby_key in groupby_dict_recall:
        groupby_dict_recall[current_groupby_key] = []
        groupby_dict_precision[current_groupby_key] = []

    groupby_dict_recall[current_groupby_key].append(recall)
    groupby_dict_precision[current_groupby_key].append(float(precision))


print "Recall"
for key, group in groupby_dict_recall.iteritems():
    current_sums = group[0]
    for recalls in group[1:]:
        for i, reading in enumerate(recalls):
            old_sum = current_sums[i][1]
            current_sums[i] = (reading[0], reading[1] + old_sum)

    average_recalls = ["("+str(retreived_samples)+", "+ str(recall / len(group))+")" for (retreived_samples, recall) in current_sums]
    print key
    print "\n".join(average_recalls)

print ""
print "Precision"
for key, group in groupby_dict_precision.iteritems():
    numpy_group = np.array(group)
    print key
    print np.mean(numpy_group), "+-", np.std(numpy_group)