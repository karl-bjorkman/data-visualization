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