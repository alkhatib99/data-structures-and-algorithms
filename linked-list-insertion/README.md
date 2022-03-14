# Link List - Append,Insert before, Insert After

Write methods that appends an node to the end of the link list, inserts a new node before a specific value and one that inserts a new node after a specific value.

[THE-PR](https://github.com/alkhatib99/data-structures-and-algorithms/pull/11)

---

## Challenge

- `.append(value)` which adds a new node with the given `value` to the end of the list
- `.insertBefore(value, newVal)` which add a new node with the given `newValue` immediately before the first `value` node
- `.insertAfter(value, newVal)` which add a new node with the given newValue immediately after the first value node

### Approach & Efficiency

Use while loops to traverse through the link list till position is found to insert the new link list

Time complexity: O(n), linear. The larger the linked list the more time it will take to traverse it
Space complexity: 0(1), we are not creating any new data structures

## Whiteboard Process

!['WhiteBoard for linked-list-insert'](./linked-list-insertion.jpg)

---
