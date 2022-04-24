from linked_list.linked_list import LinkedList
def test_Linkedlist_empty():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


def test_insert_one():
    ll = LinkedList()
    ll.insert('first')
    expected = '{first}-> NULL'
    actual = ll.to_string()
    assert expected == actual


def test_insert_multiple():
    ll = LinkedList()
    ll.insert('first')
    ll.insert(44)
    ll.insert('third')
    expected = '{first}-> {44}-> {third}-> NULL'
    actual = ll.to_string()
    assert expected == actual


def test_includes_true():
    ll = LinkedList()
    ll.insert('first')
    ll.insert('second')
    ll.insert('third')
    expected = True
    actual = ll.includes('first')
    assert expected == actual


def test_includes_false():
    ll = LinkedList()
    ll.insert('first')
    ll.insert('second')
    ll.insert('third')
    expected = False
    actual = ll.includes('fourth')
    assert expected == actual