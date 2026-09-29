import csv
file = open("/workspaces/data_5500_homework/HistoricalData_1790694863779.csv")

data = list(csv.reader(file, delimiter=','))
file.close

print(data)


#we'll be iterating through the data list backwards as to go in the direction of time

for i in range(1, len(data)): #iterating through all rows except the first one and removing the $ from the Close/Last column and then turning the value into a float
    data[i][1] = float(data[i][1][1:])
    
data = data[::-1]
print(data)


#making some variables :)
five_day_moving_average = 0
current_price = 0
buy = 0
firstbuy = 0
profit = 0
total_profit = 0

print("TSLA Mean Reversion Strategy Output:") #header for prints :)

for i in range(4, len(data)):
    

    five_day_moving_average = ((data[i][1] + data[i - 1][1] + data[i - 2][1] + data[i - 3][1] + data[i - 4][1]) / 5) #takes the average of the current value and the previous 4 values
    current_price = data[i][1]

    if current_price / five_day_moving_average <= 0.98: #if the price is below 98% then "buy" will be updated to the current price
        if firstbuy == 0: #firstbuy will only be updated if this if the first buy thats happened
            firstbuy = current_price
        if buy == 0: #will take the first buy value once the price gets low enough and will only get a new value once the stock has sold.
            buy = current_price


        print
        
    elif current_price / five_day_moving_average >= 1.02:  #if the price is above 102% then profit will be updated to current price and there will be a running total added to as well
        profit = current_price
        total_profit += profit

        buy = 0



