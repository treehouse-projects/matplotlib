import matplotlib.pyplot as plt
import numpy as np
import plotly as py

fig = plt.figure()

# line chart
# plt.plot([1, 2, 3, 4, 5, 6, 7, 8], [10, 15, 17.5, 16, 13, 14, 14, 14],
#          color='green', linestyle='dashdot', label='Green Widget')
# plt.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 7, 9, 15, 20, 21, 20, 19],
#          color='#2B5B84', linestyle='dashed', label='Blue Widget')
# plt.ylabel('Sales Revenue (Thousands $)')
# plt.xlabel('Months on Market')
# plt.legend(loc='lower right')
# plt.title('Widget Revenue')
#
# fig.savefig('line_chart.png')


# bar chart
# apples = ('Golden Delicious', 'Gala', 'Fuji', 'Granny Smith', 'Red Delicious')
# y_pos = np.arange(len(apples))
# sales = [40, 33, 25, 30, 55]
#
# plt.bar(y_pos, sales, align='center', alpha=0.75)
# plt.xticks(y_pos, apples)
# plt.ylabel('Sales in Lbs. (thousands)')
# plt.title('Apple Sales')
#
# fig.savefig('bar_chart.png')

# pie chart
# apples = ('Golden Delicious', 'Gala', 'Fuji', 'Granny Smith', 'Red Delicious',
#           'other')
# sizes = [18, 17, 14, 15, 23, 13]
# colors = ['gold', 'orange', 'lightcoral', 'yellowgreen', 'red', 'blue']
# explode = (0, 0, 0, 0, 0.1, 0)
# # Plot
# plt.pie(sizes, explode=explode, labels=apples, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=120)
# plt.axis('equal')
# plt.title('Apple Sales')
# fig.savefig('pie_chart.png')

# Scatter Plot
# num = 150
# x = np.random.rand(num)
# y = np.random.rand(num)
# colors = np.random.rand(num)
# area = np.pi * (15 * np.random.rand(num))**2
# plt.scatter(x, y, s=area, alpha=0.75, c=colors)
# fig.savefig('scatter_plot.png')

# Scatter Plot with correlation
# fig, ax = plt.subplots()
# num = 1000
# s = 121
# x1 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
# y1 = np.linspace(-5,5,num) + (0.5 - np.random.rand(num))
# x2 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
# y2 = np.linspace(5,-5,num) + (0.5 - np.random.rand(num))
# x3 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
# y3 = (0.5 - np.random.rand(num))
# ax.scatter(x1, y1, color='r', s=2*s, marker='^', alpha=.4)  # Positive
# ax.scatter(x2, y2, color='b', s=s/2, alpha=.4)  # Negative
# ax.scatter(x3, y3, color='g', s=s/3, marker='s', alpha=.4) # None
#
# fig.savefig('combined_correlation.png')

# Histogram
# gaussian_numbers = np.random.randn(10000)
# plt.hist(gaussian_numbers)
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
#
# fig.savefig('motion_sample_images/histogram.png')

# Box Plot
# Fake up the data

# spread =  np.random.rand(50) * 100
# center = np.ones(25) * 50
# flier_high = np.random.rand(10) * 100 + 100
# flier_low = np.random.rand(10)
# data = np.concatenate((spread, center, flier_high, flier_low), 0)
#
# plt.boxplot(data)
# plt.xticks([1], ['My Amazing Car'])
#
# plt.title("City Mileage", fontsize=12, loc="left")
# plt.xlabel("Vehicle Type", fontsize=10)
# plt.ylabel("MPG (City)", fontsize=10)
#
# fig.savefig('motion_sample_images/boxplot.png')

# Heat Map
# Create data
x = np.random.randn(4096)
y = np.random.randn(4096)

# Create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(64, 64))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# Plot heatmap
#here's our data to plot, all normal Python lists
x = [1, 2, 3, 4, 5]
y = [0.1, 0.2, 0.3, 0.4, 0.5]

intensity = [
    [5, 10, 15, 20, 25],
    [30, 35, 40, 45, 50],
    [55, 60, 65, 70, 75],
    [80, 85, 90, 95, 100],
    [105, 110, 115, 120, 125]
]

#setup the 2D grid with Numpy
x, y = np.meshgrid(x, y)

#convert intensity (list of lists) to a numpy array for plotting
intensity = np.array(intensity)

#now just plug the data into pcolormesh, it's that easy!
plt.pcolormesh(x, y, intensity)
plt.colorbar() #need a colorbar to show the intensity scale

fig.savefig('motion_sample_images/heatmap.png')
plt.show()

