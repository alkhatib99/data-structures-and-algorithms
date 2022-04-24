from linked_list_kth.linked_list_kth import LinkedList
import pytest

def test_kthFromEnd_k_greater_length():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(5)
    assert "Index out of range" in str(exc.value)
    assert exc.type == Exception

def test_kthFromEnd_k_equal_length():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(4)
    assert "Index out of range" in str(exc.value)
    assert exc.type == Exception

def test_kthFromEnd_k_less_zero():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(-5)
    assert "k must be non-negative number" in str(exc.value)
    assert exc.type == Exception


def test_kthFromEnd_size_1():
    expected=1
    ll=LinkedList()
    ll.insert(1)
    actual=ll.kthFromEnd(0)
    assert actual==expected

def test_kthFromEnd_happy_path():
    expected=8
    ll=LinkedList()
    
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)
    actual=ll.kthFromEnd(2)
    assert actual==expected