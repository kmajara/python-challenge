Election Analysis Project
Overview

This Election Analysis Project is designed to automate the vote counting process for a local election. The script reads election data from a CSV file, calculates the total votes each candidate received, determines the percentage of votes for each candidate, and identifies the winner of the election based on popular vote.

Features

  Reads data from a CSV file containing election data.
  Calculates total votes cast in the election.
  Calculates the total number of votes and the percentage of total votes each candidate won.
  Determines the winner of the election based on popular vote.
  Outputs the analysis to the terminal and saves it to a text file.

Prerequisites

Ensure you have Python installed on your system. This script was developed with Python 3.8. If you're using a different version of Python, the code should still work, but it's recommended to use Python 3.x.Installation

No additional installation is required for the core functionality beyond what's stated above. 

Usage

To run the script, navigate to the project directory and execute the following command in your terminal:

bash

python main.py

Ensure the CSV file with election data is placed in the PyPoll/Resources directory. The default file name expected is election_data.csv. If your file has a different name or location, you will need to modify the file_path variable in the script.
Data Format

The script expects a CSV file with three columns:

  Voter ID
  County
  Candidate

Example:

Voter ID,County,Candidate
12864552,Marsh,Charles Casper Stockham
17444633,Marsh,Diana DeGette

Output

The script outputs the election analysis to the terminal and saves it to a file named election_analysis.txt in the analysis directory. The output includes:

  Total votes cast in the election
  Total votes and the percentage of votes each candidate won
  The winner of the election based on popular vote

Contributing

Contributions to the Election Analysis Project are welcome! Please refer to CONTRIBUTING.md for guidelines.
License
