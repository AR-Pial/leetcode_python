class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        l = 0
        for r in range(1,len(prices)):
           if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > max:
                    max = profit
           else:
               l = r
        return max

prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))