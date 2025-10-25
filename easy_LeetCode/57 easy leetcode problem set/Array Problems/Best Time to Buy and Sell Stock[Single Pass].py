from convert_sorted_array_to_binary_search_tree import solution


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')

        for p in prices:
            if p < min_price:
                min_price = p
            profit = p - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

prices = [7,1,5,3,6,4]
sol = Solution()
res = sol.maxProfit(prices)
print(res)
