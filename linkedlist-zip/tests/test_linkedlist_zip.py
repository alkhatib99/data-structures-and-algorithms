

from linkedlist_zip.ll_zip import Node, LL, zip_two_ll, print_ll
import pytest

def test_functions_exist():
    assert Node
    assert LL
    assert zip_two_ll
    assert print_ll


def test_zip():
    ll_1 = LL(Node(1))
    ll_1.head.next = Node(2)
    ll_1.head.next.next = Node(3)

    ll_2 = LL(Node('A'))
    ll_2.head.next = Node('B')
    ll_2.head.next.next = Node('C')
    zip_two_ll(ll_1, ll_2)
    assert print_ll(ll_1) == '1 A 2 B 3 C '


def test_zip_short_1():
    ll_1 = LL(Node(1))
    ll_1.head.next = Node(2)

    ll_2 = LL(Node('A'))
    ll_2.head.next = Node('B')
    ll_2.head.next.next = Node('C')
    zip_two_ll(ll_1, ll_2)
    assert print_ll(ll_1) == '1 A 2 B C '


def test_zip_short_2():
    ll_1 = LL(Node(1))
    ll_1.head.next = Node(2)
    ll_1.head.next.next = Node(3)

    ll_2 = LL(Node('A'))
    ll_2.head.next = Node('B')
    zip_two_ll(ll_1, ll_2)
    assert print_ll(ll_1) == '1 A 2 B 3 '