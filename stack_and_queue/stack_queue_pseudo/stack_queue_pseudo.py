from stack_and_queue.stack import Stack


class PseudoQueue:
    """
    class will implement standard queue using Stack class
    """
    def __init__(self):
        self.front=None
        self.rear=None
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value):
        """
        This method inserts value into the PseudoQueue, using a first-in, first-out approach.
    
        """
        self.stack1.push(value)
        self.rear=self.stack1.top.data


    def dequeue(self):
        """
        This method Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        """
        if self.stack1.top:
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

            popedValue=self.stack2.pop()
            self.front=self.stack2.top
            self.stack1=Stack()
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())

            return popedValue
        else:
            raise Exception("queue is empty")

    def __str__(self):
        """
        This method to print out the queue
        """
        queue=''
        current=self.stack1.top
        while current:
            queue+="[ "+str(current.data)+" ] -> "
            current=current.next
        queue+='Null'
        return queue


if __name__=="__main__":
    pQueue=PseudoQueue()
    pQueue.enqueue(1)
    pQueue.enqueue(3)
    pQueue.enqueue(5)
    pQueue.enqueue(7)

    print(str(pQueue))
    print(pQueue.rear)
    pQueue.dequeue()
    print(str(pQueue))
    print(pQueue.front)
