# analysis.py
# The program analysis.py must output a summary of each variable to a single text file called analysis.txt. 
# It must also be able to save a histogram of each variable to PNG files. It must also output a scatter plot
# of each pair of variables. The program must also be able to do some other analysis of the data set.
# Author: Tomasz Uszynski

# Importing the necessary libraries.
import pandas as pd                                     # Importing the pandas library.
import numpy as np                                      # Importing the NumPy library.
import matplotlib.pyplot as plt                         # Importing the matplotlib library.
from analysisFunctions import analyseCorrelation, writeStatsBySpecies   # Importing the analyseCorrelation function 
                                                        # and writeStatsBySpecies from the analysisFunctions.py file.

# Reading the data from the file.
pd = pd.read_csv("data/iris.csv")                       # Reading the data from the iris.csv file.

# Creating function to write the summary of data set to a text file.
def writeSummaryToFile(filename):                       # Defining the writeSummaryToFile function.
    """
    Writes a summary of the data set to the specified file.

    Args:
        filename (str): The name of the file to write the summary to.
    """
    with open(filename, "w") as file:                   # Opening the file in write mode.
        file.write("Summary of the Iris dataset\n\n")
        file.write("The Iris dataset contains 150 rows and 5 columns.\n")
        file.write(str(pd.shape) + "\n\n")              # Writing the shape of the dataset to the file.
        file.write("Types of each column in the dataset:\n")
        file.write(str(pd.dtypes) + "\n\n")             # Writing the data types of each column to the file.
        file.write("The first 5 rows of the dataset:\n")
        file.write(str(pd.head()) + "\n\n")             # Writing the first 5 rows of the dataset to the file.
        file.write("The last 5 rows of the dataset:\n")
        file.write(str(pd.tail()) + "\n\n")             # Writing the last 5 rows of the dataset to the file.
        file.write("The summary of the dataset:\n")
        file.write(str(pd.describe()) + "\n\n")         # Writing the summary statistics of the dataset to the file.
        file.write("The number of each species in the dataset:\n")
        file.write(str(pd["species"].value_counts()) + "\n\n")  # Writing the number of each species in the dataset to the file. 
        file.write("The number of missing values in the dataset:\n")
        file.write(str(pd.isnull().sum()) + "\n\n")     # Writing the number of missing values in the dataset to the file.
        file.write("The number of unique values in the dataset:\n")
        file.write(str(pd.nunique()) + "\n\n")          # Writing the number of unique values in the dataset to the file.
        file.write("The number of duplicate rows in the dataset:\n")
        file.write(str(pd.duplicated().sum()) + "\n\n") # Writing the number of duplicate rows in the dataset to the file.
        # Find duplicate rows (all occurrences)
        duplicate_mask = pd.duplicated(keep=False)      # Finding duplicate rows (all occurrences).
        duplicate_entries = pd[duplicate_mask]          # Storing duplicate entries in the variable duplicate_entries.
        # Display all duplicate entries
        file.write("All Duplicate Entries:\n")
        file.write(str(duplicate_entries))              # Writing all duplicate entries to the file.
        
# Example usage:
# writeSummaryToFile("summary.txt")                     # Calling the writeSummaryToFile function and passing the name of the file to write the summary to.

# Creating a function to save a histogram of each variable to a PNG file.
def saveHist(pd, variable_name, num_bins=10):       # Defining the saveHist function.
    """
    Creates a histogram for the specified variable and saves it as a PNG file.

    Arguments:
        data (pandas.Series) are data for the variable.
        variable_name (str) is a name of the variable.
        num_bins (int, optional)is a number of bins for the histogram. Default is set to 10.
    """
    plt.figure(figsize=(10, 8))                                          # Creating a figure with a specified size.
    
    # Counting of bin width. 
    bin_width = (pd.max() - pd.min()) / (num_bins)                       # Calculating the bin width.
    plt.xticks(np.arange(pd.min(), pd.max() + bin_width, bin_width))     # Setting the x-axis ticks.
    plt.hist(pd, bins=num_bins, color = "blue", edgecolor = "black")     # Creating a histogram.
    plt.title(f"Histogram of {variable_name}.", fontsize = 15, fontweight = "bold") # Adding a title to the plot.
    plt.xlabel(f"{variable_name} (cm).", fontsize = 12, fontweight = "bold") # Adding a label to the x-axis.
    plt.ylabel("Frequency.", fontsize = 12, fontweight = "bold")         # Adding a label to the y-axis.
    plt.savefig(f"{variable_name.lower().replace(' ', '_')}_hist.png")   # Saving the plot as a PNG file.   
    plt.close()                                                          # Closing the plot.
    
# Example usage:
# Assuming 'pd' is pandas DataFrame and 'sepal_length' is the variable wanted to be plotted.
# saveHist(pd["sepal_length"], "Sepal Length")

def scatter(pd, x, y, FigureName):                      # Defining the scatter function.
    """
    Creates individual scatter plots for each pair of features and colors each species on the plot.

    Arguments:
        pd (pandas.DataFrame): The DataFrame containing the data.
        x (str): Name of the x-axis feature.
        y (str): Name of the y-axis feature.
        FigureName (str): Name of the figure.
    """
    species_mapping = {                          #
        'setosa': 'blue',                        # Mapping the species to colors.
        'versicolor': 'green',                   # 
        'virginica': 'orange'                    #
    }

    plt.figure(figsize = (8, 6), num=FigureName)                    # Creating a figure with a specified size.
    for species in species_mapping:                                 # Looping through the species.
        subset_pd = pd[pd['species'] == species]                    # Subsetting the data for each species.
        plt.scatter(subset_pd[x], subset_pd[y], label=species)      # Creating a scatter plot for each species.
            
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
# scatter(pd, "sepal_length", "sepal_width", "Scatter Plot Sepal Length vs Sepal Width.")

# Displaying the menu.
def displayMenu():                                      # Defining the displayMenu function.
    print("Welcome to the Iris dataset analysis program. Please select an option from the menu below:\n")   #
    print("(s) Create the summary file for the Iris dataset.")                                              #
    print("(h) Create histograms for each variable in the Iris dataset and save it to PNG files.")          # Options for the user to select.
    print("(p) Create scatter and plots for each pair of variables in the Iris dataset.")                   #
    print("(a) Make the analysis of each variables from dataset and save it into txt file.")                #                
    print("(q) Quit.\n")                                                                                    #
    choice = input("Please select (s/h/p/a/q): ")                                                           # Asking the user to select an option.
    return choice                                       # Returning the user's choice.


# Main program.
choice = displayMenu()                                  # Calling the displayMenu function and storing the user's choice in the variable choice.
while choice != "q":                                    # While the user's choice is not "q", the program will continue to run.
    if choice == "s":                                   # If the user's choice is "s", the program will execute the following code.
        print("The summary file for the Iris data set has been created and saved to summary.txt file.\n") # Printing a message to confirm that the summary is being created.
        writeSummaryToFile("summary.txt")               # Calling the writeSummaryToFile function and passing the name of the file to write the summary to.
    elif choice == "h":                                 # If the user's choice is "h", the program will execute the following code.
        print("Histograms of each variable from the Iris data set has been saved to PNG files.\n") # Printing a message to confirm that the histograms are being created.
        # Creating histograms of each variable and saving each plot to individual PNG files.
        saveHist(pd["sepal_length"], "Sepal Length")    #
        saveHist(pd["sepal_width"], "Sepal Width")      # Creating  the histograms for each varialbles.
        saveHist(pd["petal_length"], "Petal Length")    #
        saveHist(pd["petal_width"], "Petal Width")      #

    elif choice == "p":                                 # If the user's choice is "p", the program will execute the following code.
        print("Scatter plots for each pair of variables from the Iris data set has been created.\n") # Printing a message to confirm that the scatter plots are being created.
        # Creating scatter plots for each pair of variables from the Iris data set.
        scatter(pd, "sepal_length", "sepal_width", "Scatter Plot Sepal Length vs Sepal Width.")      #  
        scatter(pd, "sepal_length", "petal_length", "Scatter Plot Sepal Length vs Petal Length.")    #    
        scatter(pd, "sepal_length", "petal_width", "Scatter Plot Sepal Length vs Petal Width.")      # Creating the scatter plots for each
        scatter(pd, "sepal_width", "petal_length", "Scatter Plot Sepal Width vs Petal Length.")      #  pair of variables.
        scatter(pd, "sepal_width", "petal_width", "Scatter Plot Sepal Width vs Petal Width.")        #
        scatter(pd, "petal_length", "petal_width", "Scatter Plot Petal Length vs Petal Width.")      #

    elif choice == "a":                                 # If the user's choice is "a", the program will execute the following code.
        print ("The analysis has been saved to analysis.txt.\n") # Printing a message to confirm that the analysis has been saved.
        analyseCorrelation("analysis.txt")              # Calling the analyseCorrelation function and passing the name of the file to write the analysis to.
        writeStatsBySpecies('analysis.txt')             # Calling the writeStatsBySpecies function and passing the name of the file to write the analysis to.
    else:                                               # If the user's choice is not "s", "h", "p", "a" or "q", 
                                                        # the program will execute the following code.
        print ("Invalid choice. Please select one of the letters representing one of the menu options.")    # Printing an error message.

    choice = displayMenu()                              # Calling the displayMenu function and storing the user's choice in the variable choice.
    
print ("Thank you for using the Iris dataset analysis program. Goodbye.")   # Printing a goodbye message when the user selects "q" 
                                                                            # to quit the program.
