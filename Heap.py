from math import floor

class Heap:

    def __init__(self, heap_array, heap_size):
        self.heap = heap_array
        self.heap_size = heap_size
        self._len = len(heap_array)

    def left(self, i):
        if 2*i <= self._len:
            return self.heap[2 * i]
        else:
            print("Index out of range, no left child exist")
            return None

    def right(self, i):
        if 2*i+1 <= self._len:
            return self.heap[2 * i + 1]
        else:
            print("Index out of range, no right child exist")
            return None

    def parent(self, i):
        if (int(floor(i/2)) < self._len) and (int(floor(i/2)) != i):
            return self.heap[int(floor(i / 2))]
        else:
            print("No parent exist")
            return None


    def get_len(self):
        return self._len

    def max_heapify(self, i):
        left, right = self.left(i), self.right(i)
        largest = i

        if (left is not None) and (left <= self.heap_size) and (self.heap[left] > self.heap[i]):
            largest = left

        if (right is not None) and (right <= self.heap_size) and (self.heap[right] > self.heap[i]):
            largest = right

        if largest != i:
            value = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = value

            self.max_heapify(largest)
            print("Called max heapi")

    def build_max_heap(self):
        """Builds the maimum heap binary tree from the array given"""

        self.heap_size = self._len
        i = int(floor(self._len/2))

        for i in range(int(floor(self._len/2)), 0, -1):
            self.max_heapify(i)




def main():

    my_heap = Heap(heap_array=[1, 2, 3, 5, 8, 1, 2, 3, 5, 8], heap_size=10)
    print(my_heap.get_len())

    print(my_heap.left(1))
    print(my_heap.right(1))
    print(my_heap.parent(1))

    print(2 is not None)
    my_heap.max_heapify(0)
    #my_heap.build_max_heap()


if __name__ == '__main__':
    main()