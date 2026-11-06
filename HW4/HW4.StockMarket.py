import json
import csv

#stole this code from hw3 and made it into a function
#this code allows me to use the file directly as a multidimensional list in the following functions
def clean(data):
    data = list(csv.reader(file, delimiter=','))
    for i in range(1, len(data)): #iterating through all rows except the first one and removing the $ from the Close/Last column and then turning the value into a float
        data[i][1] = float(data[i][1][1:])
    data = data[::-1]
    return data


#mean reversion stock trading function
def stonks_mean_reversion(prices): #Now I could totally use a single dimensional list for this, but my old code didn't and I'm lazy so I didn't
    five_day_moving_average = 0
    current_price = 0
    buy = 0
    firstbuy = 0
    profit = 0
    total_profit = 0
    sell = 0
    for i in range(5, len(prices) - 1):
    

        five_day_moving_average = ((prices[i-5][1] + prices[i - 1][1] + prices[i - 2][1] + prices[i - 3][1] + prices[i - 4][1]) / 5) #takes the average of the current value and the previous 4 values
        current_price = prices[i][1]
        #print(current_price / five_day_moving_average)

        if current_price / five_day_moving_average <= 0.98: #if the price is below 98% then "buy" will be updated to the current price
            if firstbuy == 0: #firstbuy will only be updated if this if the first buy thats happened
                firstbuy = current_price
            if buy == 0: #will take the first buy value once the price gets low enough and will only get a new value once the stock has sold.
                buy = current_price

                profit = 0 #allowing a sell if it can 
                #print("Buying at:", current_price)
            
        elif current_price / five_day_moving_average >= 1.02 and profit == 0:  #if the price is above 102% then profit will be updated to current price and there will be a running total added to as well
            profit = round(current_price - buy,2)
            total_profit += profit

            buy = 0 #allowing buy to be set next iteration if it can
            #print("Selling at:", current_price)
            #print("Profit:", profit)
            #print() #extra line :)

    try:
        percent_return = (total_profit / firstbuy) * 100
    except:
        percent_return = 0
    return(total_profit, percent_return)


#simple moving average stock trading function
def stonks_standard_ma(prices): #Now I could totally use a single dimensional list for this, but my old code didn't and I'm lazy so I didn't
    five_day_moving_average = 0
    current_price = 0
    buy = 0
    firstbuy = 0
    profit = 0
    total_profit = 0
    sell = 0
    for i in range(5, len(prices) - 1):
    

        five_day_moving_average = ((prices[i-5][1] + prices[i - 1][1] + prices[i - 2][1] + prices[i - 3][1] + prices[i - 4][1]) / 5) #takes the average of the current value and the previous 4 values
        current_price = prices[i][1]
        #print(current_price / five_day_moving_average)

        if current_price / five_day_moving_average > 1.00: #if the price is below 98% then "buy" will be updated to the current price
            if firstbuy == 0: #firstbuy will only be updated if this if the first buy thats happened
                firstbuy = current_price
            if buy == 0: #will take the first buy value once the price gets low enough and will only get a new value once the stock has sold.
                buy = current_price

                profit = 0 #allowing a sell if it can 
                #print("Buying at:", current_price)
            
        elif current_price / five_day_moving_average < 1 and profit == 0:  #if the price is above 102% then profit will be updated to current price and there will be a running total added to as well
            profit = round(current_price - buy,2)
            total_profit += profit

            buy = 0 #allowing buy to be set next iteration if it can
            #print("Selling at:", current_price)
            #print("Profit:", profit)
            #print() #extra line :)
    try:
        percent_return = (total_profit / firstbuy) * 100
    except:
        percent_return = 0
    return(total_profit, percent_return)

#save results function :)
def save_results(results):
    with open("/workspaces/data_5500_homework/HW4/results.json", "w") as file:
        json.dump(results, file, indent=4)


results = {}

"""
I like to call this next part the "Brute Force Area"

"""
"""
with open("/workspaces/data_5500_homework/HW4/apple_1yr.csv") as file:
    cfile = clean(file)
    results["apple_mr_p"], results["apple_mr_r"] = stonks_mean_reversion(cfile)
    results["apple_sma_p"], results["apple_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/amd_1yr.csv") as file:
    cfile = clean(file)
    results["amd_mr_p"], results["amd_mr_r"] = stonks_mean_reversion(cfile)
    results["amd_sma_p"], results["amd_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/amazon_1yr.csv") as file:
    cfile = clean(file)
    results["amazon_mr_p"], results["amazon_mr_r"] = stonks_mean_reversion(cfile)
    results["amazon_sma_p"], results["amazon_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/cisco_1yr.csv") as file:
    cfile = clean(file)
    results["cisco_mr_p"], results["cisco_mr_r"] = stonks_mean_reversion(cfile)
    results["cisco_sma_p"], results["cisco_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/meta_1yr.csv") as file:
    cfile = clean(file)
    results["meta_mr_p"], results["meta_mr_r"] = stonks_mean_reversion(cfile)
    results["meta_sma_p"], results["meta_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/microsoft_1yr.csv") as file:
    cfile = clean(file)
    results["microsoft_mr_p"], results["microsoft_mr_r"] = stonks_mean_reversion(cfile)
    results["microsoft_sma_p"], results["microsoft_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/netflix_1yr.csv") as file:
    cfile = clean(file)
    results["netflix_mr_p"], results["netflix_mr_r"] = stonks_mean_reversion(cfile)
    results["netflix_sma_p"], results["netflix_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/qualcomm_1yr.csv") as file:
    cfile = clean(file)
    results["qualcomm_mr_p"], results["qualcomm_mr_r"] = stonks_mean_reversion(cfile)
    results["qualcomm_sma_p"], results["qualcomm_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/starbucks_1yr.csv") as file:
    cfile = clean(file)
    results["starbucks_mr_p"], results["starbucks_mr_r"] = stonks_mean_reversion(cfile)
    results["starbucks_sma_p"], results["starbucks_sma_r"] = stonks_standard_ma(cfile)

with open("/workspaces/data_5500_homework/HW4/tesla_1yr.csv") as file:
    cfile = clean(file)
    results["tesla_mr_p"], results["tesla_mr_r"] = stonks_mean_reversion(cfile)
    results["tesla_sma_p"], results["tesla_smar_r"] = stonks_standard_ma(cfile)
"""


tickers = ["apple", "amd", "amazon", "cisco", "meta", "microsoft", "netflix", "qualcomm", "starbucks", "tesla"]


for ticker in tickers:
    with open(f"/workspaces/data_5500_homework/HW4/{ticker}_1yr.csv") as file:
        cfile = clean(file)
        results[f"{ticker}_mr_profit"], results[f"{ticker}_mr_%return"] = stonks_mean_reversion(cfile)
        results[f"{ticker}_sma_profit"], results[f"{ticker}_sma_%return"] = stonks_standard_ma(cfile)



#saving dem results
save_results(results)
#print(results)