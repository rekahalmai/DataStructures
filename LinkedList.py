# Linked list is a data structure in which objects are arranged in a linear order. This linear order is
# determined by a pointer in each object. -> Linked lists provide a flexible representation for dynamic sets.

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next
        return

    def get_next(self):
        return self.next

    def is_last(self):
        return self.next != None

    def set_previous(self, previous):
        self.previous = previous
        return

    def get_previous(self):
        return self.previous

    def is_start(self):
        return self.previous == None


class LinkedList():

    def __init__(self):
        self._len = 0
        self.head = None
        # self.current_node = None


    def add_node(self, node):
        if self._len == 0:
            pass
        else:
            pass


    def add_first_node(self, node):
        _node = node
        _node.previous, _node.next = None, None
        self.current_node = _node
        self.head = _node
        self._len += 1


    def add_node_last(self, node):
        _node = node
        _node.previous = self.current_node
        _node.next = None
        self.current_node = _node

