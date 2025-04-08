class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_lnlist(head):
    c = head
    while c:
        print(c.val, end=" -> " if c.next else "\n")  # Correct usage
        c = c.next


p = ListNode(1)
p.next = ListNode(2)
p.next = ListNode(3)
p.next.next = ListNode(5)
p.next.next = ListNode(4)
print_lnlist(p)
