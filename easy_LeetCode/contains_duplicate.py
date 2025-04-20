from enum import unique


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False

nums = [1,2,3]
sol = Solution()
res = sol.containsDuplicate(nums)
print(res)