# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('../Resources/menu_data.csv')
sales_filepath = Path('../Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, "r") as menu_file:
    csvreader = csv.reader(menu_file, delimiter = ",")
    next(csvreader) 
    for rows in csvreader:
        menu.append(rows)
        

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, "r") as sales_file:
    csvreader = csv.reader(sales_file, delimiter = ",")
    next(csvreader)
    for rows in csvreader:
        sales.append(rows)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for rows in sales:
    print()
    print(rows)

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    
    quantity = int(rows[3])
    sales_Item = (rows[4])
    
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sales_Item not in report.keys():
        report[sales_Item] = {
        "01-count": 0,
        "02-revenue": 0,
        "03-cost": 0,
        "04-profit": 0,
        }

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for row in menu:
        

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        Item = (row[0])
        price = float(row[3])
        cost = float(row[4])


        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sales_Item == Item:

            # @TODO: Print out matching menu data
            print(f"matching data {sales_Item}")
            
            
            # @TODO: Cumulatively add up the metrics for each item key
            report[sales_Item]["01-count"] += quantity
            report[sales_Item]["02-revenue"] += price * quantity
            report[sales_Item]["03-cost"] += cost * quantity
            report[sales_Item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{sales_Item} does not equal {Item}! NO MATCH!")
        

    # @TODO: Increment the row counter by 1
    row_count = row_count+1

# @TODO: Print total number of records in sales data
    print(row_count)


# @TODO: Write out report to a text file (won't appear on the command line output)
