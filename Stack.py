"""This program implements a stack data structure along with functions
to reverse a string using the stack and to sort a stack in ascending order."""

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if self._items:
            return self._items.pop()

    def lookup_item(self):
        """Return the item at the top of the stack without removing it."""
        if self._items:
            return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return not self._items


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str


def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.lookup_item() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


if __name__ == "__main__":

    stack = Stack()
    for i in [34, 3, 31, 98, 92, 23]:
        stack.push(i)
    sorted_stack = sort_stack(stack)
    print(reverse_string("hellooo world :("))  # Output: "(: dlrow ooolleh"

    stack = Stack()
    for i in [34, 3, 31, 98, 92, 23]:
        stack.push(i)
    sorted_stack = sort_stack(stack)
    print(sorted_stack._items)