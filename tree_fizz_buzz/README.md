# Fizz Buzz Tree

## Challenge

Write a function called FizzBuzzTree which takes a k-ary tree as an argument. Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows: If the value is divisible by 3, replace the value with “Fizz” If the value is divisible by 5, replace the value with “Buzz” If the value is divisible by 3 and 5, replace the value with “FizzBuzz” If the value is not divisible by 3 or 5, simply turn the number into a String. Return a new tree.

## Whiteboard Process

![whiteboard](whiteboard-fizz-buzz.jpg)

## Approach and Efficiency

I used a pre-order, DFS, recursive algorithm with a helper function to traverse the k-ary tree and return a new tree, as represented by a list, with fizzbuzz values inside of it.


