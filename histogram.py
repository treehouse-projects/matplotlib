import csv
import matplotlib.pyplot as plt

input_file = 'iris_data_set/iris.csv'
plt.figure(figsize=(10.5, 5.5))
plt.style.use('classic')

with open(input_file, 'r') as iris_data:
    irises = list(csv.reader(iris_data))

virginica_petal_length = []
num_bins = 10

for petal in range(0, len(irises)-1):
    if irises[petal][4] == 'Iris-virginica':
        virginica_petal_length.append(float(irises[petal][2]))

plt.hist(virginica_petal_length, num_bins, facecolor='red',
         alpha=0.75)

plt.title("Iris-virginia Petal Length", fontsize=12)
plt.xlabel("Petal Length (cm)", fontsize=10)
plt.ylabel("Probability", fontsize=10)

plt.show()
