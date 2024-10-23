def palindrome(head):
    fast = head
    slow = head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

     # reverse the list from that position 
    slow = reverse_linked_list(slow) 

    # Reset fast to be the front of the list, so that we can compare
    fast = head
    
    while slow:
      if slow.data != fast.data:
        return False
      slow = slow.next
      fast = fast.next
    return True

def reverse_linked_list(pointer):
    prev = None
    next = None
    curr = pointer
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev