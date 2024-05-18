# plottingFunctions.py contains the following functions which create scatter plots and histograms of the data set.
# Author: Tomasz Uszynski

import matplotlib.pyplot as plt                         # Importing the matplotlib library.
import pandas as pd                                     # Importing the pandas library.
import numpy as np                                      # Importing the NumPy library.

df = pd.read_csv("data/iris.csv")                       # Reading the data from the iris.csv file.

def scatter(pd, x, y, FigureName):                      # Defining the scatter function.
    """
    Creates individual scatter plots for each pair of features and colors each species on the plot.

    Arguments:
        pd (pandas.DataFrame): The DataFrame containing the data.
        x (str): Name of the x-axis feature.
        y (str): Name of the y-axis feature.
        FigureName (str): Name of the figure.
    """
    
    speciesMapping = {                          #
        'setosa': 'blue',                        # Mapping the species to colors.
        'versicolor': 'green',                   # 
        'virginica': 'orange'                    #
    }

    plt.figure(figsize = (8, 6), num=FigureName)                    # Creating a figure with a specified size.
    for species in speciesMapping:                                 # Looping through the species.
        subsetPd = pd[pd['species'] == species]                    # Subsetting the data for each species.
        plt.scatter(subsetPd[x], subsetPd[y], label=species)      # Creating a scatter plot for each species.
            
    plt.title(f"{x.capitalize().replace('_', ' ')} vs. {y.capitalize().replace('_', ' ')+'.'}",
              fontsize = 15, fontweight = "bold")                   # Adding a title to the plot.
    plt.xlabel(x.capitalize().replace('_', ' ') + ' (cm).',
                fontsize = 12, fontweight = "bold")                 # Adding a label to the x-axis.
    plt.ylabel(y.capitalize().replace('_', ' ') + ' (cm).', 
               fontsize= 12 , fontweight = "bold")                  # Adding a label to the y-axis.
    plt.legend()                                                    # Adding a legend to the plot.
    plt.show()                                                      # Displaying the plot.
    plt.close()                                                     # Closing the plot.


# Example usage:
# Assuming DataFrame is named 'pd' with columns 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', and 'species':
# scatter(pd, 'sepal_length', 'sepal_width', 'Scatter Plot Sepal Length vs Sepal Width')


# Creating a function to save a histogram of each variable to a PNG file.
def saveHist(pd, variableName, numBins=10):       # Defining the saveHist function.
    """
    Creates a histogram for the specified variable and saves it as a PNG file.

    Arguments:
        data (pandas.Series) are data for the variable.
        variable_name (str) is a name of the variable.
        num_bins (int, optional)is a number of bins for the histogram. Default is set to 10.
    """
    plt.figure(figsize=(10, 8))                                          # Creating a figure with a specified size.
    
    # Counting of bin width. 
    binWidth = (pd.max() - pd.min()) / (numBins)                       # Calculating the bin width.
    plt.xticks(np.arange(pd.min(), pd.max() + binWidth, binWidth))     # Setting the x-axis ticks.
    plt.hist(pd, bins=numBins, color = "blue", edgecolor = "black")     # Creating a histogram.
    plt.title(f"Histogram of {variableName}.", fontsize = 15, fontweight = "bold") # Adding a title to the plot.
    plt.xlabel(f"{variableName} (cm).", fontsize = 12, fontweight = "bold") # Adding a label to the x-axis.
    plt.ylabel("Frequency.", fontsize = 12, fontweight = "bold")         # Adding a label to the y-axis.
    plt.savefig(f"{variableName.lower().replace(' ', '_')}_hist.png")   # Saving the plot as a PNG file.   
    plt.close()                                                          # Closing the plot.
    
# Example usage:
# Assuming 'pd' is pandas DataFrame and 'sepal_length' is the variable wanted to be plotted.
# saveHist(pd["sepal_length"], "Sepal Length")