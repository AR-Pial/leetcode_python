class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(node):
    """ Helper function to print the linked list. """
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)

def createLinkedList(arr):
    """ Helper function to create a linked list from an array. """
    dummy = ListNode()
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next
def mergeTwoLists(list1, list2):
    initial_node = ListNode()
    last_node = initial_node
    while list1 and list2:
        if list1.val <= list2.val:
            last_node.next = list1
            list1 = list1.next
        else:
            last_node.next = list2
            list2 = list2.next
        last_node = last_node.next

    if list1:
        last_node.next = list1
    else:
        last_node.next = list2

    return initial_node.next


list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])

merged_list = mergeTwoLists(list1, list2)
printList(merged_list)
