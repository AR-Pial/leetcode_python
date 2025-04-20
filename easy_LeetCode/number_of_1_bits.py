class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res

n = 11
sol = Solution()
result = sol.hammingWeight(n)
print(result)