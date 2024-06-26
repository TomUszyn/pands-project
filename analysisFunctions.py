# analysisFunctions.py contains functions that are used to create summary and analysis results.
# the data from the Iris data set.
# Author: Tomasz Uszynski

import pandas as pd                     # Import the pandas library as pd.
import numpy as np                      # Import the numpy library as np.

df = pd.read_csv("data/iris.csv")       # Load the Iris dataset.

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
        file.write(str(df.shape) + "\n\n")              # Writing the shape of the dataset to the file.
        file.write("Types of each column in the dataset:\n")
        file.write(str(df.dtypes) + "\n\n")             # Writing the data types of each column to the file.
        file.write("The first 5 rows of the dataset:\n")
        file.write(str(df.head()) + "\n\n")             # Writing the first 5 rows of the dataset to the file.
        file.write("The last 5 rows of the dataset:\n")
        file.write(str(df.tail()) + "\n\n")             # Writing the last 5 rows of the dataset to the file.
        file.write("The summary of the dataset:\n")
        file.write(str(df.describe()) + "\n\n")         # Writing the summary statistics of the dataset to the file.
        file.write("The number of each species in the dataset:\n")
        file.write(str(df["species"].value_counts()) + "\n\n")  # Writing the number of each species in the dataset to the file. 
        file.write("The number of missing values in the dataset:\n")
        file.write(str(df.isnull().sum()) + "\n\n")     # Writing the number of missing values in the dataset to the file.
        file.write("The number of unique values in the dataset:\n")
        file.write(str(df.nunique()) + "\n\n")          # Writing the number of unique values in the dataset to the file.
        file.write("The number of duplicate rows in the dataset:\n")
        file.write(str(df.duplicated().sum()) + "\n\n") # Writing the number of duplicate rows in the dataset to the file.
        # Find duplicate rows (all occurrences)
        duplicateMask = df.duplicated(keep=False)      # Finding duplicate rows (all occurrences).
        duplicateEntries = df[duplicateMask]           # Storing duplicate entries in the variable duplicate_entries.
        # Display all duplicate entries
        file.write("All Duplicate Entries:\n")
        file.write(str(duplicateEntries))              # Writing all duplicate entries to the file.
        
# Example usage:
# writeSummaryToFile("summary.txt")                     # Calling the writeSummaryToFile function and passing the name of the file to write the summary to.


# Function analyseCorrelation.
def analyseCorrelation(filename): # Define a function called analyseCorrelation that takes an output file name as an argument.
    """
    Creates a correlation matrix and writes the results with analysis to a file.
    
    Arguments:  
            filename: the name of the output file.
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

# Function findOutliers.
def findOutliers(df, filename):         # Define a function called findOutliers that takes a data frame and a filename as arguments.
    """
    Find outliers in the data set and write them to a file.
    
    Arguments:
        df: the data frame to search for outliers.
        filename: the name of the output file.
    """
    with open(filename, 'a') as f:      # Open the output file in append mode.
        f.write("Outliers by species for the Iris Data set.\n\n")   # Write the title of the analysis.
        for species in df['species'].unique():                      # Iterate over the unique species in the data frame.                     
            speciesDF = df[df['species'] == species]                # Filter the data frame by species.
            numericColumns = speciesDF.select_dtypes(include=['float64', 'int64'])  # Select the numeric columns.
            Q1 = numericColumns.quantile(0.25)                      # Calculate the first quartile.
            Q3 = numericColumns.quantile(0.75)                      # Calculate the third quartile.
            IQR = Q3 - Q1                                           # Calculate the interquartile range.
            outliers = speciesDF[(numericColumns < (Q1 - 1.5 * IQR)) | (numericColumns > (Q3 + 1.5 * IQR))] # Find the outliers.
            outliers = outliers.dropna(how='all')                   # Drop rows with all NaN values.
            if not outliers.empty:                                  # Check if there are outliers.
                f.write(f"Species: {species.capitalize()}\n\n")     # Write the species name.
                for column in outliers.columns:                     # Iterate over the columns with outliers.
                    outlierValues = outliers[column].dropna()       # Get the outlier values.
                    if not outlierValues.empty:                     # Check if there are outlier values.
                        f.write(f"   Feature: {column.capitalize().replace('_', ' ')}\n")   # Write the feature name.
                        f.write(                                            #
                            "   Outlier Values: " + ', '.join([str(value)   # Write the outlier values.
                            for value in outlierValues.values]) + "\n\n")   # 
        f.write("\n")                                                       # Write a new line to separate the species results.

# Call the function with the text filename.
# findOutliers(df, "analysis.txt")                                          # Call the function with the text filename.

# Function analysisOneCall.
def analysisOneCall():                                                      # Define a function called analysisOneCall.
    """
    Calls all the analysis functions in one call.
    """
    analyseCorrelation("analysis.txt")                                      # Call the analyseCorrelation function.
    writeStatsBySpecies("analysis.txt")                                     # Call the writeStatsBySpecies function.
    findOutliers(df, "analysis.txt")                                        # Call the findOutliers function.