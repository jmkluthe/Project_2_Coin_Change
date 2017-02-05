#!/usr/bin/env python3
import sys
import time

def changedp(d, n):

    currCoin = n
    iter = 0
    currDenom = d[0]
    currDenomCount = 0
    denomUsed = []
    numDenom = []
    #Create a list that will hold the number of each denomination used to make the change amount.
    eachCoin = [0]*len(d) #
    
    #Create a table indexed by change values that will hold the minimum number of coins to make that amount of change.
    #Initialize to all zeros.
    minCoins = [0]*(n + 1)
    
    #Create a table indexed by change values that will hold the last coin used to make change for that value.
    lastCoinUsed = [0]*(n + 1)
    
    #Loop through the two tables that are indexed by change values up to the change amount needed. Fill the minCoins
    #indexes with the minimum number of coins needed to provide the change amount that represents that position. Fill the
    #lastCoinUsed indexes with the last coin used to when finding the minimum number of coins needed to provide the change
    #amount that represents that position.
    for cents in range(n + 1):
        coinCount = cents
        newCoin = 1
        
        #Loop through the denominations. If the denomination is less than or equal to the current index then use it
        #to determine the minimum number of coins needed to provide change indicated by the index number.
        for j in [coins for coins in d if coins <= cents]:
            
            #Use the cents value and the current denomination to determine if the current index can be built from
            #a previous solution. If so, and it is less than the previous minimum coins solution for the current index,
            #then assign the new minimum coin count and update the newCoin to be used to update the lastCoinUsed table.
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        
        #Update the minCoins table at the current index with the new minimum coins count.
        minCoins[cents] = coinCount
        
        #Update the lastCoinUsed table at the current index with the coin that was last used to find the current minimum
        #coins
        lastCoinUsed[cents] = newCoin
            
    #Use the lastCoinUsed table to determine which denominations, and how many of those denominations, were used to find
    #the solution. Fill the denomUsed table with the used denominations.
    while currCoin > 0:
        denomUsed.append(lastCoinUsed[currCoin])
        currCoin = currCoin - lastCoinUsed[currCoin]

    #Use the denomination and used denomination tables to fill the numDenom (number of each denomination) table.
    for denom in d:
        if denom < denomUsed[0]:
            numDenom.append(currDenomCount)
            continue
        while denom == denomUsed[0]:
            currDenomCount += 1
            if len(denomUsed) == 1:
                break
            else:
                del denomUsed[0]
        numDenom.append(currDenomCount)
        currDenomCount = 0

    return numDenom
'''
with open('Amount.txt') as f:
    #Loop through the file and extract the denominations and change amounts until the end of file is reached.
    while True:
        line = f.readline()
        if not line: break
        #Split the denominations string and turn the result into integers.
        parts = line.split(' ')
        denominations = [int(P) for P in parts]
        print(denominations)
        #Read in the change amount and turn the result into an integer.
        line = f.readline()
        changeNeeded = int(line)
        print(changeNeeded)
        #Time changedp algorithm.
        tStart = time.time()
        minCoins = changedp(denominations, changeNeeded)
        tStop = time.time()
        print("Time:", tStop - tStart)
        print(minCoins)
'''
