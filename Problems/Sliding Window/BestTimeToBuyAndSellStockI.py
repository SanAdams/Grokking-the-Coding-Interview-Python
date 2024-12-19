def best_time_to_buy_and_sell_optimal(prices):
    max_profit = 0
    sell = 0
    buy = 1
    for sell in range(len(prices)):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
        else:
            # prices[sell] must be less than prices[buy], 
            # so we might as well calculate profits starting from prices[sell]
            buy = sell
    return max_profit
