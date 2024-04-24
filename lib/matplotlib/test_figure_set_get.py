print("Testing...")
import sys
sys.path.append('C:\\Users\\Landon\\Documents\\GitHub\\matplotlib-SE-Project\\lib\\matplotlib')
import matplotlib.pyplot as plt

# Inital parameters for figure
figure_size = (8, 6)
figure_facecolor = 'lightblue'
figure_edgecolor = 'red'
figure_linewidth = 2.0
figure_frameon = True

# Create a figure with initial parameters
figure = plt.Figure(figsize = figure_size,
                    facecolor = figure_facecolor, 
                    edgecolor = figure_edgecolor,
                    linewidth = figure_linewidth, 
                    frameon = figure_frameon
                    )
plt.show()

# Print the initial parameters
print("Initial Parameters:")
print("figsize:", figure_size)
print("facecolor:", figure_facecolor)
print("edgecolor:", figure_edgecolor)
print("linewidth:", figure_linewidth)
print("frameon:", figure_frameon)

# Modify parameters using custom set functions (replace these with your custom set functions)
# New parameters for figure
figure.set_figsize(10, 8)
figure.set_facecolor('lightgreen')
figure.set_edgecolor('blue')
figure.set_linewidth(1.5)
figure.set_frameon(False)

# Print the modified parameters
print("\nModified Parameters:")
print("figsize xdfgh:", figure.get_figsize())
print("facecolor:", figure.get_facecolor())
print("edgecolor:", figure.get_edgecolor())
print("linewidth:", figure.get_linewidth())
print("frameon:", figure.get_frameon())

# Show plot
plt.show()
