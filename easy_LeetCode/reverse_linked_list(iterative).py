
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # For printing the linked list nicely
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return str(result)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, cur = None, head
        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next
        return prev

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)
sol = Solution()
res = sol.reverseList(head)
print(res)