from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        q = deque([root])
        d = 0
        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            d += 1
        return d

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(1)
p.right.right.right = TreeNode(9)



solution = Solution()
print(solution.maxDepth(p))

