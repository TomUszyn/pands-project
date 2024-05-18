# analysis.py
# The program analysis.py must output a summary of each variable to a single text file called analysis.txt. 
# It must also be able to save a histogram of each variable to PNG files. It must also output a scatter plot
# of each pair of variables. The program must also be able to do some other analysis of the data set. 
# In this case it will be the correlation between the variables, finding the mean, median and standard 
# deviation of each variable for each species and finding the outliers for each variables for each species. 
# The program saves the output this to a text file called analysis.txt.
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
df = pd.read_csv("data/iris.csv")                     # Reading the data from the iris.csv file.

# Displaying the menu.
def displayMenu():                                    # Defining the displayMenu function.
    print(                                            #
        "\nWelcome to the Iris dataset analysis "     # Printing the welcome message and the options
        "program. Please select an option from the "  # for the user to select.
        "menu below:\n"                               #
        )                                             #
    
    print(                                            # 
        "(s) Create the summary file for the Iris "   #
        "dataset."                                    #
        )                                             #
    print(                                            #                                            
        "(h) Create histograms for each variable in " #
        "the Iris dataset and save them to "          #
        "PNG files."                                  #
        )                                             #
    print(                                            #
        "(p) Create scatter plots for each pair of "  #
        "variables in the Iris dataset."              # Options for the user to select.
        )                                             # 
    print(                                            #
        "(a) Perform advanced analysis for the Iris " #
        "dataset to the txt file."                    #
        )                                             #
    print("(q) Quit.\n")                              #
    
    choice = input("Please select (s/h/p/a/q): ")     # Asking the user to select an option.
    return choice.lower()                             # Returning the user's choice.

# Defining the pause function.
def pause():                                          # Defining the pause function.
    print("Press any key to come back to the menu.\n")# Printing a message to prompt the user to press any key.
    msvcrt.getch()                                    # Waiting for the user to press any key.
    
# Main program.
choice = displayMenu()       # Calling the displayMenu function and storing the user's choice in the variable choice.
while choice != "q":         # While the user's choice is not "q", the program will continue to run.
    if choice == "s":        # If the user's choice is "s", the program will execute the following code.
        
        print(                                        #
            "\nThe summary has been saved to a "      #
            "summary.txt file in the main folder of " # Printing a message to inform the user where the file is saved.
            "the program.\n"                          #
            )                                         #
        
        writeSummaryToFile("summary.txt")             # Calling the writeSummaryToFile function.
        pause()                                       # Calling the pause function. 
                
    elif choice == "h":                               # If the user's choice is "h", the program will execute the following code.
        
        print(                                        #
            "\nHistograms of each variable from the " #
            "Iris data set has been saved to PNG "    # Printing a message to confirm that the histograms are being created. 
            "files in the main folder of the "        #
            "program.\n"                              #
            )                                         #
        
        saveAllHists(df, columnsDict)                 # Calling the saveAllHists function with arguments.
        pause()                                       # Calling the pause function.

    elif choice == "p":                               # If the user's choice is "p", the program will execute the following code.
        
        print(                                        #  
            "\nScatter plots for each pair of "       # Printing a message to confirm that the scatter 
            "variables from the Iris data set "       # plots are being created.
            "has been created."                       #                       
            )                                         #
        
        print(                                        #
            "Its open in a new window. Please close " # Printing a message for the user.  
            "the current plot window to see next "    #
            "plot. \nMake must close all plots "      #     
            "windows to come back to the menu.\n"     #
            )                                         #
        
        createScatterPlots(df, plotDict)              # Calling the createScatterPlots function with arguments.
        pause()                                       # Calling the pause function.

    elif choice == "a":                               # If the user's choice is "a", the program will execute the following code.
        
        print(                                        #
            "\nThe analysis has been saved to "       # Printing a message to confirm that the analysis has been saved.
            "analysis.txt in the main folder "        #
            "of the program.\n"                       #
            )                                         #
        
        analysisOneCall()                             # Calling the analysisOneCall function.
        pause()                                       # Calling the pause function.
        
    else:                                             # If the user's choice is not "s", "h", "p", "a" or "q", 
                                                      # the program will execute the following code.
                                                      
        print(                                        #
            "\aInvalid choice. Please select one of " #
            "the letters representing one of the "    # Printing an error message.
            "menu options."                           #
            )                                         #
        
        pause()                                       # Calling the pause function.
    choice = displayMenu()                            # Calling the displayMenu function and storing the user's choice 
                                                      # in the variable choice.
    
print(                                                #   
    "\nThank you for using the Iris dataset "         # Printing a goodbye message when the user selects "q" to quit the program.
    "analysis program. Goodbye.\n"                    #
    )                                                 #