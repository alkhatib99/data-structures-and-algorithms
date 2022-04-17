from linked_list_insertion import __version__

from linked_list_insertion.linked_list_insertion import LinkedList

def test_append_node():
    expected ="{ 5 } -> { 7 } -> NULL"
    ll = LinkedList()
    ll.insert(5)
    ll.append(7)
    actual= ll.__str__()
    assert actual == expected


def test_append_many_nodes():
    expected ="{ 1 } -> { 2 } -> { 3 } -> NULL"
    ll = LinkedList()
    ll.insert(1)
    ll.append(2)
    ll.append(3)
    actual= str(ll)
    assert actual == expected

def test_insert_before_first_node():
    expected="{ 1 } -> { 2 } -> { 3 } -> NULL"
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert_before(2,1)
    actual= ll.__str__()
    assert actual==expected

def test_insert_before_middle_node():
    expected ="{ 5 } -> { 1 } -> { 3 } -> NULL"
    ll = LinkedList()
    ll.insert(5)
    ll.insert(3)
    ll.insert_before(3,1)
    actual= str(ll)
    assert actual == expected

def test_insert_before_empty_list():
    expected ="NULL"
    ll = LinkedList()
    ll.insert_before(7,1)
    actual= str(ll)
    assert actual == expected

def test_insert_after_list_empty():
    expected =None
    ll = LinkedList()
    actual= ll.insert_after(3,7)
    assert actual == expected

def test_insert_after_middle_node():
    expected ="{ 5 } -> { 10 } -> { 17 } -> NULL"
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert_after(10,17)
    actual= str(ll)
    assert actual == expected

def test_insert_after():
    expected ="{ 5 } -> { 17 } -> { 10 } -> { 20 } -> NULL"
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(20)
    ll.insert_after(5,17)
    actual= str(ll)
    assert actual == expected
