class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check_list = {}
        for i, val in enumerate(nums):
            rest_val = target - nums[i]
            if rest_val in check_list:
                return [check_list[rest_val],i]
            check_list[val] = i
        return None

nums = [2,7,11,15]
target = 17
sol = Solution()
res = sol.twoSum(nums,target)
print(res)
