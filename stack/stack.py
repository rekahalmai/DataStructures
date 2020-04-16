
class Stack:
    """
    Basic Stack class.
    Assume that the stack can hold max_size number of items and can
    hold any type of items.

    _size()    - returns the size of stack
    is_empty() - returns boolean whether stack is empty
    is_full()  - returns boolean whether stack is full
    pop()      - drop last element of stack
    push()     - add new_item to stack
    peek()     - look at last element of stack
    """

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.array = []

    def _size(self):
        """ Returns the size of the stack. Bounded by max_size."""
        return len(self.array)

    def is_empty(self):
        """ Returns True if the stack is empty and False if it is not"""
        return self._size() == 0

    def is_full(self):
        """Returns True if the stack is full and False if it is not"""
        return self._size() == self.max_size

    def pop(self):
        """ Removes the last added item in the stack """
        if self.is_empty():
            return IndexError("No elements in stack, can't pop element.")
        else:
            last_item = self.array.pop()
            return last_item

    def push(self, new_item):
        """ Adds an element to the stack"""
        if self.is_full():
            return IndexError("Stack is full, can't add element")
        else:
            self.array.append(new_item)
            return

    def peek(self):
        """ Returns the last element of the stack. """
        return self.array[self._size() - 1]

def create_stack(create_own=True, n_max=10):
    """
    Creates a stack with n_max number of elements.
    If create_own, we input all elements to the stack and choose to push or pop elements.
    Else add and pop randomly.

    :param create_own: Boolean, if True, needs to input all element
    :return: Stack object
    """

    if create_own:
        n_max = int(input("Max number of elements in stack: "))

        my_stack = Stack(n_max)

        no_more_element = False
        while not no_more_element:
            element = input("Type new element")
            my_stack.push(element)
            print(my_stack.array)
            no_more_element = bool(input("Add element? Enter for yes, any key for no more element."))

        drop_no_more_element = False
        while not drop_no_more_element:
            my_stack.pop()
            print(my_stack.array)
            drop_no_more_element = bool(input("Pop an element? Enter for yes, any key for no more pop."))

    else:
        import random
        my_stack = Stack(n_max)

        for p in range(n_max):
            my_stack.push(random.randrange(1, 100))

        for p in range(n_max+1):
            my_stack.pop()
        print(my_stack.array)

    print(my_stack.array)
    return my_stack


if __name__ == "__main__":
    my_stack_instance = create_stack(True)

