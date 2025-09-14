class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = 0
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            j = i+1
            while j < len(nums) and nums[j] == nums[j-1] + 1:
                j += 1
            if start == nums[j-1]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[j-1]))
            i = j
        return result

nums = [0,1,2,4,5,7]
sol = Solution()
res = sol.summaryRanges(nums)
print(res)