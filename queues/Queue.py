
class Queue:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.array = [None] * self.max_size
        self.head = 0
        self.tail = 1
        self.size = 0

    def is_empty(self):
        """ Returns True if the queue is empty and False if it is not"""
        return self.size == 0

    def is_full(self):
        """ Returns True if the queue is full and False if it is not full"""
        return self.size == self.max_size


    def peek(self):
        """ Returns first element of the queue """
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.array[self.head]


    def enqueue(self, new_element):
        """ Adds an element to the end of the queue """

        if self.is_full():
            print("Queue is full")
            return
        else:
            self.array[self.tail] = new_element
            if self.tail == self.max_size-1:
                self.tail = 0
            else:
                self.tail += 1
            self.size += 1
            print(self.array)
            return self.array


    def dequeue(self):
        """ Drops the first element of the queue and returns the changed queue"""
        if self.is_empty():
            print("No items in the queue, can't remove.")
            return
        else:
            self.array[self.head] = None
            if (self.head == self.max_size-1) and (self.tail == 0):
                self.head = 0
                self.tail = 1
            elif (self.head == self.max_size-1) and (self.tail != 0):
                self.head = 0
            else:
                self.head += 1
            self.size -= 1
            print(self.array, self.size)
            return self.array


def main():
    my_queue = Queue()
    print(my_queue.is_empty())

    for i in range(my_queue.max_size):
        my_queue.enqueue(2)
    for i in range(int(my_queue.max_size/2)):
        my_queue.dequeue()

    print(my_queue)


if __name__ == "__main__":
    main()
