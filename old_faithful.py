import csv
import matplotlib.pyplot as plt
import os
import sys

input_file = 'old_faithful.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')

# Check if data file exists
if not os.path.exists(input_file):
    sys.exit("File %s couldn't be found" % input_file)

with open(input_file, 'r') as old_faithful_data:
    eruptions = list(csv.reader(old_faithful_data))

eruptions.pop(0)

eruption_time = []
waiting_time = []
for event in range(0, len(eruptions)-1):
    eruption_time.append(float(eruptions[event][0]))
    waiting_time.append(float(eruptions[event][1]))

plt.subplot(2, 2, 1)
plt.boxplot(eruption_time)
plt.title('Old Faithful Eruptions (BoxPlot)')
plt.xticks([1], ['Eruptions'])
plt.xlabel('Length of Eruption (minutes)')

plt.subplot(2, 2, 2)
num_bins = 8
plt.hist(eruption_time, num_bins)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (minutes)')

plt.subplot(2, 2, 3)
plt.boxplot(waiting_time)
plt.title('Old Faithful Waiting')
plt.xticks([1], ['Waiting Time'])
plt.xlabel('Time between eruptions (minutes)')

plt.subplot(2, 2, 4)
plt.scatter(eruption_time, waiting_time)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (minutes)')
plt.ylabel('Time Between Eruption (minutes)')
plt.tight_layout()

plt.show()


