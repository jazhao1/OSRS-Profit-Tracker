import sys
import os.path
from os import path
import csv
import re

# Helper Functions

def parseInputPrice(price):
    if (str(price)[-1] == "k"):
        price = float(price[:-1]) * 1000
    elif (str(price)[-1] == "m"):
        price = float(price[:-1]) * 1000000
    else:
        price = float(price)
    return price

def formatNumber(number):
    number = float(number)
    if (number >= 1000000):
        number = round(number/1000000, 3)
        number = str(number) + "m"
    elif (number >= 10000):
        number = round(number/1000, 2)
        number = str(number) + "k"
    else:
        number = str(int(number))

    return number

def unformatNumber(number):
    if number[-1].isdigit():
        return number
    elif number[-1] == "k":
        return float(number[:-1]) * 1000
    elif number[-1] == "m":
        return float(number[:-1]) * 1000000
    else:
        print('invalid number: ' + str(number))

def formatName(label):
    return re.sub("([a-z])([A-Z])","\g<1> \g<2>",label).capitalize()

# Get inputs from terminal

itemName = formatName(sys.argv[1])
price1 = parseInputPrice(sys.argv[2])
price2 = parseInputPrice(sys.argv[3])
amount = None

# Caculate data

if price1 > price2:
    buyPrice = price2
    sellPrice = price1
else:
    buyPrice = price1
    sellPrice = price2

if (len(sys.argv) == 5):
    amount = parseInputPrice(sys.argv[4])

itemPerGp = 1.0/buyPrice
margin = sellPrice - buyPrice

profitPerGp = margin*itemPerGp
profitPer1mGp = profitPerGp * 1000000
profitPer10mGp = profitPerGp * 10000000
profitPer25mGp = profitPerGp * 25000000
profitPer50mGp = profitPerGp * 50000000

# Print data to terminal

print("Item: " + itemName)
print("Buy price: " + str(formatNumber(buyPrice)))
print("Sell price: " + str(formatNumber(sellPrice)))
print("Margin: " + str(formatNumber(margin)))
print('')
print("Profit per 1 gp spent: " + str(profitPerGp))
print("Profit per 1M gp spent: " + str(formatNumber(profitPer1mGp)))
print("Profit per 10M gp spent: " + str(formatNumber(profitPer10mGp)))
print("Profit per 25M gp spent: " + str(formatNumber(profitPer25mGp)))
print("Profit per 50M gp spent: " + str(formatNumber(profitPer50mGp)))
print('')
if (amount):
    print("Quantity: " + str(formatNumber(amount)))
    print("GP required: " + str(formatNumber(amount * buyPrice)))
    print("Total Profit: " + str(formatNumber(margin * amount)))
    print('')

# Save to csv file
if not path.isfile('osrsFlipProfitTracker.csv'):
    file = open('osrsFlipProfitTracker.csv', 'wb')
    file.close()
if (profitPer1mGp >= 10000 or (amount)):
    allRows = []
    with open('osrsFlipProfitTracker.csv', 'rb') as file:
        reader = csv.reader(file)
        header = ['Name', 'Buy Price', 'Sell Price', 'Margin', 'Profit per 1gp', 'Profit per 1m']
        newRow = [itemName, formatNumber(buyPrice), formatNumber(sellPrice), formatNumber(margin), profitPerGp, formatNumber(profitPer1mGp)]
        newRowMilProfit = unformatNumber(newRow[5])
        allRows = list(reader)
        allRows = filter(lambda row: len(row) > 0 and row[0] != newRow[0], allRows)
        if len(allRows) <= 1:
            allRows = [header, newRow]
        elif float(unformatNumber(allRows[-1][5])) >= float(newRowMilProfit):
            allRows.append(newRow)
        else:
            for i in range(1, len(allRows)):
                currRow = allRows[i]
                
                if float(unformatNumber(currRow[5])) <= float(newRowMilProfit):
                    allRows.insert(i, newRow)
                    break


    with open('osrsFlipProfitTracker.csv', 'wb') as file:
        writer = csv.writer(file)
        writer.writerows(allRows)
        
# python rsProfitChecker.py 59519 60000 10
