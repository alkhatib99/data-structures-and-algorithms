from curses import echo
from array.array_reverse.array_reverse.array_reverse import reverse_array
from array_reverse import __version__

def test_array_even_reverse():
    actual=[3,5,6,7]
    expected=[7,6,5,3]
    actual=reverse_array(actual)
    assert actual == expected

def test_array_odd_reverse():
    actual=(reverse_array([1,5,7,8,6]))
    expected=[6,8,7,5,1]
    assert actual==expected

def test_array_empty_reverse():
    actual=(reverse_array([]))
    expected=[]
    assert actual==expected
