import csv
import matplotlib.pyplot as plt
import numpy as np

# Function to read CSV file
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

# Function to plot 2D array
def plot_2d_array(data):
    # Convert data to numpy array
    data = np.array(data, dtype=float)

    # Plot the data
    plt.imshow(data, cmap='viridis')
    plt.show()

# Example usage
filename = 'dataoutpy.csv'  # Specify the filename
data = read_csv(filename)  # Call the function to read the CSV file
plot_2d_array(data)  # Call the function to plot the 2D array
