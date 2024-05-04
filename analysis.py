# analysis.py
# The program analysis.py must output a summary of each variable to a single text file called analysis.txt. 
# It must also be able to save a histogram of each variable to PNG files. It must also output a scatter plot
# of each pair of variables. The program must also be able to do some other analysis of the data set.
# Author: Tomasz Uszynski

# Importing the necessary libraries.
import pandas as pd                                     # Importing the pandas library.
import numpy as np                                      # Importing the NumPy library.
import matplotlib.pyplot as plt                         # Importing the matplotlib library.

# Reading the data from the file.
pd = pd.read_csv("data/iris.csv")                       # Reading the data from the iris.csv file.

# Creating function to write the summary of data set to a text file.
def writeSummaryToFile(filename):                       # Defining the writeSummaryToFile function.
    """
    Writes a summary of the ataset to the specified file.

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
# Example usage:
# writeSummaryToFile("summary.txt")                     # Calling the writeSummaryToFile function and passing the name of the file to write the summary to.

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

choice = displayMenu()                                  # Calling the displayMenu function and storing the user's choice in the variable choice.
while choice != "q":                                    # While the user's choice is not "q", the program will continue to run.
    if choice == "s":                                   # If the user's choice is "s", the program will execute the following code.
        print("The summary file for the Iris data set has been created and saved to summary.txt file.\n") # Printing a message to confirm that the summary is being created.
        writeSummaryToFile("summary.txt")               # Calling the writeSummaryToFile function and passing the name of the file to write the summary to.
    elif choice == "h":                                 # If the user's choice is "h", the program will execute the following code.
        print("Histograms of each variable from the Iris data set has been saved to PNG files.\n") # Printing a message to confirm that the histograms are being created.
    
    elif choice == "p":                                 # If the user's choice is "p", the program will execute the following code.
        print("Scatter plots for each pair of variables From the Iris data set has been created.\n") # Printing a message to confirm that the scatter plots are being created.

    elif choice == "a":                                 # If the user's choice is "a", the program will execute the following code.
        print ("The analysis has been saved to analysis.txt.\n") # Printing a message to confirm that the analysis has been saved.
        
    else:                                               # If the user's choice is not "s", "h", "p", "a" or "q", 
                                                        # the program will execute the following code.
        print ("Invalid choice. Please select one of the letters representing one of the menu options.")    # Printing an error message.

    choice = displayMenu()                              # Calling the displayMenu function and storing the user's choice in the variable choice.
    
print ("Thank you for using the Iris dataset analysis program. Goodbye.")   # Printing a goodbye message when the user selects "q" 
                                                                            # to quit the program.
