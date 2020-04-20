
class TreeNode():

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self._size = 0

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_left(self, treeNode):
        self.left = treeNode

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_right(self, treeNode):
        self.right = treeNode

    def get_parent(self):
        return self.parent

    def set_parent(self, treeNode):
        self.parent = treeNode


class BinaryTree():

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add_treenode(self, node):
        if self.is_empty():
            self.root = node
        else:
            if 


def main():

    my_tree = BinaryTree()
    print(my_tree.is_empty())

if __name__ == "__main__":
    main()