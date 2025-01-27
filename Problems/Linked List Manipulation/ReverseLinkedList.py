# Class definition for Linked List Node
class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def print_list(ll):
    while ll:
      print(f'{ll.data} -->', end = " ")
      ll = ll.next
    print('None', end = " ")
      
    

def reverse(head):
  prev = None
  next = None
  current = head

  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

ll = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
print_list(ll)
print()
print_list(reverse(ll))
