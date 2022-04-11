from array_reverse import __version__
from array_reverse.array_reverse import reverse_array

def test_array_reverse():
    actual=[3,5,6,7]
    expected=[7,6,5,3]
    actual=reverse_array(actual)
    assert actual == expected
