# Class definition for Linked List Node
# class LinkedListNode:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def reverse(head):
    prev = None
    next = None
    current = head
    
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next

