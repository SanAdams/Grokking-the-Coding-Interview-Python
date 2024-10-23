# This comes up while trying to do Palindrome Linked List
# Not sure I've ever reversed a linked list
# So let's do that

from linked_list import LinkedList

linkedlist = LinkedList()
linkedlist.create_linked_list([1,3,2,7])

def reverse_list(list: LinkedList):
    previous_node = None
    next_node = None  
    current_node = list.head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node
        

reversed_list = reverse_list(linkedlist)
print(reversed_list.data, reversed_list.next.data, reversed_list.next.next.data, reversed_list.next.next.next.data) # Expected 7 2 3 1, Actual: 7 2 3 1