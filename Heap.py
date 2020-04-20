from math import floor

class Heap:
    def __init__(self, heap_array, heap_size):
        self.heap = heap_array
        self.heap_size = heap_size


    def get_len(self):
        return len(self.heap)


    def left_index(self, i):
        if i == 0:
            return 1
        elif (i==0) and (2*i < self.get_len()):
            return 2*i
        else:
            return None


    def get_left_value(self, i):
        try:
            return self.heap[self.left_index(i)]
        except TypeError:
            return None


    def right_index(self, i):
        if i==0:
            return 2
        elif (i!=0) and ((2*i+1)<self.get_len()):
            return 2*i+1
        else:
            return None

    def get_right_value(self, i):
        try:
            return self.heap[self.right_index(i)]
        except TypeError:
            return None

    def parent_index(self, i):
        parent_index = int(floor(i/2))
        if parent_index<self.get_len() and parent_index!=i:
            return int(floor(i/2))
        else:
            return None


    def get_parent_value(self, i):
        """Return parent"""
        try:
            self.heap[self.parent_index()]
        except TypeError:
            return None

    def max_heapify(self, i):
        left, right = self.get_left_value(i), self.get_right_value(i)
        largest = i

        if (left is not None) and (self.heap[left] > self.heap[i]):
            largest = left

        if (right is not None) and (self.heap[right] > self.heap[i]):
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
            print("Called max heapi")
            print(self.heap)


    def build_max_heap(self):
        """Builds the maimum heap binary tree from the array given"""

        self.heap_size = self._len
        i = int(floor(self._len/2))

        for i in range(int(floor(self._len/2)), 0, -1):
            self.max_heapify(i)




def main():

    my_heap = Heap(heap_array=[1, 2, 3, 5, 8, 1, 2, 3, 5, 8], heap_size=10)
    print(my_heap.get_len())

    print(my_heap.get_left_value(1))
    print(my_heap.get_right_value(1))
    print(my_heap.get_parent_value(1))

    print(2 is not None)
    my_heap.max_heapify(2)
    #my_heap.build_max_heap()

if __name__ == '__main__':
    main()