class Stock
  def self.best_transaction(prices)
    self.best_transaction_and_lowest(prices)[0..1]
  end

  def self.best_transaction_and_lowest(prices, n = prices.size - 1)
    return [0, 0, 0] if n == 0

    buy_idx, sell_idx, lowest_price_idx = self.best_transaction_and_lowest(prices, n - 1)

    if prices[n] < prices[lowest_price_idx]
      lowest_price_idx = n
    end

    if prices[n] > prices[sell_idx]
      sell_idx = n
    end

    profit_so_far = prices[sell_idx] - prices[buy_idx]
    profit_since_lowest = prices[n] - prices[lowest_price_idx]

    if profit_since_lowest > profit_so_far
      return [lowest_price_idx, n, lowest_price_idx]
    else
      return [buy_idx, sell_idx, lowest_price_idx]
    end
  end
end
