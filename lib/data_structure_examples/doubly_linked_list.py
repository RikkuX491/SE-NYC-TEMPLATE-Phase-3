# The head node is going to be the very first node in our doubly linked list, and will point to the next node once we start adding more elements.
# The tail node is going to be the very last node in our doubly linked list, and will point to the previous node once we start adding more elements.
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def append(self, node):
        # Add element to the beginning of the doubly linked list if the doubly linked list is empty. Both head and tail should be the same since there is only 1 node in the doubly linked list in this case.
        if self.head == None:
            self.head = node
            self.tail = node
        
        else:
            # Otherwise, add the node to the end of the linked list.
            node.prev_node = self.tail
            self.tail.next_node = node

            # We also need to make sure to keep track of the new tail.
            self.tail = node

    def delete_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            # access the second-to-last node (self.tail.prev_node)
            prev = self.tail.prev_node

            # update the tail and next_node pointers
            prev.next_node = None
            self.tail = prev

# Doubly linked lists have pointers to the next node as well as the previous node.
class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node