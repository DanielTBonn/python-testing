# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    new_head = None
    current = head
    buildArray = []
    size = 0

    while current is not None:
        buildArray.append(current.val)
        next = current.next
        current.next = new_head
        new_head = current
        current = next
        size += 1
    
    current = head
    currentSize = 0
    while current is not None:
        currentSize += 1
        temp = current.val
        for i in buildArray[::-1]:
            if (i != current.val) or (size < currentSize):
                return True
            else:
                current = current.next

    
    return False

head = ListNode(1)
node2 = ListNode(2)
head.next = node2

hasCycle(head)