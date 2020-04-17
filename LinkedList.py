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


    def list_len(self):
        return self._len


    def add_node(self, node):
        if self._len == 0:
            self.add_first_node(node)
        else:
            self.insert_node_at_end(node)


    def add_first_node(self, node):
        _node = node
        _node.previous, _node.next = None, None
        self.head = _node
        self._len += 1


    def insert_node_at_end(self, node):
        _node = node

        current_node = self.head()
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = _node

        _node.previous = current_node
        _node.next = None

        self._len += 1


    def delete_first_node(self):
        if self._len == 0:
            print("Double linked list is empty, cannot delete.")
        else:
            self.head = self.head.next
            self._len -= 1


    def delete_last_node(self):
        if self._len == 0:
            print("Double linked list is empty, cannot delete.")
        else:
            current_node, previous_node = self.head, self.head

            while current_node.next is not None:
                current_node = current_node.next
                previous_node = current_node
            previous_node.next = None
            self._len -= 1


    def create_node_value_list(self):

        current_node = self.head
        node_value_list = []
        while current_node is not None:
            node_value_list.append(current_node.data)
            current_node = current_node.next
        return node_value_list


    def print_values_in_list(self):
        node_value_list = self.create_node_value_list()
        print(node_value_list)
        return

    def search_value_in_list(self, value):
        current_node = self.head
        results = []
        while current_node is not None:
            if current_node.value == value:
                print(f"Found the value {value} at node {current_node}")
                results.append(current_node)

        return results


    def delete_value(self, value):
        current_node, previous_node = self.head, self.head

        while current_node is not None:
            if current_node.value == value:
                previous_node.next = current_node.next
