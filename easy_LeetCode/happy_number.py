class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sqr_sum = set()
        while n != 1:
            if n in sqr_sum:
                return False
            sqr_sum.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return True

n = 19
sol = Solution()
res = sol.isHappy(n)
print(res)