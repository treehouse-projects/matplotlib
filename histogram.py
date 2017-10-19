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

sepal_length = []
sepal_width = []
species_array = []
colors = ["blue", "red", "green"]
num_bins = 10
for sepal in range(0, len(iris_array)-1):

    if iris_array[sepal][4] not in species_array:
        species_array.append(iris_array[sepal][4])

    for species in species_array:

        sepal_length.append(float(iris_array[sepal][0]))
        sepal_width.append(float(iris_array[sepal][1]))

        plt.hist(sepal_length, num_bins, facecolor="blue", alpha=0.75)


        sepal_length.append(float(iris_array[sepal][0]))
        sepal_width.append(float(iris_array[sepal][1]))

        plt.hist(sepal_length, num_bins, facecolor="green", alpha=0.75)

    elif species == 'Iris-versicolor':
        green_dot = plt.scatter(sepal_length, sepal_width, s=10, c="#3CB878")

    elif species == 'Iris-virginica':
        red_dot = plt.scatter(sepal_length, sepal_width, s=10, c="red")

#
# plt.title("Fisher's Iris Data Set, Iris-setosa Sepal Length Distribution",
#           fontsize=12)
# plt.xlabel("sepal length (cm)", fontsize=10)
# plt.ylabel("Probability", fontsize=10)
# # plt.legend((blue_dot, green_dot, red_dot), ["Iris-setosa", "Iris-versicolor",
# #                                             "Iris-virginica"], loc=1)
# # plt.axis([3, 9, 1.5, 6])
#
plt.show()
