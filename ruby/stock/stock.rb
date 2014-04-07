class Stock
  def self.best_transaction(prices)
    best_buy = best_sell = lowest_price_idx = 0

    prices.each_index do |n|
      best_profit = prices[best_sell] - prices[best_buy]
      profit_since_lowest = prices[n] - prices[lowest_price_idx]

      if prices[n] < prices[lowest_price_idx]
        lowest_price_idx = n
      elsif profit_since_lowest > best_profit
        best_buy = lowest_price_idx
        best_sell = n
      end
    end
    [best_buy, best_sell]
  end
end
