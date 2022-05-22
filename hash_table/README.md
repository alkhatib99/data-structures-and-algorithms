# Hash Table

Hashtable is a type of data structure, that stores data as (key, value) pairs.
 This means every Node or Bucket has both a key and a value. 

 Hashing can also be defined as a technique that is used to uniquely identify a specific object from a group of similar objects.

## Challenge

Implements the hashtable data structure and the following methods.
**set**, **get**, **contains**, **hash**

## Approach & Efficiency

An array was the chosen data structure to use for the HashTable and a linked list was the chosen data structure to use at each index of the Hash Table to handle collisions.

Adding key/value pairs and getting values from the Hash Table is essentially O(1) for time for both posting and getting. 
Big O is always looking for the worst-case scenario. The worst case would be the length of the linked list at any given index. Say one index had 5 collisions, the Big O for time would be O(5) in that case time.

## API

**set**:<br/>
>Arguments: key, value .<br/>
>Returns: Nothing this method should hash the key, and set the key and value pair in the table, handling collisions as needed. Should a given key already exist, replace its value from the value argument given to this method.

**get**:<br/>
>Arguments: key. <br/>
>Returns: Value associated with that key in the table

**contains**:<br/>
>Arguments: key. <br/>
>Returns: Boolean, indicating if the key exists in the table already

**hash**:<br/>
>Arguments: key.<br/>
>Returns: Index in the collection for that key