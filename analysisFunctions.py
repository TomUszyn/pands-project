# analysisFunctions.py contains functions that are used to analyse
# the data from the Iris data set.
# Author: Tomasz Uszynski

import pandas as pd                     # Import the pandas library as pd.
import numpy as np                      # Import the numpy library as np.

df = pd.read_csv("data/iris.csv")       # Load the Iris dataset.

# Function analyseCorrelation.
def analyseCorrelation(filename): # Define a function called analyseCorrelation that takes an output file name as an argument.
    """
    Creates a correlation matrix and writes the results with analysis to a file.
    
    Arguments:  
            outputFileName: the name of the output file.
    """
    numericColumns =df.drop(columns=["species"])    # Exclude the "species" column.
    correlationMatrix = numericColumns.corr()       # Calculate the correlation matrix.
   
    correlationLevels = {               #
        'a very high': (0.9, 1),        #
        'a high': (0.7, 0.9),           # Define correlation levels.
        'a moderate': (0.5, 0.7),       #
        'a low': (0.3, 0.5),            #
        'a little if any': (0.0, 0.3)   #
    }                                   #

    # Analyse correlations and write results to a file.
    with open(filename, "w") as file:                        # Open the output file in write mode.
        file.write("Analysis of the Iris dataset.\n\n")            # Write the title of the analysis.
        file.write("Correlation between each set of values.\n\n")  # Write the subtitle of the analysis.
        for col in correlationMatrix.columns:                      # Iterate over the columns of the correlation matrix.
            for row in correlationMatrix.index:                    # Iterate over the rows of the correlation matrix.
                if row < col:                                      # Avoid duplicate pairs.
                    value = correlationMatrix.loc[row, col]        # Get the correlation value.
                    for level, (minVal, maxVal) in correlationLevels.items():   # Iterate over the correlation levels.
                        if minVal <= abs(value) <= maxVal:                      # Check if the correlation value is within the current level.
                            correlationType = "positive" if value > 0 else "negative"   # Define the correlation type.
                            file.write(                                                   #
                                f"The Correlation Coefficient value between "             #
                                f"{row.capitalize().replace('_', ' ')} and "              # Write the correlation result.
                                f"{col.capitalize().replace('_', ' ')} is {value:.2f},\n" #    
                                f"and there is {level} {correlationType} correlation.\n"  #    
                                      )                                                   #

        file.write("\n\n")              # Write two new lines to separate the correlation results.

# Call the function with the text filename.
# analyseCorrelation("analysis.txt").

# Function writeStatsBySpecies.
def writeStatsBySpecies(filename):      # Define a function called writeStatsBySpecies 
                                        # that takes a filename as an argument.
    """
    Creates a table with the statistics of the Iris dataset by species and writes the results to a file.

    Arguments:  
            filename: the name of the output file.
    """
    statsBySpecies = df.groupby('species').agg(['mean', 'median', 'std'])   # Calculate statistics by species.

    with open(filename, 'a') as file:   # Save the formatted table as a text file.
        file.write(                                                     # 
            f"The mean, the median and the standadard deviation by "    # Write the title of the analysis.
            f"species in the Iris dataset by species.\n\n"              #
            )                                                           #
        for species, row in statsBySpecies.iterrows():                  # Iterate over the rows of the statsBySpecies DataFrame.
            file.write(f"{species.capitalize()}:\n")                    # Write the species name.
            for col in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:  # Iterate over the columns.
                file.write(                                     #
                    f"  {col.capitalize().replace('_', ' ')}:"  #
                    f" mean={row[(col, 'mean')]:.2f}, "         #
                    f" median={row[(col, 'median')]:.2f}, "     # Write the statistics for each column.
                    f" std={row[(col, 'std')]:.2f}\n"           #
                    )                                           #
            
            file.write("\n")                                    # Write a new line to separate the species.

# Usage
# writeStatsBySpecies('analysis.txt')
       
