
from Heap import Heap

class PriorityQueueNode():

    def __init__(self, data, priority_key):
        self.data = data
        self.priority_key = priority_key

class PriorityQueue(Heap):

    def heap_max(self):
        return self.heap[0]

    def max_heapify(self, i):
        """Given an array and an index, verify whether the index is well placed, that is whether the
        subarray defined by it is maximum heap. 0(lg n) complexity"""
        largest, left_index, right_index = i, 2*i+1, 2*i+2
        current_length = self.heap_size

        if (left_index < current_length) and (self.heap[left_index].priority_key  > self.heap[largest].priority_key):
            largest = left_index

        if (right_index < current_length) and (self.heap[right_index].priority_key > self.heap[largest].priority_key):
            largest = right_index

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.max_heapify(largest)
        return self.heap


    def heap_extract_max(self):
        """Running time: O(lg n) """
        _max = self.heap_max()
        self.heap_size = self.get_len()
        self.heap[0] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(0)
        return _max

    def heap_increase_key(self, i, key):
        """Running time: O(lg n)"""
        if key < self.heap[i].priority_key:
            print("The new key should be higher than the current priority_key ")
        else:
            self.heap[i].priority_key = key
            while i > 0 and self.heap[i//2].priority_key < self.heap[i//2].priority_key:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
                i = i//2

    def list_elements(self):
        return [(v.data, v.priority_key) for v in self.heap]


def main():
    """Example usage of the heap object"""

    first_element = PriorityQueueNode("first_element", 1)
    second_element = PriorityQueueNode("second_element", 2)
    third_element = PriorityQueueNode("third_element", 3)
    fourth_element = PriorityQueueNode("fourth_element", 4)
    fifth_element = PriorityQueueNode("fifth_element", 5)

    my_priority_queue = PriorityQueue([first_element, second_element, third_element, fourth_element, fifth_element])

    print(f"Initial priority queue: {my_priority_queue.list_elements()}")
    my_priority_queue.build_max_heap()
    print(f"My priority queue after building max_heap: {my_priority_queue.list_elements()}")

    my_priority_queue.heap_increase_key(2, 8)
    print(f"My priority queue after building heap_increase_key: {my_priority_queue.list_elements()}")


if __name__ == '__main__':
    main()