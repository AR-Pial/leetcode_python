class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Hash Map / Dictionary solution
        store = {}
        for i, num in enumerate(nums):
            if num in store and (i - store[num]) <= k:
                return True
            store[num] = i
        return False

nums = [1,2,3,1]
k = 3
sol = Solution()
res = sol.containsNearbyDuplicate(nums, k)
print(res)