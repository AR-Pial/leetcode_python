class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  # This will be the intersection node or None if no intersection

# Assuming headA and headB are already created with or without intersection
# Example:

# List A: [4, 1, 8, 4, 5]
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

# List B: [5, 6, 1, 8, 4, 5]
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = headA.next.next  # Intersection at node with value 8

# Solving the intersection problem
solution = Solution()
intersection = solution.getIntersectionNode(headA, headB)

# The output is either the intersection node or None
intersection_val = intersection.val if intersection else None
print(intersection_val)