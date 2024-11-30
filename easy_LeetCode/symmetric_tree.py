class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def is_mirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left))

        return is_mirror(root.left, root.right)
# tree = [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
solution = Solution()
print(solution.isSymmetric(root))