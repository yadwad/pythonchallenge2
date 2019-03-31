import os
import csv


budget_data = os.path.join("PyBank", "budget_data.csv")


with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    print(f"Header: {csv_header}")

    
    profit = []
    months = []

    
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])

    
    revenue_change = []

    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))
    
    
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    
    total_months = len(months)

    
    greatest_increase = max(revenue_change)
    
    greatest_decrease = min(revenue_change)


    
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total amount profit/loss: " + "$" + str(sum(profit)))

    print("Average change profit/loss: " + "$" + str(revenue_average))

    print("Greatest increase in profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest decrease in losses: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    
    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total amount profit/loss: " + "$" + str(sum(profit)) + "\n")

    file.write("Average change profit/loss: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest increase in profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest decrease in losses: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

#Financial Analysis
#....................................................................................
#total months: 86
#Total amount profit/loss: $38382578
#Average change profit/loss: $-2315.1176470588234
#Greatest increase in profits: 2/1/2012 $1926159
#Greatest decrease in losses: 9/1/2013 $-2196167
#PS C:\Users\Kwad\Desktop\python1>
