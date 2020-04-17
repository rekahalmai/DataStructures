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

    def __call__(self, *args, **kwargs):
        return


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
        print("added first node")


    def insert_node_at_end(self, node):
        _node = node
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        _node.previous = current_node
        _node.next = None
        current_node.next = _node

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
            current_node.data, current_node.previous, current_node.next = None, None, None
            #current_node.previous, current_node.data = None, None
            self._len -= 1


    def create_node_value_list(self):
        current_node = self.head
        node_value_list = []
        while current_node is not None:
            node_value_list.append(current_node.data)
            current_node = current_node.next
        return node_value_list


    def print_values(self):
        node_value_list = self.create_node_value_list()
        print(node_value_list)

    def search_value_in_list(self, value):
        """"""
        current_node = self.head
        results = []
        while current_node is not None:
            if current_node.data == value:
                print(f"Found the value {value} at node {current_node}")
                results.append(current_node)
                current_node = current_node.next
            else:
                current_node = current_node.next
        print(results)
        return results


    def delete_value(self, value):
        """ Delete the nodes that have the same value as value """
        current_node, previous_node = self.head, self.head

        while current_node.next is not None:
            if current_node.data == value:
                print(f"Found the value {value} at node {current_node}")
                previous_node.next = current_node.next
                current_node =current_node.next
                self._len -= 1
            else:
                previous_node = current_node
                current_node = current_node.next




def main():
    node1 = Node("H")
    node2 = Node("I")
    node3 = Node("T")
    node4 = Node("H")
    node5 = Node("E")
    node6 = Node("R")
    node7 = Node("E")

    dl_list = LinkedList()
    dl_list.add_node(node1)
    dl_list.add_node(node2)
    dl_list.add_node(node3)
    dl_list.add_node(node4)
    dl_list.add_node(node5)
    dl_list.add_node(node6)
    dl_list.add_node(node7)
    dl_list.print_values()

    dl_list.delete_first_node()
    dl_list.print_values()

    dl_list.delete_last_node()
    dl_list.print_values()

    dl_list.delete_value('E')
    dl_list.print_values()


if __name__ == "__main__":
    main()
