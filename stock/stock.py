# given a list of past share prices, find the optimal time to buy and sell
#return a tuple (best time to buy, best time to sell)
def maxProfit(prices):
    bestBuyIndex = bestSellIndex = 0
    possibleBestBuyIndex = 0
    for i, price in enumerate(prices):
        if price < prices[possibleBestBuyIndex]:
            possibleBestBuyIndex = i
        if price > prices[bestSellIndex]:
            bestSellIndex = i
        if price - prices[possibleBestBuyIndex] > prices[bestSellIndex] - prices[bestBuyIndex]:
            bestBuyIndex = possibleBestBuyIndex
            bestSellIndex = i

    return (bestBuyIndex, bestSellIndex)
