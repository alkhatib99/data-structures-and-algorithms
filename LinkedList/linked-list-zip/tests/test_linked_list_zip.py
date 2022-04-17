from LinkedList.linkedlist.linked_list.linked_list import LinkedList, Node
from linked_list_zip.linked_list_zip import zip_linked_list, print_linked_list
from linked_list_zip import __version__
import pytest

def test_functions_exist():
    assert Node
    assert LinkedList
    assert zip_linked_list
    assert print_linked_list


def test_zip():
    LinkedList_1 = LinkedList(Node(1))
    LinkedList_1.head.next = Node(2)
    LinkedList_1.head.next.next = Node(3)

    LinkedList_2 = LinkedList(Node('A'))
    LinkedList_2.head.next = Node('B')
    LinkedList_2.head.next.next = Node('C')
    zip_linked_list(LinkedList_1, LinkedList_2)
    assert print_linked_list(LinkedList_1) == '1 A 2 B 3 C '


def test_zip_short_1():
    LinkedList_1 = LinkedList(Node(1))
    LinkedList_1.head.next = Node(2)

    LinkedList_2 = LinkedList(Node('A'))
    LinkedList_2.head.next = Node('B')
    LinkedList_2.head.next.next = Node('C')
    zip_linked_list(LinkedList_1, LinkedList_2)
    assert print_linked_list(LinkedList_1) == '1 A 2 B C '


def test_zip_short_2():
    LinkedList_1 = LinkedList(Node(1))
    LinkedList_1.head.next = Node(2)
    LinkedList_1.head.next.next = Node(3)

    LinkedList_2 = LinkedList(Node('A'))
    LinkedList_2.head.next = Node('B')
    zip_linked_list(LinkedList_1, LinkedList_2)
    assert print_linked_list(LinkedList_1) == '1 A 2 B 3 '