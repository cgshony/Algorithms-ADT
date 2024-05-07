"""Max Heap Data structure implementation with methods
for insertion, deletion, and peeking at the maximum element"""

class MaxHeap:
    """ Initialize a MaxHeap instance.
        Args - items (list, optional): initial items to build the heap. Default set to None."""

    def __init__(self, items=None):
        if items is None:
            self.heap = []
        else:
            self.heap = items
            self._heapify()

    def _heapify(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self._sift_down(i)

    def push(self, val):
        """Inserts a value into the heap and maintains the heap property."""

        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """ Removes and returns the maximum value from the heap and maintains the property."""

        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self._sift_down(0)
        return max_val

    def _sift_down(self, idx):
        """Restores the heap property, takes an  index from which to start the sift-down operation """

        while idx < len(self.heap):
            max_idx = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < len(self.heap) and self.heap[left] > self.heap[max_idx]:
                max_idx = left
            if right < len(self.heap) and self.heap[right] > self.heap[max_idx]:
                max_idx = right

            if max_idx != idx:
                self.heap[idx], self.heap[max_idx] = self.heap[max_idx], self.heap[idx]
                idx = max_idx
            else:
                break

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] < self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def peek(self):
        """Returns the maximum value in the heap ."""

        if len(self.heap) > 0:
            return self.heap[0]
        return None


if __name__ == "__main__":

    # Initialize a MaxHeap
    initial_items = [10, 5, 15, 3, 7, 12, 17]
    max_heap = MaxHeap(initial_items)
    print("Max Heap:")
    print(max_heap.heap)

    new_elements = [33, 8, 16]
    for element in new_elements:
        max_heap.push(element)
    print("Max Heap after pushing new elements:")
    print(max_heap.heap)

    print("\nPopping element from the Max Heap:")
    print(max_heap.pop())