# Using dictionary solution
class Solution(object):
    def majorityElement(self, nums):
        count = {}
        num, maxCount = 0,0

        for n in nums:
            count[n] = 1 + count.get(n,0)

            num = n if count[n] > maxCount else num
            maxCount = max(count[n], maxCount)

        return num

nums = [2,2,1,1,1,2,2]
sol = Solution()
result = sol.majorityElement(nums)
print(result)