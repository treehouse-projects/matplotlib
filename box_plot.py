import csv
import matplotlib.pyplot as plt
from itertools import groupby

input_file = 'iris_data_set/iris.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')
fig = plt.figure()

with open(input_file, 'r') as iris_data:
    irises = list(csv.reader(iris_data))

irises.pop()
petal_lengths=[]
for species, group in groupby(irises, lambda i: i[4]):
    # Group is a generator, so you can only go over it once
    # categorized_irises = list(group)
    # print(str(categorized_irises))
    petal_lengths.append([float(petal[2]) for petal in group])

plt.boxplot(petal_lengths)

plt.axis([0, 4, 0, 10])

plt.xticks([1, 2, 3], ['Setosa', 'Versicolor', 'Virginica'])

plt.title("Fisher's Iris Data Set, Petal Length", fontsize=12, loc="left")
plt.xlabel("Iris Variety", fontsize=10)
plt.ylabel("Petal length (cm)", fontsize=10)

fig.savefig('petal_length_boxplot.png')
plt.show()
