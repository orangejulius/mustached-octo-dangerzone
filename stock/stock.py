# given a list of past share prices, find the optimal time to buy and sell
#return a tuple (best time to buy, best time to sell)
def maxProfit(prices):
    lowestPriceIndex = highestPriceIndex = 0
    for i, price in enumerate(prices):
        if price > prices[highestPriceIndex]:
            highestPriceIndex = i
        if price < prices[lowestPriceIndex]:
            lowestPriceIndex = i
            highestPriceIndex = i

    return (lowestPriceIndex, highestPriceIndex)
