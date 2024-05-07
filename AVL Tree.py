class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # Pointer to parent node in tree
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            # Value already in tree
            pass

    def _inspect_insertion(self, cur_node, path=[]):
        # Insertion inspection logic here
        pass

    # Other methods go here...

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        return False


if __name__ == "__main__":
    # Create an AVL tree
    avl_tree = AVLTree()

    # Insert some values into the AVL tree
    values = [10, 5, 15, 3, 7, 12, 17]
    for value in values:
        avl_tree.insert(value)

    # Print the AVL tree
    print("AVL Tree:")
    print(avl_tree)

    # Search for a value in the AVL tree
    search_value = 12
    if avl_tree.search(search_value):
        print(f"Value {search_value} found in the tree")
    else:
        print(f"Value {search_value} not found in the tree")

    # Delete a value from the AVL tree
    delete_value = 5
    avl_tree.delete(delete_value)
    print(f"Deleted value {delete_value} from the tree")

    # Print the AVL tree after deletion
    print("AVL Tree after deletion:")
    print(avl_tree)
