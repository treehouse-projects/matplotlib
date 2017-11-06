import csv
import matplotlib.pyplot as plt
import os
import sys

from matplotlib.backends.backend_pdf import PdfPages


input_file = 'old_faithful.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')
pp = PdfPages('old_faithful_multi.pdf')
fig = plt.figure()

# Check if data file exists
if not os.path.exists(input_file):
    sys.exit("File %s couldn't be found" % input_file)

with open(input_file, 'r') as old_faithful_data:
    eruptions = csv.reader(old_faithful_data)
    old_faithful_info = []
    for eruption in eruptions:
        old_faithful_info.append(eruption)
old_faithful_info.pop(0)

eruption_time = []
waiting_time = []
for event in range(0, len(old_faithful_info)-1):
    eruption_time.append(float(old_faithful_info[event][0]))
    waiting_time.append(float(old_faithful_info[event][1]))

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

fig.savefig('sample.png')
pp.savefig()
pp.close()

plt.show()


