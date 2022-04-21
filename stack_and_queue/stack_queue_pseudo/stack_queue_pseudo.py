from stack_and_queue.stack import Stack


class PseudoQueue:
    """
    class will implement standard queue using Stack class
    """
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value):
        """
        This method inserts value into the PseudoQueue, using a first-in, first-out approach.
    
        """
        # res=''
        while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        self.stack2.push(value)

    def dequeue(self):
        """
        Method that extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        """

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        if self.stack1.is_empty():
            raise Exception("Method not allowed on empty collection")

        return self.stack1.pop()  


if __name__=="__main__":
    pQueue=PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(3)
    pQueue.enqueue(5)
    pQueue.enqueue(7)

    print(str(pQueue))
    pQueue.dequeue()
    print(str(pQueue))
