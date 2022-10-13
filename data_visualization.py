from matplotlib import pyplot as plt

x = [0, 2, 3, 4, 5, 6]
y = [0, 1, 4, 16, 25, 36]

# Plotting green line with circle markers at each x-axis tick
plt.plot(x, y, color = 'green', marker = 'o')
plt.show()
plt.clf()

# Zoom in to x or y axes
plt.axis([0, 15, 25, 75]) # [xmin, xmax, ymin, ymax]

# Labeling Axes
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Plot Title')

# Subplots
plt.subplot(subplot_rows, subplot_columns, subplot_index) # CONFUSING! GO BACK AND REVIEW!
plt.plot(var1, var2)
plt.show()

plt.subplots_adjust(left, right, bottom, top, wspace, hspace)

plt.plot([0, 1, 2, 3], [1, 4, 9, 16], label = "line name") # Instead of 'legend'
plt.legend(['label 1', 'label 2']) # Can also make list of legend labels and feed it to .legend()

# Modify Ticks
ax = plt.subplot() # 'ax' is axes object
ax.set_xticks([1, 2, 4]) # Shows only these ticks
ax.set_yticks([1, 50, 100])

# Use special labels
ax.set_xticklabels()
ax.set_yticks([0.1, 0.5, 1.0])
ax.set_yticklabels(['10%', '50%', '100%'])

# Figures
plt.figure(figsize = (4, 10))

# Clear all existing plots before creating a new one
plt.close('all')

# Saving a plot for presentation or website, say
plt.savefig()
plt.savefig('example.pdf')
plt.savefig('example2.png')
plt.savefig('example3.svg')


# Different Plot Types

# Simple Bar Chart
plt.bar(xlist, ylist)

ax = plt.subplot()
ax.set_xticks()
ax.set_xticklabels(str_list, rotation = 30) # If labels are long, this puts them at an angle to make them fit

# Side-by-side Bar Charts

n = 2  # This is our second dataset (out of 2)
t = 2  # Number of datasets
d = 7  # Number of sets of bars
w = 0.8  # Width of each bar
x_values2 = [t*element + w*n for element in range(d)] # list comprehension

# Example Side-by-side Bar Charts

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

n = 1  # This is our first dataset (out of 2)
t = 2  # Number of datasets
d = 6  # Number of sets of bars
w = 0.8  # Width of each bar
store1_x = [t*element + w*n for element in range(d)]
plt.bar(store1_x, sales1)

n = 2  # This is our second dataset (out of 2)
t = 2  # Number of datasets
d = 6  # Number of sets of bars
w = 0.8  # Width of each bar
store2_x = [t*element + w*n for element in range(d)]
plt.bar(store2_x, sales2)

plt.show()

# Stacked Bars

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1) # 'bottom' is crucial parameter, here
plt.legend(['Location 1', 'Location 2'])

plt.show()

# Error Bars - YERRRRRR!

values = [10, 13, 11, 15, 20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()

values = [10, 13, 11, 15, 20]
yerr = [1, 3, 0.5, 2, 4]
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()

# Fill Between

x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27] # calculated quickly below
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31] # calculated quickly below

# this is the shaded error
plt.fill_between(x_values, y_lower, y_upper, alpha=0.2)
plt.plot(x_values, y_values)  # this is the line itself
plt.show()

y_lower = [i - 2 for i in y_values] # list comprehension
y_upper = [i + 2 for i in y_values] # list comprehension

# Pie Charts

budget_data = [500, 1000, 750, 300, 100]

plt.pie(budget_data)
plt.axis('equal') # This makes pie chart appear as perfect circle, not awkwardly stretched
plt.show()

budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']

plt.pie(budget_data)
plt.legend(budget_categories) # Labeling as a legend/key

plt.pie(budget_data, labels=budget_categories) # OR you can do it this way, around the chart

plt.pie(budget_data,
        labels=budget_categories,
        autopct='%0.1f%%') # Adds percentages, see documentation

# Histograms

plt.hist(dataset)
plt.show()

plt.hist(dataset, range=(66,69), bins=40)

# Multiple Histograms
plt.hist(a, range=(55, 75), bins=20, alpha=0.5) # 'alpha' sets transparency
plt.hist(b, range=(55, 75), bins=20, alpha=0.5)

plt.hist(a, range=(55, 75), bins=20, histtype='step') # 'histtype = 'step'' to draw just outline
plt.hist(b, range=(55, 75), bins=20, histtype='step')

# Histograms of different sizes - makes them proportional
a = normal(loc=64, scale=2, size=10000)
b = normal(loc=70, scale=2, size=100000)

plt.hist(a, range=(55, 75), bins=20, alpha=0.5, normed=True) # 'normed = True' is crucial syntax, here
plt.hist(b, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.show()