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