from stack_and_queue.node import Node
class Stack:
    """
    Stack class has one properity top of the stack
    """
    def __init__(self):
        self.top=None

        
    def push(self,value):
        """ 
       Method to  adds a new node with that value to the top of the stack
       
        """
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        """ 
        Removes the node from the top of the stack,
         return the data of the node
        """
        if not self.top:
            raise Exception("You can't pop from Empty Stack !!!")
        else:
            tmp=self.top
            self.top=self.top.next
            tmp.next=None
        return tmp.data

    def peek(self):
        """
        Method to  view the top value, Return a top stack without remove it 
        """
        if not self.top:
            raise Exception("You can't peek from Empty Stack !!!")
        else:
            return self.top.data


    def is_empty(self):
        """
        Method to check if the stack is empty, Return true if is it empty, otherwise return false
        """
        if not self.top:
            return True
        else:
            return False
