from array_binary_search import __version__
from array_binary_search import binary_search

def test_array_binary_search():
    arr=[4,5,6,10]
    actual = binary_search(arr,6)
    expected  = 2
    assert actual == expected

    

