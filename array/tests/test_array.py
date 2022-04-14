from array import __version__

from array.array_reverse.array_reverse import reverse_array


def test_version():
    assert __version__ == '0.1.0'
def test_array_reverse():
    actual=[3,5,6,7]
    expected=[7,6,5,3]
    actual=reverse_array(actual)
    assert actual == expected
