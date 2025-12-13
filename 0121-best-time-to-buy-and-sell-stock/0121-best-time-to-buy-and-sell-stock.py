class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: empty list or only one price
        if not prices:
            return 0

        lowest = prices[0]     # best buying price so far
        max_profit = 0        # maximum profit found

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = price - lowest
                if profit > max_profit:
                    max_profit = profit

        return max_profit
