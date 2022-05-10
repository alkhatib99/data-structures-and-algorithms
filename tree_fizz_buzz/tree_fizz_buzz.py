
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(Node(child))


def fizzbuzz_tree(root, arr=None):
    if arr == None:
        arr = []
    if root:
        arr.append(fizzbuzz(root.value))
        if root.children:
            for i in root.children:
                fizzbuzz_tree(i, arr)
    return arr


def fizzbuzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'
    return str(number)
