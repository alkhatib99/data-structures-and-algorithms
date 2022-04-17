from stack_and_queue.node import Node

class Queue:
    """
     Queue class has two properities  

    Attribute:

    front -> the first Node of the queue.
    rear ->  the last Node of the queue.

    """
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        Method to adds a new node with that value to the back of the queue
        """
        node = Node(value)
        if not self.rear:
           self.front = node
           self.rear= node
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        Method to removes the node from the front of the queue
       Return the value of front node 
        """
        if not self.front :
            raise Exception("You can't dequeue from empty Queue !!!")
        else :
            temp = self.front
            self.front = self.front.next
            temp.next = None

        return temp.data

    def peek(self):
        """
        view the value of the front Node in the queue,
            Return the value of the front node
        """
        if not self.front :
            raise Exception("Empty Queue !!!")
        else :
            return self.front.data

    def is_empty(self):
        """
                Method to check if the stack is empty, Return true if is it empty, otherwise return false

        """
        if not self.front:
            return True
        return False