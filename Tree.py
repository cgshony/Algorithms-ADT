"""Tree data structure implementation representing the staff in a company and the hierarchy - Framestore LTD
        Attributes: name - The name of the person in the company.
        designation - The djob title.
        children - A list of the child nodes in the tree.
        parent: The parent node of the current node. """

class TreeNode:
    """Initialize a Tree object."""

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def search_node(self, value):
        """Search for a node by the name of the person."""

        if value.lower() in self.name.lower():
            return self
        for child in self.children:
            found_node = child.search_node(value)
            if found_node:
                return found_node
        return None

    def remove_child(self, value):
        for child in self.children:
            if child.name == value:
                self.children.remove(child)
                return True
        return False

    def count_nodes(self):
        """Count the total number of nodes in the subtree of the current node."""

        count = 1
        for child in self.children:
            count += child.count_nodes()
        return count

    def get_subtree(self):
        subtree = [self]
        for child in self.children:
            subtree.extend(child.get_subtree())
        return subtree

    def print_tree(self, property_name):
        if property_name == 'NameTitle':
            if self.designation.strip():
                value = self.name + " (" + self.designation + ")"
            else:
                value = self.name
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

def build_company_tree():
    """Build a sample company tree structure."""

    root = TreeNode('Framestore ', 'LTD')

    ceo = TreeNode('CEO', ' ')
    ceo.add_child(TreeNode('Mel Sullivan ', 'CEO'))
    ceo.add_child(TreeNode('Fiona Walkinshaw ', 'CEO'))

    cto = TreeNode('CTO',' ')
    cto.add_child(TreeNode('Michael Stein ', 'CTO'))

    operations = TreeNode('Operations', ' ')
    operations.add_child(TreeNode('Lottie Cooper ' , 'Operations and Business'))
    operations.add_child(TreeNode('Alison Turner ', 'Operations and Infrastructure'))

    advertising = TreeNode('Advertising', ' ')
    advertising.add_child(TreeNode('James Razzall ', 'US President'))
    advertising.add_child(TreeNode('Krystina WIlson ', 'Executive VP'))

    root.add_child(ceo)
    root.add_child(cto)
    root.add_child(operations)
    root.add_child(advertising)

    return root

if __name__ == '__main__':
    root = build_company_tree()

    #root.print_tree("name") prints only name hierarchys
    # root.print_tree("") prints only job titles hierarchy
    # root.print_tree("NameTitle") prints both
    root.print_tree('NameTitle')

    print("")

    # Search for a node
    node_name = 'James Razzall'
    found_node = root.search_node(node_name)
    if found_node:
        print(f"Node '{node_name}' found: {found_node.name} ({found_node.designation})")
    else:
        print(f"Node '{node_name}' not found.")

    # Remove a node
    node_to_remove = 'Operations'
    if root.remove_child(node_to_remove):
        print(f"Node '{node_to_remove}' removed successfully.")
    else:
        print(f"Node '{node_to_remove}' not found.")

    # Total number of nodes from the root
    print(f"Total number of nodes: {root.count_nodes()}\n")

    print(f"Tree after laying off {node_to_remove}")
    root.print_tree('NameTitle')