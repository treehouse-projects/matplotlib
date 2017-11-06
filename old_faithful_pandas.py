import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

input_file = 'old_faithful.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')


# Check if data file exists
if not os.path.exists(input_file):
    sys.exit("File %s couldn't be found" % input_file)

old_faithful = pd.read_csv(input_file)

print(old_faithful.head())

old_faithful.columns = ['eruptions', 'waiting']

plt.subplot(2, 2, 1)
plt.scatter(old_faithful.eruptions, old_faithful.waiting)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (minutes)')
plt.ylabel('Time Between Eruption (minutes)')

plt.subplot(2, 2, 2)
plt.boxplot(old_faithful.eruptions)
plt.title('Old Faithful Eruptions (BoxPlot)')
plt.xticks([1], ['Eruptions'])
plt.xlabel('Length of Eruption (minutes)')

plt.subplot(2, 2, 3)
plt.boxplot(old_faithful.waiting)
plt.title('Old Faithful Waiting')
plt.xticks([1], ['Waiting Time'])
plt.xlabel('Time between eruptions (minutes)')

plt.subplot(2, 2, 4)
num_bins = 8
plt.hist(old_faithful.eruptions, num_bins)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (minutes)')

plt.tight_layout()
plt.show()
