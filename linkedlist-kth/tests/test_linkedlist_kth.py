from linkedlist_kth import __version__
from linkedlist_kth.linkedlist_kth import linkedList
import pytest
def test_version():
    assert __version__ == '0.1.0'


def test_kthFromEnd_k_greater_length():
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(5)
    assert "Index out of range" in str(exc.value)
    assert exc.type == Exception

#@pytest.mark.skip('todo')
def test_kthFromEnd_k_equal_length():
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(4)
    assert "Index out of range" in str(exc.value)
    assert exc.type == Exception

#@pytest.mark.skip('todo')
def test_kthFromEnd_k_less_zero():
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)

    with pytest.raises(Exception) as exc:
        actual=ll.kthFromEnd(-5)
    assert "k must be non-negative number" in str(exc.value)
    assert exc.type == Exception


#@pytest.mark.skip('todo')
def test_kthFromEnd_size_1():
    expected=1
    ll=linkedList()
    ll.insert(1)
    actual=ll.kthFromEnd(0)
    assert actual==expected

#@pytest.mark.skip('todo')
def test_kthFromEnd_happy_path():
    expected=8
    ll=linkedList()
    ll.insert(1)
    ll.insert(8)
    ll.insert(3)
    ll.insert(2)
    actual=ll.kthFromEnd(2)
    assert actual==expected