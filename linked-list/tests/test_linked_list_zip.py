from linked_list_zip.linked_list_zip import LinkedList,Node
from linked_list_zip.linked_list_zip import zip_linked_list, print_linked_list
import pytest

def test_functions_exist():
    assert Node
    assert LinkedList
    assert zip_linked_list
    assert print_linked_list


def test_zip():
    LinkedList_1 = LinkedList()
    LinkedList_1.head=(Node(1))
    LinkedList_1.head.next = Node(2)
    LinkedList_1.head.next.next = Node(3)

    LinkedList_2 = LinkedList()
    LinkedList_2.head=(Node('A'))
    LinkedList_2.head.next = Node('B')
    LinkedList_2.head.next.next = Node('C')
    actual = zip_linked_list(LinkedList_1, LinkedList_2).__str__()
    excpected="{1}->{'A'}->{2}->{'B'}->{3}->{'C'}->None"
    assert actual == excpected


def test_zip_short_1():
    LinkedList_1 = LinkedList()
    LinkedList_1.head=Node(1)
    LinkedList_1.head.next = Node(2)

    LinkedList_2 = LinkedList()
    LinkedList_2.head=Node('A')
    LinkedList_2.head.next = Node('B')
    LinkedList_2.head.next.next = Node('C')
    actual=zip_linked_list(LinkedList_1, LinkedList_2).__str__()
    excpected = "{1}->{'A'}->{2}->{'B'}->{'C'}->None"
    assert actual == excpected

def test_zip_short_2():
    LinkedList_1 = LinkedList()
    LinkedList_1.head=Node(1)
    LinkedList_1.head.next = Node(2)
    LinkedList_1.head.next.next = Node(3)

    LinkedList_2 = LinkedList()
    LinkedList_2.head=Node('A')
    LinkedList_2.head.next = Node('B')
    actual = zip_linked_list(LinkedList_1, LinkedList_2).__str__()
    excpected="{1}->{'A'}->{2}->{'B'}->{3}->None"
    assert actual == excpected