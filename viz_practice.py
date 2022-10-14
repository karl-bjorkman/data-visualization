from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

drinks = ['coffee', 'tea', 'iced tea', 'smoothie', 'milkshake']
costs = [3, 3, 4, 6, 7]
y_err = 0.5

plt.bar(range(len(drinks)), costs, yerr = y_err, capsize = 10)

ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks, rotation = 20)

plt.xlabel('Drinks')
plt.ylabel('Cost ($)')
plt.show()