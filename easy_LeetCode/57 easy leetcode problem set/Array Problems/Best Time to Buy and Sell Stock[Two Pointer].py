from convert_sorted_array_to_binary_search_tree import solution


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        left, right = 0,1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit,max_profit)
            else:
                left = right
            right += 1

        return max_profit



prices = [7,1,5,3,6,4]
sol = Solution()
res = sol.maxProfit(prices)
print(res)
