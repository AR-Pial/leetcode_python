from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        m = len(nums) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])
        return root

        # 2nd way
        # def tree(l,r):
        #     if l > r:
        #         return None
        #     m = (l+r) // 2
        #     root = TreeNode(nums[m])
        #     root.left = tree(l,m-1)
        #     root.right = tree(m+1,r)
        #     return root
        #
        # return(tree(0, len(nums)-1))

nums = [-10, -3, 0, 5, 9]
solution = Solution()
print(solution.sortedArrayToBST(nums))

