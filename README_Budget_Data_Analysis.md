Budget Data Analysis
Project Overview

The Budget Data Analysis project is a Python script designed to automate the financial records analysis of a company. By analyzing financial data from a CSV file, this script computes various financial metrics, including the total number of months included in the dataset, the net total amount of "Profit/Losses" over the entire period, and the average of the changes in "Profit/Losses" over the entire period. Additionally, it identifies the greatest increase and decrease in profits (date and amount) over the entire period.
Features

  Calculation of the total number of months included in the dataset.
  Calculation of the net total amount of "Profit/Losses" over the entire period.
  Calculation of the average of the changes in "Profit/Losses" over the entire period.
  Identification of the greatest increase in profits over the entire period.
  Identification of the greatest decrease in losses over the entire period.

Prerequisites

To run this script, you will need Python installed on your system. This script was developed with Python 3.8, but it should be compatible with most Python 3.x versions.
Installation

To run the script, navigate to the cloned directory in your terminal and execute the following command:

bash
python main.py

Ensure your dataset is placed in the Resources directory and is named budget_data.csv. If your dataset has a different name or path, you will need to adjust the file_path variable in the script accordingly.
Data Format

The script expects a CSV file with two columns:

    Date (in format "Jan-2010")
    Profit/Losses (integer value)

Example:

plaintext

Date,Profit/Losses
Jan-2010,867884
Feb-2010,984655

Output

The script outputs the analysis to the terminal and saves it to a file named budget_analysis.txt in the analysis directory. The output includes the total months, net total amount of "Profit/Losses," average change, greatest increase in profits, and greatest decrease in losses.
Contributing

Contributions are welcome! Please feel free to submit pull requests, open issues, or suggest improvements to the project.
License
