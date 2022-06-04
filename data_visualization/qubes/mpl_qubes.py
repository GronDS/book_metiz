'''15.1. Кубы: число, возведенное в третью степень, называется «кубом». 
Нанесите на диаграмму первые пять кубов, а затем первые 5000 кубов.
15.2. Цветные кубы: примените цветовую карту к диаграмме с кубами'''

import tkinter
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('TkAgg')

input_values = list(range(1,5001)) #list(range(1,6))
qubes = [x**3 for x in input_values]

plt.style.use('seaborn-whitegrid')

fig, ax = plt.subplots()
ax.plot(input_values, qubes, linewidth=1)
ax.scatter(input_values, qubes, c=qubes, cmap=plt.cm.cool, s=2)



ax.set_title('Qube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Qube of Value', fontsize=14)

ax.axis([0, 5000, 0, (5000**3) ])
plt.show()
# plt.savefig('qubes_plot.png', bbox_inches = 'tight')