class Solution(object):
    def singleNumber(self, nums):
        r = 0
        for num in nums:
            r = r ^ num
        return r


nums = [2,4,2,1,1]
s = Solution()
print(s.singleNumber(nums))