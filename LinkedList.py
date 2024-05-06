"""
Implementation of a singly linked list with basic functionality including:
appending nodes, inserting a node, finding a node with a given value, getting an index,
and reversing the linked list.
"""

class Node:
    """Initialize a new node with the given value.
    Args - value: The value to be stored in the node."""

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """A singly linked list implementation. Initializes an empty linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the end of the linked list.
        Args - data: The data to be stored in the new node."""

        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def delete_node(self, key):
        """Delete the first occurrence of a node with the given value from the linked list.
        Args - key: The value of the node to be deleted."""

        current_node = self.head
        if current_node and current_node.value == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.value != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            raise ValueError("Node with specified value not found")
        prev_node.next = current_node.next
        current_node = None

    def insert_node(self, prev_node, data):
        """Insert a new node with the given data after the specified node.
        Args - prev_node: The node after which the new node should be inserted.
             - data: The value to be stored in the new node."""

        if not prev_node:
            raise ValueError("Given node does not exist")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def find_node(self, key):
        """Find and return the first node with the specified value.
        Args - key: The value of the node to find."""

        current_node = self.head
        while current_node and current_node.value != key:
            current_node = current_node.next
        return current_node

    def get_index(self, index):
        """Get the value at the specified index.
        Args - index: The index of the value to retrieve."""

        if index < 0:
            return None
        count = 0
        current_node = self.head
        while current_node:
            if count == index:
                return current_node.value
            count += 1
            current_node = current_node.next
        return None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return prev


if __name__ == '__main__':
    # Create a new linked list
    ll = LinkedList()

    # Append nodes
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    # Print linked list
    print("Initial Linked List:")
    current_node = ll.head
    while current_node:
        print(current_node.value, end=" -> ")
        current_node = current_node.next
    print("None")

    # Find and delete a node with value 3
    ll.delete_node(3)

    # Insert a new node with given value
    node_2 = ll.find_node(2)
    ll.insert_node(node_2, 5)

    # Print the updated linked list
    print("\nUpdated Linked List:")
    current_node = ll.head
    while current_node:
        print(current_node.value, end=" -> ")
        current_node = current_node.next

    # Get the value at index 1
    value_at_index_1 = ll.get_index(1)
    print("\nValue at index 1:", value_at_index_1)

    # Reverse
    ll.reverse()

    print("\nReversed Linked List:")
    current_node = ll.head
    while current_node:
        print(current_node.value, end=" -> ")
        current_node = current_node.next
    print("None")