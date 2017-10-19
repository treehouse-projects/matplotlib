import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

input_file = 'iris_data_set/iris.csv'
plt.figure(figsize=(10.5, 5.5))

# Check if data file exists
if not os.path.exists(input_file):
    sys.exit("File %s couldn't be found" % input_file)

with open(input_file, 'r') as iris_data:
    irises = csv.reader(iris_data)
    iris_information = []
    for iris in irises:
        iris_information.append(iris)
    iris_array = np.array(iris_information)
    colors = {"Iris-setosa": "#2B5B84", "Iris-versicolor": "#3CB878",
              "Iris-virginica": "red"}

for sepal in range(0, len(iris_array)-1):
    sepal_length, sepal_width = [iris_array[sepal][0], iris_array[sepal][1]]
    species = iris_array[sepal][4]

    if species == 'Iris-setosa':
        blue_dot = plt.scatter(sepal_length, sepal_width, s=10,
                               c=colors[species])

    elif species == 'Iris-versicolor':
        green_dot = plt.scatter(sepal_length, sepal_width, s=10,
                                c=colors[species])

    elif species == 'Iris-virginica':
        red_dot = plt.scatter(sepal_length, sepal_width, s=10,
                              c=colors[species])


plt.title("Fisher's Iris Data Set", fontsize=12)
plt.xlabel("sepal length (cm)", fontsize=10)
plt.ylabel("sepal width (cm)", fontsize=10)
plt.legend((blue_dot, green_dot, red_dot), ["Iris-setosa", "Iris-versicolor",
                                            "Iris-virginica"], loc=1)
# plt.axis([3, 9, 1.5, 6])

plt.show()
