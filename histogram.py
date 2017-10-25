import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

input_file = 'iris_data_set/iris.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')

# Check if data file exists
if not os.path.exists(input_file):
    sys.exit("File %s couldn't be found" % input_file)

with open(input_file, 'r') as iris_data:
    irises = csv.reader(iris_data)
    iris_information = []
    for iris in irises:
        iris_information.append(iris)
    iris_array = np.array(iris_information)

virginica_petal_length = []
num_bins = 10

for petal in range(0, len(iris_array)-1):
    if iris_array[petal][4] == 'Iris-virginica':
        virginica_petal_length.append(float(iris_array[petal][2]))

plt.hist(virginica_petal_length, num_bins, facecolor='red',
         alpha=0.75)

plt.show()
