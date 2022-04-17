# Array

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.

## Table Of Content

- [Array](#array)
  - [Table Of Content](#table-of-content)
  - [Overview](#overview)
  - [Advantages of using arrays:](#advantages-of-using-arrays)
  - [Disadvantages of using arrays:](#disadvantages-of-using-arrays)
  - [Challenges](#challenges)
  
## Overview

The idea is to store multiple items of the same type together.
This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

For simplicity, we can think of an array of a fleet of stairs where on each step is placed a value (let’s say one of your friends).
Here, you can identify the location of any of your friends by simply knowing the count of the step they are on.
The array can be handled in Python by a module named array.
They can be useful when we have to manipulate only specific data type values.
A user can treat lists as arrays.
However, the user cannot constrain the type of elements stored in a list.
If you create arrays using the array module, all elements of the array must be of the same type. 
Remember: “Location of next index depends on the data type we use”.

## Advantages of using arrays:

Arrays allow random access to elements.
This makes accessing elements by position faster.
Arrays have better cache locality which makes a pretty big difference in performance.
Arrays represent multiple data items of the same type using a single name.

## Disadvantages of using arrays:

You can’t change the size i.e.
 once you have declared the array you can’t change its size because of static memory allocation.
 Here Insertion(s) and deletion(s) are difficult as the elements are stored in consecutive memory locations and the shifting operation is costly too.

Now if take an example of the implementation of data structure Stack using array there are some obvious flaws.
Let’s take the POP operation of the stack. The algorithm would go something like this. 

Check for the stack underflow
Decrement the top by 1
So there what we are doing is that the pointer to the topmost element is decremented means we are just bounding our view actually that element stays there taking up of the memory space. If you have any primitive datatype then it might be ok but the object of an array would take a lot of memory.

## Challenges

- [Array Reverse](./array-reverse/README.md).
- [Array Insert Shift](./array-insert-shift/README.md).
- [Array Binary Search](./array-binary-search/README.md).