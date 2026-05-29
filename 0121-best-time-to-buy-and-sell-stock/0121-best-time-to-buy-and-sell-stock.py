"""
U: 
    input: an array "prices" 
        price[i] = price of the stock on ith day 
    output: return the max profit or return 0 if cannot achieve any profit 
    choose a single day to buy and choosing a diff day (later) to sell that stock 

    trick: the best day to buy before today = the minimumn price seen so far 

    edge case = if len == 1, return 0 (no profit possible)
M: 
P: 
    edge case
    1. min_price = prices[0], max_profit = 0 
    2. iterate prices, for each price 
        3. curr_profit = curr_price - min_price
        4. if curr_profit > max_profit, update max profit 
        5. if curr_price < min_price, update min price 
    6. return max_profit 
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for curr_price in prices: 
            curr_profit = curr_price - min_price 
            if curr_profit > max_profit:
                max_profit = curr_profit 
            if curr_price < min_price: 
                min_price = curr_price 
        return max_profit
        