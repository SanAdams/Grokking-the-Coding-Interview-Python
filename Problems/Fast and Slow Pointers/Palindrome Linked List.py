from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list

def palindrome(head):
    fast = head
    slow = head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      
    slow = reverse_linked_list(slow) 
    
    # Reset fast to be the front of the list, so that we can compare
    fast = head
    
    while slow:
      if slow.data != fast.data:
        return False
      slow = slow.next
      fast = fast.next
    return True