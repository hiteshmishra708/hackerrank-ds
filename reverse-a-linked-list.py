# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    if not head:
        return head
    h = head
    q = None
    p = h.next
    while (p):
        h.next = q
        q = h
        h = p
        p = h.next
    h.next = q
    return h