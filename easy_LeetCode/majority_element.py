# Using Boyer-Moore Voting Algorithm
class Solution(object):
    def majorityElement(self, nums):
        res, count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res

nums = [2,2,1,1,1,2,2]
sol = Solution()
result = sol.majorityElement(nums)
print(result)