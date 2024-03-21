import os
import csv

# provide file path
file_path = os.path.join('Resources','budget_data.csv')
output_path = os.path.join(r'analysis', 'budget_analysis.txt')

#variables
net_total_col =0
value = 0
total_changes = 0

with open(file_path, 'r') as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")

  #Read the header row and print header
  csv_header = next(csv_reader)
  
  # Count the total number of rows/months
  total_months = sum(1 for row in csv_reader)
  #Reset file pointer to beginning of file 
  csvfile.seek(0)
  
  #Skip the header row
  next(csv_reader)

  #create lists to hold profit/loss and months
  profit_losses_list = []
  months_list = []

  #Iterate through each row in the file starting after the header
  for row in csv_reader: 
    #access second column values (profit/loss) and update the column sum for each row
    #access first column values and update the list with every new row of months
    column_value = float(row[1])
    
    #calculate totals for columns and rows
    net_total_col += round(column_value,None)
   
    #Assign profit/loss
    profit_loss = float(row[1])

    #add profit profit/loss to the list
    profit_losses_list.append(float(profit_loss))
    
    #Calculate changes from one profit loss to the next
    changes = [profit_losses_list[i] - profit_losses_list[i - 1] for i in range(1, len(profit_losses_list))]
    total_changes = sum(changes)
    #Greatest increase/decrease in profits
    greatest_increase = round(max(changes, default = 0))
    greatest_decrease = round(min(changes, default = 0))

    #calculate average 
    #first check if there is data to avoid division by zero, then calc average. The denominator is reduced by 1 since the count of changes starts from 1st position, not zero position (header)
    if profit_losses_list:
      average_change = round(sum(changes)/int(total_months-1),2)
    else:
      average_change = 0

    #Print the results 
output = ("\nFinancial Analysis\n" 
  f"------------------------------" '\n'
  f"Total Months: {total_months}\n"
  f"Total: ${net_total_col}\n"
  f"Average Change: ${average_change}\n"
  f"Greatest Increase in Profits: ${greatest_increase} \n"
  f"Greatest Decrease in Profits: ${greatest_decrease} \n")

#print out results
print(output)

#Write results to a textfile and save in output path
with open(output_path, "w") as txtfile: 
    txtfile.write(output)
 