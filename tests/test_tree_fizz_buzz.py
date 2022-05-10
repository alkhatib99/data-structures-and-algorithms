from tree_fizz_buzz.tree_fizz_buzz import Node, fizzbuzz,fizzbuzz_tree

def test_class_and_functions_exist():
    assert Node
    assert fizzbuzz
    assert fizzbuzz_tree


def test_fizzbuzz_tree():
    root = Node(1)
    root.add_child(2)
    root.add_child(3)
    root.add_child(4)
    root.add_child(5)
    root.children[0].add_child(6)
    root.children[1].add_child(7)
    root.children[2].add_child(8)
    root.children[3].add_child(15)
    test = fizzbuzz_tree(root)
    assert test == ['1', '2', 'fizz', 'fizz', '7', '4', '8', 'buzz', 'fizzbuzz']


def test_fizzbuzz_tree2():
    root = Node(9)
    root.add_child(1)
    root.add_child(4)
    root.children[0].add_child(15)
    root.children[0].add_child(30)
    root.children[0].add_child(4)
    root.children[1].add_child(2)
    root.children[1].add_child(7)
    root.children[1].add_child(8)
    test = fizzbuzz_tree(root)
    assert test == ['fizz', '1', 'fizzbuzz', 'fizzbuzz', '4', '4', '2', '7', '8']


def test_works_with_one_node():
    root = Node(15)
    test = fizzbuzz_tree(root)
    assert test == ['fizzbuzz']