# The head node is going to be the very first node in our linked list, and will point to the next node once we start adding more elements.
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        # Add element to the beginning of the list if the list is empty
        if self.head == None:
            self.head = node
            return
        
        # Otherwise, traverse the list to find the last node
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = node

# Since our SinglyLinkedList class is going to contain a series of nodes linked together, we'll create a Node class.
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node