# given a list of past share prices, find the optimal time to buy and sell
#return a tuple (best time to buy, best time to sell)
def maxProfit(prices):
    bestBuyIndex = bestSellIndex = 0
    possibleBestBuyIndex = 0
    for i, price in enumerate(prices):
        #a lower price than seen before is worth considering as a
        #potential best buying point
        if price < prices[possibleBestBuyIndex]:
            possibleBestBuyIndex = i
        #if the price is higher than seen before, a new best
        #selling point has been found
        if price > prices[bestSellIndex]:
            bestSellIndex = i
        #if the difference between the current price and possible best buy price
        #is greater than the current best selling and buying prices, a new best
        #buying (and selling) point has been found
        if price - prices[possibleBestBuyIndex] > prices[bestSellIndex] - prices[bestBuyIndex]:
            #the possible best buy price is always equal or less than the current best buy price
            #so it's always safe to update the best selling and best buying indicies together
            bestBuyIndex = possibleBestBuyIndex
            bestSellIndex = i

    return (bestBuyIndex, bestSellIndex)
