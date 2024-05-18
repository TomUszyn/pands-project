# analysis.py
# The program analysis.py must output a summary of each variable to a single text file called analysis.txt. 
# It must also be able to save a histogram of each variable to PNG files. It must also output a scatter plot
# of each pair of variables. The program must also be able to do some other analysis of the data set.
# Author: Tomasz Uszynski

# Importing the necessary libraries.
import pandas as pd                                                                   # Importing the pandas library.
import numpy as np                                                                    # Importing the NumPy library.
import matplotlib.pyplot as plt                                                       # Importing the matplotlib library.
import msvcrt                                                                         # Importing the msvcrt library.
from analysisFunctions import analysisOneCall, writeSummaryToFile                     # Importing the analysisOneCall and writeSummaryToFile functions.
from plottingFunctions import createScatterPlots, saveAllHists, columnsDict, plotDict # Importing functions createScatterPlots, saveAllHists
                                                                                      # and columnsDict, and plotDict dictionaries.

# Reading the data from the file.
df = pd.read_csv("data/iris.csv")                       # Reading the data from the iris.csv file.

# Displaying the menu.
def displayMenu():                                      # Defining the displayMenu function.
    print("\nWelcome to the Iris dataset analysis program. Please select an option from the menu below:\n") #
    print("(s) Create the summary file for the Iris dataset.")                                              #
    print("(h) Create histograms for each variable in the Iris dataset and save them to PNG files.")        # Options for the user to select.
    print("(p) Create scatter plots for each pair of variables in the Iris dataset.")                       #
    print("(a) Perform advanced analysis for the Iris dataset to the txt file.")                            #                
    print("(q) Quit.\n")                                                                                    #
    choice = input("Please select (s/h/p/a/q): ")                                                           # Asking the user to select an option.
    return choice.lower()                               # Returning the user's choice.

# Defining the pause function.
def pause():                                            # Defining the pause function.
    print("Press any key to come back to the menu.\n")  # Printing a message to prompt the user to press any key.
    msvcrt.getch()                                      # Waiting for the user to press any key.
    
# Main program.
choice = displayMenu()                                  # Calling the displayMenu function and storing the user's choice in the variable choice.
while choice != "q":                                    # While the user's choice is not "q", the program will continue to run.
    if choice == "s":                                   # If the user's choice is "s", the program will execute the following code.
        print("\nThe summary file for the Iris data set has been created and saved to summary.txt file.\n") # Printing a message to confirm that the summary is being created.
        writeSummaryToFile("summary.txt")               # Calling the writeSummaryToFile function and passing the name of the file to write the summary to.
        pause()
    elif choice == "h":                                 # If the user's choice is "h", the program will execute the following code.
        print("\nHistograms of each variable from the Iris data set has been saved to PNG files.\n") # Printing a message to confirm that the histograms are being created.
        saveAllHists(df, columnsDict)                   # Calling the saveAllHists function to create histograms for each variable and save them to PNG files.
        pause()

    elif choice == "p":                                 # If the user's choice is "p", the program will execute the following code.
        print("\nScatter plots for each pair of variables from the Iris data set has been created.") # Printing a message to confirm that the scatter plots are being created.
        print("Its open in a new window. Please close the current plot window to continue.\n") # Printing a message to inform the user to close the current plot window.
        createScatterPlots(df, plotDict)                # Calling the createScatterPlots function to create scatter plots for each pair of variables.
        pause()

    elif choice == "a":                                 # If the user's choice is "a", the program will execute the following code.
        print ("\nThe analysis has been saved to analysis.txt.\n") # Printing a message to confirm that the analysis has been saved.
        analysisOneCall()                               # Calling the analysisOneCall function to perform advanced analysis of the Iris dataset.
        pause()
        
    else:                                               # If the user's choice is not "s", "h", "p", "a" or "q", 
                                                        # the program will execute the following code.
        print ("\aInvalid choice. Please select one of the letters representing one of the menu options.") # Printing an error message.
        pause()

    choice = displayMenu()                              # Calling the displayMenu function and storing the user's choice in the variable choice.
    
print ("\nThank you for using the Iris dataset analysis program. Goodbye.\n")   # Printing a goodbye message when the user selects "q" 
                                                                                # to quit the program.