class Stock
  def self.best_transaction(prices)
    return nil if prices.size == 1

    lowest_index = prices.index(prices.min)
    prices_after_lowest = prices[lowest_index..prices.size - 1]
    highest_index_after_lowest = lowest_index + prices_after_lowest.index(prices_after_lowest.max)

    [lowest_index, highest_index_after_lowest]
  end
end
