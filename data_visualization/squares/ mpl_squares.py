import tkinter
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool , s=10) 
#c='lightgreen' == c=(0, 0.8, 0)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches = 'tight')
# print(plt.style.available)