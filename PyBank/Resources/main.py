# Import the os module
import os

# Module for reading CSV files
import csv
 
# Define resources path 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
 
# Define variables 
total_months = 0 
total_revenue = 0 
revenue_change_list = [] 
prev_month_revenue = 0 
greatest_increase_month = "" 
greatest_decrease_month = "" 
greatest_increase_revenue = 0 
greatest_decrease_revenue = 0 


# Open budget_data to read as a csv file 
with open(csvpath) as csv_file:
# Make csv file an iteratable object, use dictionary type of reader 
    csv_reader = csv.DictReader(csv_file, delimiter=",") 
    # For Loop      
    for row in csv_reader: 
        # Find total months 
        total_months += 1 

        # Find total revenue 
        total_revenue = total_revenue + int(row["Profit/Losses"]) 
        
        # Find revenue change for each month using if statement 
        revenue_change = int(row["Profit/Losses"]) - prev_month_revenue 
        if total_months > 1:
            revenue_change_list.append(revenue_change) 
         
        # Pre_month_revenue needs to be the new value, not 0 
        prev_month_revenue = int(row["Profit/Losses"]) 
 
        # Find greatest revenue_change increase 
        if revenue_change > greatest_increase_revenue: 
            greatest_increase_revenue = revenue_change 
            # Find greatest increase month 
            greatest_increase_month = row["Date"] 
        # Find greatest revenue_change decrease 
        if revenue_change < greatest_decrease_revenue: 
            greatest_decrease_revenue = revenue_change 
            # Find greatest decrease month 
            greatest_decrease_month = row["Date"] 
 
# Find the FINAL revenue change average, sum / length 
revenue_average = round(sum(revenue_change_list) / len(revenue_change_list), 2) 
 
output_string = f'''
            Financial Analysis
            -------------------------
            Total Months: {total_months}
            Total: ${total_revenue}
            Average Change: ${revenue_average}
            Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_revenue})
            Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_revenue}) 

        '''
print(output_string)
 
 
# Export a text.file and print PyBank results
output_path = "../analysis/PyBank_Results.txt" 
with open(output_path, "w") as text_file: 
    text_file.write("Financial Analysis") 
    text_file.write("\n") 
    text_file.write("------------------------") 
    text_file.write("\n") 
    text_file.write(f"Total Months: {total_months}") 
    text_file.write("\n") 
    text_file.write(f"Total: ${total_revenue}") 
    text_file.write("\n") 
    text_file.write(f"Average Change: ${revenue_average}") 
    text_file.write("\n") 
    text_file.write(f"Greatest Increase: {greatest_increase_month} (${greatest_increase_revenue})")  
    text_file.write("\n") 
    text_file.write(f"Greatest Increase: {greatest_decrease_month} (${greatest_decrease_revenue})") 
