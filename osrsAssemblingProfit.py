import sys
import os.path
from os import path
import csv
import locale
import requests
import datetime
import time

now = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, 'en_US')

# Helper Functions

def getDateDifference(unitTimeStamp):
    lastUpdated = datetime.datetime.fromtimestamp(unitTimeStamp)
    difference = (now - lastUpdated).total_seconds()/60
    return round(difference, 2)

def formatNumberCommas(number):
    return locale.format("%d", number, grouping=True)

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


headers = {
    'User-Agent': 'Am using this for personal use for personal project. Am planning to track my favorite items low and high without having to visit wiki',
    'From': 'zeakchi@gmail.com'  # This is another valid field
}

def getPriceData(id):
    return requests.get('https://prices.runescape.wiki/api/v1/osrs/latest?id='+ str(id), headers=headers).json()['data'][str(id)]


justiciarSet = getPriceData(22438)
justiciarHead = getPriceData(22326)
justiciarTop = getPriceData(22327)
justiciarBottom = getPriceData(22328)

ancestralSet = getPriceData(21049)
ancestralHead = getPriceData(21018)
ancestralTop = getPriceData(21021)
ancestralBottom = getPriceData(21024)

magicFang = getPriceData(12932)
toxicStaff = getPriceData(12902)
deadStaff = getPriceData(11791)

toxicTrident = getPriceData(12900)
# trident = getPriceData(11907)

kodaiWand = getPriceData(21006)
masterWand = getPriceData(6914)
kodaiInsignia = getPriceData(21043)


cost = 0 - justiciarHead['high'] - justiciarTop['high'] - justiciarBottom['high']
if (justiciarSet['high'] + cost > 0 or True):
    print("Justiciar")
    print("          head: ", formatNumberCommas(justiciarHead['high']), "    ", getDateDifference(justiciarHead['highTime']), " minutes ago")
    print("           top: ", formatNumberCommas(justiciarTop['high']), "    ", getDateDifference(justiciarTop['highTime']), " minutes ago")
    print("        bottom: ", formatNumberCommas(justiciarBottom['high']), "    ", getDateDifference(justiciarBottom['highTime']), " minutes ago")
    print("-------------------------------")
    print("      set high: ", formatNumberCommas(justiciarSet['high']), "    ", getDateDifference(justiciarSet['highTime']), " minutes ago")
    print("       set low: ", formatNumberCommas(justiciarSet['low']), "    ", getDateDifference(justiciarSet['lowTime']), " minutes ago")
    print("    set margin: ", formatNumberCommas(justiciarSet['high'] - justiciarSet['low']))
    print("-------------------------------")
    print("items buy cost: ", formatNumberCommas(cost))
    print("   Profit high: ", formatNumberCommas(justiciarSet['high'] + cost))
    print("    Profit low: ", formatNumberCommas(justiciarSet['low'] + cost))

    print("==========================================")

# cost = 0 - ancestralHead['high'] - ancestralTop['high'] - ancestralBottom['high']
# if (ancestralSet['high'] + cost > 0 or True):
#     print("Ancestral")
#     print("          head: ", formatNumberCommas(ancestralHead['high']), "    ", getDateDifference(ancestralHead['highTime']), " minutes ago")
#     print("           top: ", formatNumberCommas(ancestralTop['high']), "    ", getDateDifference(ancestralTop['highTime']), " minutes ago")
#     print("        bottom: ", formatNumberCommas(ancestralBottom['high']), "    ", getDateDifference(ancestralBottom['highTime']), " minutes ago")
#     print("-------------------------------")

#     print("      set high: ", formatNumberCommas(ancestralSet['high']), "    ", getDateDifference(ancestralSet['highTime']), " minutes ago")
#     print("       set low: ", formatNumberCommas(ancestralSet['low']), "    ", getDateDifference(ancestralSet['lowTime']), " minutes ago")
#     print("    set margin: ", formatNumberCommas(ancestralSet['high'] - ancestralSet['low']))
#     print("-------------------------------")
#     print("items buy cost: ", formatNumberCommas(cost))
#     print("   Profit high: ", formatNumberCommas(ancestralSet['high'] + cost))
#     print("    Profit low: ", formatNumberCommas(ancestralSet['low'] + cost))

#     print("==========================================")

# cost = 0 - masterWand['high'] - kodaiInsignia['high']
# if (kodaiWand['high'] + cost > 0):
#     print("Kodai Wand")
#     print("    Master wand: ", formatNumberCommas(masterWand['high']), "    ", getDateDifference(masterWand['highTime']), " minutes ago")
#     print(" Kodai insignia: ", formatNumberCommas(kodaiInsignia['high']), "    ", getDateDifference(kodaiInsignia['highTime']), " minutes ago")
#     print("-------------------------------")
#     print("Kodai Wand High: ", formatNumberCommas(kodaiWand['high']), "    ", getDateDifference(kodaiWand['highTime']), " minutes ago")
#     print("Kodai Wand Low : ", formatNumberCommas(kodaiWand['low']), "    ", getDateDifference(kodaiWand['lowTime']), " minutes ago")
#     print("-------------------------------")
#     print(" items buy cost: ", formatNumberCommas(cost))
#     print("    Profit high: ", formatNumberCommas(kodaiWand['high'] + cost))
#     print("     Profit low: ", formatNumberCommas(kodaiWand['low'] + cost))

#     print("==========================================")
cost = 0 - deadStaff['high'] - magicFang['high']
if (toxicStaff['high'] + cost > 0 or True):
    print("Toxic Staff")
    print("    Staff of Dead: ", formatNumberCommas(deadStaff['high']), "    ", getDateDifference(deadStaff['highTime']), " minutes ago")
    print("       Magic Fang: ", formatNumberCommas(magicFang['high']), "    ", getDateDifference(magicFang['highTime']), " minutes ago")
    print("    Toxic Trident: ", formatNumberCommas(toxicTrident['high']), "    ", getDateDifference(toxicTrident['highTime']), " minutes ago")
    print("-------------------------------")

    print(" Toxic Staff High: ", formatNumberCommas(toxicStaff['high']), "    ", getDateDifference(toxicStaff['highTime']), " minutes ago")
    print(" Toxic Staf  Low : ", formatNumberCommas(toxicStaff['low']), "    ", getDateDifference(toxicStaff['lowTime']), " minutes ago")
    print("     Staff Margin: ", formatNumberCommas(toxicStaff['high'] - toxicStaff['low']))
    print("-------------------------------")
    print("   items buy cost: ", formatNumberCommas(cost))
    print("      Profit high: ", formatNumberCommas(toxicStaff['high'] + cost))
    print("       Profit low: ", formatNumberCommas(toxicStaff['low'] + cost))


print("==========================================")
print("==========================================")



# if not path.isfile('osrsAssemblyProfit.csv'):
#     file = open('osrsAssemblyProfit.csv', 'wb')
#     file.close()

# allRows = []
# header = ['Name', 'Piece1', 'Piece2', 'Piece3', 'Material Cost', 'Product Price High', 'Product Price Low', 'Product High Profit', 'Product Low Profit']
# justiciar = ['Justciar', formatNumberCommas(justiciarHead['high']), formatNumberCommas(justiciarTop['high']), formatNumberCommas(justiciarBottom['high'])]
# toxicDeadStaff = ['Toxic Stauff']
# kodai = ['Kodai']

# with open('osrsFlipProfitTracker.csv', 'wb') as file:
#         writer = csv.writer(file)
#         writer.writerows(allRows)







