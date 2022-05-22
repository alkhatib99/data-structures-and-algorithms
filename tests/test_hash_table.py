from hash_table.hash_table import HashTable
import pytest



def test_hash_table_hash():
    expected = 586
    hashtable=HashTable()
    actual = hashtable.hash("r")
    assert actual == expected


def test_hash_table_hash_word():
        expected = 40
        hashtable=HashTable()
        actual = hashtable.hash("dd")
        assert actual == expected


def test_hash_table_set():
    hashtable=HashTable()
    expected = "40"
    hashtable.set("abood","40")
    actual = hashtable.get("abood")
    assert actual == expected

def test_hash_table_get():
    hashtable=HashTable()
    expected = "Pythonic"
    hashtable.set("py","Pythonic")
    actual = hashtable.get("py")
    assert actual == expected

def test_hash_table_get_null():
    hashtable=HashTable()
    expected = "None"
    actual = hashtable.get("flower")
    assert actual == expected

def test_hash_table_handle_collision():
    hashtable=HashTable()
    expected = "10"
    hashtable.set("abood","10")
    hashtable.set("abood","10")
    actual = hashtable.get("abood")
    assert actual == expected

def test_hash_table_get_value_within_collision():
    hashtable=HashTable()
    expected = "11"
    hashtable.set("dd","11")
    hashtable.set("dd","15")
    actual = hashtable.get("dd")
    assert actual == expected