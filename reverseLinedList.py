# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def reverseList(head):
#     prev = None
#     while head:
#         curr = head
#         head = head.next
#         curr.next = prev
#         prev = curr
#     return prev


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
first.next = second
second.next = third
print(reverseList(first))