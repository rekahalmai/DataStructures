

class Heap:
    """Simple implementation of a binary heap, that can be seen as an almost perfect binary tree.
    Max and min heap properties are implemented in the build_max_heap and build_min_heap functions respectively.

    Max heap property: every child is smaller or equal to its parent.

    Ex:

           10
        /     \
       9       6
      / \     / \
     8  4    5   2
    / \  \
   7  3  0

     This is equal to the following array representation:

     [10, 9, 6, 8, 4, 5, 2, 7, 3, 0]

     Min heap property: every child is larger or equal to its parent.

     The heap has two attributes:
     - The length of the heap array (get_len())
     - The heap_size: max elements in heap, generally heap_size == get_len()
    """
    def __init__(self, heap):
        self.heap = list(heap)
        self.heap_size = len(heap)


    def get_len(self):
        """Return the length of the heap array"""
        return len(self.heap)


    def max_heapify(self, i):
        """Given an array and an index, verify whether the index is well placed, that is whether the
        subarray defined by it is maximum heap. 0(lg n) complexity"""
        largest, left_index, right_index = i, 2*i+1, 2*i+2
        current_length = self.heap_size

        if (left_index < current_length) and (self.heap[left_index] > self.heap[largest]):
            largest = left_index

        if (right_index < current_length) and (self.heap[right_index] > self.heap[largest]):
            largest = right_index

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.max_heapify(largest)
        return self.heap


    def min_heapify(self, i):
        """Given an index, verifies whether the subarray defined by the node at the given index is a minimum heap.
        0(lg n) complexity"""
        smallest, left_index, right_index = i, 2*i+1, 2*i+2
        current_length = self.heap_size

        if (left_index < current_length) and (self.heap[left_index] < self.heap[smallest]):
            smallest = left_index

        if (right_index < current_length) and (self.heap[right_index] < self.heap[smallest]):
            smallest = right_index

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.max_heapify(smallest)
        return self.heap



    def build_max_heap(self):
        """Builds the maximum heap from the array given, following the max heap property.
        Running time: O(n lgn), although asymptotically tight bound is O(n)"""
        self.heap_size = self.get_len()
        for i in range(self.get_len()//2, -1, -1):
            self.max_heapify(i)


    def build_min_heap(self):
        """Builds the minimum heap from the array given, following the max heap property.
        Running time: O(n lgn), although asymptotically tight bound is O(n)"""
        self.heap_size = self.get_len()
        for i in range(self.get_len()//2, -1, -1):
            self.min_heapify(i)


    def heap_sort(self):
        """Sort the array elements in increasing order. O(n lgn) running time."""
        self.build_max_heap()

        for i in range(self.get_len()-1, -1, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heap_size -= 1
            self.max_heapify(0)


def main():
    """Example usage of the heap object"""
    my_heap = Heap(heap=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Initial heap array: {my_heap.heap}")
    my_heap.build_min_heap()
    print(f"My heap after building min_heap: {my_heap.heap}")
    my_heap.build_max_heap()
    print(f"My heap after building max_heap: {my_heap.heap}")
    my_heap.heap_sort()
    print(f"My heap after heap-sort: {my_heap.heap}")


if __name__ == '__main__':
    main()