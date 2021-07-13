
import os
import csv

budget_csv = os.path.join(".", "Resources", "budget_data.csv")

total_months = 0
total_amount = 0
average_change = 0
greatest_increase = None
greatest_decrease = None
increase_month = ""
decrease_month = ""

with open (budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    print(csv_header)
    months_list = [] 
    amount_list = []
    for row in csv_reader:
        months_list.append(row[0])
        total_months = len(months_list)
        amount_list.append(int(row[1]))
        total_amount = sum(amount_list)
    amount_list2 = amount_list.copy() 
    change_list = []
    months_change = []
    for x,y,m in zip(amount_list, amount_list2[1:], months_list[1:]):
        change = y-x
        change_list.append(change)
        change_tuple = (change, m)
        months_change.append(change_tuple)
    total_change = sum(change_list)
    average_change = round(total_change / len(change_list),2)
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)
    for m in months_change:
        if greatest_increase == m[0]:
            increase_month = m[1]
        if greatest_decrease == m[0]:
            decrease_month = m[1]
        
