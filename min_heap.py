 Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        self._heap.append(node)
        node_index = self._heap.length() - 1

        while node_index > 0:
            parent_index = (node_index - 1) // 2

            if self._heap[parent_index] <= self._heap[node_index]:
                break
            else:
                self._heap[parent_index], self._heap[node_index] = self._heap[node_index], self._heap[parent_index]
                node_index = parent_index

    def is_empty(self) -> bool:
        """
        Return True if the heap is empty; otherwise, it returns False.
        The runtime complexity of this implementation is O(1).
        """
        return self._heap.length() == 0

    def get_min(self) -> object:
        """
        Return the minimum key in the heap.
        """
        if self._heap.is_empty():
            raise MinHeapException("MinHeap is empty")
        return self._heap[0]

    def remove_min(self) -> object:
        """
        This method returns an object with the minimum key, and removes it from the heap.
        If the heap is empty, the method raises a MinHeapException.

        For the downward percolation of the replacement node:
        if both children of the node have the same value (and are both smaller than the node),
        swap with the left child.

        The runtime complexity of this implementation must be O(log N).
        """
        if self.is_empty():
            raise MinHeapException("MinHeap is empty")

        # Get the minimum value (at root) and replace with last leaf node
        minimum = self._heap[0]
        last_leaf_node = self._heap[self._heap.length() - 1]
        self._heap[0] = last_leaf_node
        self._heap.pop()

        # Perform a downward percolation to restore heap property
        current_index = 0
        while current_index < self._heap.length():
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2

            # If there is no child node, we are done.
            if left_child_index >= self._heap.length():
                break

            # Determine the smallest child node
            if right_child_index < self._heap.length():
                left_child = self._heap[left_child_index]
                right_child = self._heap[right_child_index]
                if left_child <= right_child:
                    smallest_child_index = left_child_index
                else:
                    smallest_child_index = right_child_index
            else:
                smallest_child_index = left_child_index

            # Swap the current node with the smallest child node, if necessary
            smallest_child = self._heap[smallest_child_index]
            if last_leaf_node > smallest_child:
                self._heap[current_index] = smallest_child
                self._heap[smallest_child_index] = last_leaf_node
                current_index = smallest_child_index
            else:
                break

        return minimum

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a DynamicArray with objects in any order, and builds a proper MinHeap from them. The current content of the MinHeap is overwritten. The runtime complexity of this implementation must be O(N).
        """
        self._heap = DynamicArray(list(da))

        for i in range(self._heap.length() // 2, -1, -1):
            self._min_heapify(i)

    def _min_heapify(self, i: int) -> None:
        """
        This method takes an index of a node and makes a heap of the subtree rooted at this node.
        """
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self._heap.length() and self._heap[left] < self._heap[smallest]:
            smallest = left

        if right < self._heap.length() and self._heap[right] < self._heap[smallest]:
            smallest = right

        if smallest != i:
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            self._min_heapify(smallest)

    def size(self) -> int:
        return self._heap.length()

    def clear(self) -> None:
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    This function receives a DynamicArray and sorts its content
    in non-ascending order, using the Heapsort algorithm.
    """
    n = da.length()

    for i in range(n // 2 - 1, -1, -1):
        parent = i
        while parent * 2 + 1 < n:
            child = parent * 2 + 1
            if child + 1 < n and da[child] < da[child + 1]:
                child += 1
            if da[parent] < da[child]:
                da[parent], da[child] = da[child], da[parent]
                parent = child
            else:
                break

    for i in range(n - 1, 0, -1):
        da[0], da[i] = da[i], da[0]
        parent = 0
        while parent * 2 + 1 < i:
            child = parent * 2 + 1
            if child + 1 < i and da[child] < da[child + 1]:
                child += 1
            if da[parent] < da[child]:
                da[parent], da[child] = da[child], da[parent]
                parent = child
            else:
                break

    start = 0
    end = da.length() - 1

    while start < end:
        da[start], da[end] = da[end], da[start]
        start += 1
        end -= 1


def heap_sort(da: DynamicArray) -> None:
    """
    This function receives a DynamicArray and sorts its content
    in non-ascending order, using the Heapsort algorithm.
    """
    n = da.length()

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        parent = i
        while parent * 2 + 1 < n:
            child = parent * 2 + 1
            if child + 1 < n and da[child] > da[child + 1]:
                child += 1
            if da[parent] < da[child]:
                da[parent], da[child] = da[child], da[parent]
                parent = child
            else:
                break

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        da[0], da[i] = da[i], da[0]
        parent = 0
        while parent * 2 + 1 < i:
            child = parent * 2 + 1
            if child + 1 < i and da[child] > da[child + 1]:
                child += 1
            if da[parent] < da[child]:
                da[parent], da[child] = da[child], da[parent]
                parent = child
            else:
                break


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
     Swapping a node with its children until the node
     is swapped into a position on the heap where it is already less
     than both children
    """
    while (2 * parent + 1) < da.length():
        smaller_idx = 2 * parent + 1
        if (2 * parent + 2) < da.length() and da[2 * parent + 2] < da[2 * parent + 1]:
            smaller_idx = 2 * parent + 2
        if da[smaller_idx] > da[parent]:
            return
        da[smaller_idx], da[parent] = da[parent], da[smaller_idx]
        parent = smaller_idx

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
