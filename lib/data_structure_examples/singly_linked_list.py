# The head node is going to be the very first node in our linked list, and will point to the next node once we start adding more elements.
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

# Since our SinglyLinkedList class is going to contain a series of nodes linked together, we'll create a Node class.
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node