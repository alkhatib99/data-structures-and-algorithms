from  stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest

def test_enqueue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.stack2.top.data
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_dequeue_with_one_node():
    q = PseudoQueue()
    q.enqueue("apple")
    q.dequeue()
    actual = q.stack2.top
    expected = None
    assert actual == expected


# @pytest.mark.skip("pending")
def test_enqueue_two():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.stack2.top.data
    expected = "bananas"
    assert actual == expected


def test_dequeue_when_empty():
    q = PseudoQueue()
    with pytest.raises(Exception) as e:
        q.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"


def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("pending")
def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.stack1.top.data
    expected = "bananas"
    assert actual == expected