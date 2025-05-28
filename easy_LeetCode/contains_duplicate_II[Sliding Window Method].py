class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Sliding Window Solution
        store = set()
        l = 0

        for i in range(len(nums)):
            if i - l > k:
                store.remove(nums[l])
                l += 1
            if nums[i] in store:
                return True
            store.add(nums[i])
        return False


nums = [1,2,3,1]
k = 3
sol = Solution()
res = sol.containsNearbyDuplicate(nums, k)
print(res)