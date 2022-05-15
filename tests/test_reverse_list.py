from hashlib import new
import pytest
from interview.reverse import reverse

from linked_list.linked_list import Node, LinkedList

from linked_list_insertion.linked_list_insertion import append


def test_none_head():
    ll=LinkedList()
    ll.head=None
    actual = reverse(ll)
    expect = None
    assert actual == expect

def test_reverse_single_element():
    ll=LinkedList()
    append(ll,1)
    actual=reverse(ll).__str__()
    ll2=LinkedList()
    append(ll2,1)
    excpected = ll2.__str__()
    assert excpected == actual
    
    


def test_reverse_list_int():
    ll=LinkedList()
    append(ll,1)
    append(ll,2)
    append(ll,3)
    append(ll,4)
    append(ll,5)

    rev_ll=LinkedList()
    append(rev_ll,5)
    append(rev_ll,4)
    append(rev_ll,3)
    append(rev_ll,2)
    append(rev_ll,1)
    excpected=rev_ll.__str__()
    actual=reverse(ll).__str__()

    assert actual == excpected

def test_reverse_list_string():
    l1=LinkedList()
    l2=LinkedList()
    #insert element into list 1 
    append(l1,'1')
    append(l1,'2')
    append(l1,'3')
    append(l1,'4')
    append(l1,'5')
    actual =reverse(l1).__str__()
    #insert element into list 2
    append(l2,'5')
    append(l2,'4')
    append(l2,'3')
    append(l2,'2')
    append(l2,'1')
    excpected=l2.__str__()

    assert actual == excpected