import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("analysis", "pybank_analysis.txt")

total_months = 0
total_change = 0 
total_profit_loss = 0
greatest_inc_value =  -9999
greatest_dec_value = 9999

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #create counting variable 
    csv_header = next(csvreader)
    
    # Read each row of data after the first row of data
    for row in csvreader:
        total_months += 1 
        current_profit = int(row[1])
     
        # Add the profit/loss value to the total
        total_profit_loss += current_profit

        #Calculate the change in profit/loss and add it to the total change
        if total_months > 1:
            change = current_profit - previous_profit_loss
            total_change += change
            if change > greatest_inc_value:
                greatest_inc_month = row[0]
                greatest_inc_value = change
            if change < greatest_dec_value:
                greatest_dec_month = row[0]
                greatest_dec_value = change
        # Set the current profit/loss as the previous for the next iteration
        previous_profit_loss = current_profit
        
average_change = round(total_change / (total_months-1),2)

output = (
    f"The net total over the period is:${total_profit_loss}\n"
    f"Total number of months:{total_months}\n"
    f"The average change is ${average_change}\n"
    f"The month with the greatest increase is {greatest_inc_month},${greatest_inc_value}\n"
    f"The month with the greatest decrease is {greatest_dec_month},${greatest_dec_value}"
)
with open(OUTPUT_PATH, "w") as outfile:
    outfile.write(output)
    print(output)