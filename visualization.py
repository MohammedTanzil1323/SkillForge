import matplotlib.pyplot as plt
import numpy as np

def create_line_chart(data, x_label, y_label, title):
    """Creates a line chart from the given data."""
    x = np.arange(len(data))
    plt.plot(x, data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def create_bar_chart(categories, values, x_label, y_label, title):
    """Creates a bar chart from the given data."""
    plt.bar(categories, values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=45, ha="right") # Rotate x-axis labels for better readability if needed.
    plt.tight_layout() # Adjusts plot layout to prevent labels from overlapping
    plt.show()



# Example usage:
data = [10, 15, 12, 18, 22]
create_line_chart(data, "Day", "Value", "Daily Values")

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 18, 32, 20, 28]
create_bar_chart(categories, values, "Category", "Count", "Category Counts")

