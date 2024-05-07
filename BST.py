"""Binary search tree implementation providing methods for
insertion, deletion, searching, and in-order traversal."""

class BinarySearchTreeNode:
    def __init__(self, data):
        """Initialize the node with the input data."""
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        """Search for a value in the tree. Returns True or False if it exists."""
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min_value(self):
        """Find the minimum value in the tree."""
        if self.left is None:                #reach leftmost leaf node
            return self.data
        return self.left.find_min_value()    #keep going a down a level

    def find_max_value(self):
        """Find the maximum value in the tree."""
        if self.right is None:
            return self.data
        return self.right.find_max_value()

    def find_min_node(self):
        """Find the node with the minimum value."""
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, val):
        """Delete a node with the given value from the tree."""
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_right_subtree = self.right.find_min_node()
            self.data = min_right_subtree.data
            self.right = self.right.delete(min_right_subtree.data)
        return self



def build_tree(elements):
    """Build a binary search tree from input elements."""
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    elements = [13,4,1,9,55,18,3,34]

    # Build the binary search tree
    numbers_tree = build_tree(elements)

    # Test in-order traversal
    print("In-order Traversal:", numbers_tree.in_order_traversal())

    # Test search functionality
    search_value = 13
    if numbers_tree.search(search_value):
        print(f"Value {search_value} found in the tree")
    else:
        print(f"Value {search_value} not found in the tree")

    # Test deletion
    delete_value = 34
    try:
        numbers_tree.delete(delete_value)
        print(f"Value {delete_value} deleted from the tree")
    except ValueError as e:
        print(e)

    # Print the tree after deletion
    print("Tree after Deletion:", numbers_tree.in_order_traversal())
