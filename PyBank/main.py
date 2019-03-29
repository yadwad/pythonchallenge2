import os
import csv

budgetcsv = os.path.join("PyBank","budget_data.csv")

def getcount (budgetdata):
    _total_months = int(budgetdata[1])

    print(f"stats for {budgetdata [0]})

with open(budgetcsv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)



 