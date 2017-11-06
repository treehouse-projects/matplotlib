import csv
import matplotlib.pyplot as plt

input_file = 'iris.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')
fig = plt.figure()

with open(input_file, 'r') as iris_data:
    irises = list(csv.reader(iris_data))

setosa = []
versicolor = []
virginica = []

for petal in range(0, len(irises)-1):
    if irises[petal][4] == 'Iris-setosa':
        setosa.append(float(irises[petal][2]))
    elif irises[petal][4] == 'Iris-versicolor':
        versicolor.append(float(irises[petal][2]))
    elif irises[petal][4] == 'Iris-virginica':
        virginica.append(float(irises[petal][2]))

petal_lengths = [setosa, versicolor, virginica]

plt.boxplot(petal_lengths)

plt.axis([0, 4, 0, 10])

plt.xticks([1, 2, 3], ['Setosa', 'Versicolor', 'Virginica'])

plt.title("Fisher's Iris Data Set, Petal Length", fontsize=12, loc="left")
plt.xlabel("Iris Variety", fontsize=10)
plt.ylabel("Petal length (cm)", fontsize=10)

fig.savefig('boxplot.png')
plt.show()
