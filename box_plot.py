import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

input_file = 'iris_data_set/iris.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')
fig = plt.figure()

# Check if data file exists
if not os.path.exists(input_file):
    sys.exit("File %s couldn't be found" % input_file)

with open(input_file, 'r') as iris_data:
    irises = csv.reader(iris_data)
    iris_information = []
    for iris in irises:
        iris_information.append(iris)
    iris_array = np.array(iris_information)

setosa_petal_length = []
versicolor_petal_length = []
virginica_petal_length = []

for petal in range(0, len(iris_array)-1):
    if iris_array[petal][4] == 'Iris-setosa':
        setosa_petal_length.append(float(iris_array[petal][2]))

    elif iris_array[petal][4] == 'Iris-versicolor':
        versicolor_petal_length.append(float(iris_array[petal][2]))

    elif iris_array[petal][4] == 'Iris-virginica':
        virginica_petal_length.append(float(iris_array[petal][2]))

petal_lengths = [setosa_petal_length, versicolor_petal_length,
                 virginica_petal_length]


plt.boxplot(petal_lengths)

plt.axis([0, 4, 0, 10])

plt.xticks([1, 2, 3], ['Setosa', 'Versicolor', 'Virginica'])

plt.title("Fisher's Iris Data Set, Petal Length", fontsize=12, loc="left")
plt.xlabel("Iris Variety", fontsize=10)
plt.ylabel("Petal length (cm)", fontsize=10)

fig.savefig('boxplot.png')
#plt.show()
