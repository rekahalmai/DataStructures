
class Stack:
    """
    Basic Stack class.
    Assume that the stack can hold max_size number of items.
    """

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.array = []

    def stack_size(self):
        return len(self.array)

    def is_empty(self):
        return self.stack_size() == 0

    def is_full(self):
        return self.stack_size() == self.max_size

    def pop(self):
        if self.is_empty():
            print("Underflow, can't drop.")
            return None
        else:
            last_item = self.array.pop()
            return last_item

    def push(self, new_item):
        if self.is_full():
            print("Overflow, can't add.")
        else:
            self.array.append(new_item)



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

