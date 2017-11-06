import csv
import matplotlib.pyplot as plt
from itertools import groupby

input_file = 'iris_data_set/iris.csv'
plt.figure(figsize=(10.5, 5.5))


with open(input_file, 'r') as iris_data:
    irises = list(csv.reader(iris_data))

colors = {"Iris-setosa": "#2B5B84", "Iris-versicolor": "#3CB878",
          "Iris-virginica": "purple"}
# Extra junk in the trunk
irises.pop()
for species, group in groupby(irises, lambda i: i[4]):
    # Group is a generator, so you can only go over it once
    categorized_irises = list(group)
    sepal_lengths = [iris[0] for iris in categorized_irises]
    sepal_widths = [iris[1] for iris in categorized_irises]
    plt.scatter(sepal_lengths, sepal_widths, s=10,
                c=colors[species], label=species)

plt.title("Fisher's Iris Data Set", fontsize=12)
plt.xlabel("sepal length (cm)", fontsize=10)
plt.ylabel("sepal width (cm)", fontsize=10)
plt.legend(loc='upper left')
plt.axis([3, 9, 1.5, 6])

plt.show()