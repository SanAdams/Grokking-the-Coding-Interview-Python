class Node:
    value: int
    def __init__(self, value):
        self.value = value
        self.next = None
    
def addToEnd(head: Node, data) -> Node:
    new_node = Node(data)
    dummy = head
    while dummy != None:
        print (dummy.value)
        if dummy.next == None:
            dummy.next = new_node
        dummy = dummy.next
    return head

def hasCycle(head: Node):
    fast_pointer = head.next.next
    slow_pointer = head.next

    while (fast_pointer != None):
        # Advance the slow_pointer once
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if fast_pointer == slow_pointer:
            return True

    return False
    
head: Node = Node(4)
node1 = addToEnd(head, Node(-1))
head.next = node1
node2 = addToEnd(head, Node(3))
head.next.next = node2
node3 = addToEnd(head, Node(2))
head.next.next.next = node3
    
