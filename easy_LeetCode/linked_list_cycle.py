class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## using hashmap(dict set)
# def hasCycle(head: ListNode) -> bool:
#     visited = set()  # HashSet to store visited nodes
#
#     while head:
#         if head in visited:
#             return True  # Cycle detected
#         visited.add(head)  # Mark node as visited
#         head = head.next  # Move to next node
#
#     return False  # No cycle found

## using Floyd's Cycle Detection Algorithm
def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# Example 1: Linked List with a Cycle
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle here (tail connects to node2)

print("Example 1: Cycle present?", hasCycle(node1))  # Output: True