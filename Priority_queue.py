
from Heap import Heap

class PriorityQueueNode():
    """Node object of the priority queue, containing some data and the priority_key (higher -> more important)"""
    def __init__(self, data, priority_key):
        self.data = data
        self.priority_key = priority_key

class PriorityQueue(Heap):
    """Implementation of maximum heap used as a Priority Queue. Its elements are PriorityQueueNodes.
    The Priority queue satisfies the maximum heap property with regards to the priority key of its nodes:
    no node can have a higher priority than its parent node. """


    def heap_max(self):
        """Return maximum priority node. Running time: O(n lgn) because of the build_max function."""
        self.build_max_heap()
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
        """Extract and delete the node with the maximum priority key. Running time: O(lg n) """
        _max = self.heap_max()
        self.heap_size = self.get_len()
        self.heap[0] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(0)
        return _max


    def heap_increase_key(self, i, key):
        """Increase the priority key to the element at the ith index. If the new key is smaller then the
        initial key, return.
        Running time: O(lg n)"""
        if key < self.heap[i].priority_key:
            print("The new key should be higher than the current priority_key ")
        else:
            self.heap[i].priority_key = key
            while i > 0 and self.heap[(i-1)//2].priority_key < self.heap[i].priority_key:
                self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
                i = (i-1)//2

    def max_heap_insert(self, new_node):
        """Insert a new node (PriorityQueueNode) and change Priority queue to satisfy max heap
        property. Running time: O(lg n)"""
        changed_node = PriorityQueueNode(new_node.data, float("-inf"))
        self.insert_at_end(changed_node)
        self.heap_increase_key(self.heap_size-1, new_node.priority_key)


    def insert_at_end(self, new_node):
        """Insert new_node (PriorityQueueNode) to the end of the priority queue"""
        self.heap.append(new_node)
        self.heap_size += 1


    def list_elements(self):
        """Create a list of the nodes. """
        return [(v.data, v.priority_key) for v in self.heap]


def main():
    """Example usage of the heap object."""
    first_element = PriorityQueueNode("first_element", 1)
    second_element = PriorityQueueNode("second_element", 2)
    third_element = PriorityQueueNode("third_element", 3)
    fourth_element = PriorityQueueNode("fourth_element", 4)
    fifth_element = PriorityQueueNode("fifth_element", 5)

    my_priority_queue = PriorityQueue([first_element, second_element, third_element, fourth_element, fifth_element])

    print(f"Initial priority queue: {my_priority_queue.list_elements()}")
    my_priority_queue.build_max_heap()
    print(f"My priority queue after building max_heap: {my_priority_queue.list_elements()}")

    my_priority_queue.heap_increase_key(3, 9)
    print(f"My priority queue after building heap_increase_key: {my_priority_queue.list_elements()}")

    sixth_element = PriorityQueueNode("sixth_element", 195)

    my_priority_queue.max_heap_insert(sixth_element)
    print(f"My priority queue after building max_heap_insert: {my_priority_queue.list_elements()}")


if __name__ == '__main__':
    main()