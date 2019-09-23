import csv

with open("/Users/peirangxu/Desktop/Python-challenge/PyBank/budget_data.csv", newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  ## skip the header of the csv file
    
    #create empty lists
    month = []
    profit = []
    change = []
    
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))
        
    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i]) #change in profit/loss
        row[1]
        
len(month) #total number of month included
sum(profit) #sum of Profit & Loss
average_profit = sum(change)/len(change) #average profit/loss
max_profit = max(change) #maximum profit/loss
min_profit = min(change) #minimumu profit/loss
max_date = month[change.index(max_profit)+1] #date of maximum change in profit/loss
min_date = month[change.index(min_profit)+1] #date of minimum change in profit/loss

print(f'There are a total of {len(month)} months included in the dataset')
print(f'There is net total of {sum(profit)} profit/loss over the entire period')
print(f'The average profit/loss change is ${round(average_profit, 2)}')
print(f'The maximum change in profit/loss is ${max_profit} on {max_date}')
print(f'The minimum change in profit/loss is ${min_profit} on {min_date}')

#Write results in a txt file
with open("/Users/peirangxu/Desktop/Python-challenge/PyBank/Financial_Analysis_Summary.txt","w") as text:
    text.write("Financial Analysis \n")
    text.write("--------------------------\n")
    text.write("Total Months:" +str(len(month)) + "\n")
    text.write("Total: $" +str(sum(profit))+"\n")
    text.write("Average Change: $"+str(round(average_profit,2))+"\n")
    text.write("Greatest Increase in Profits:" + str(max_date)+
               " ($"+str(max_profit)+")"+"\n")
    text.write("Greatest Decrease in Profits:" + str(min_date)+
               " ($"+str(min_profit)+")"+"\n")