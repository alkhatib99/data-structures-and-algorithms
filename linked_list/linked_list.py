


class Node:
    """
    The Node class
    """
    def __init__(self,value):
        """
        The initialization of the Node class
        """
        self.value =value
        self.next = None

class LinkedList:
    """
    The LinkedList class
    """

    def __init__(self):
        """
        The initialization of the linked list.
        """
        self.head = None

    def insert(self, data):
        """
        Method to inserts node into the beginning of the linked list (not append).
        """
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode    
    
    def includes(self,value):
        """
        Returns true if node with value is in linked list. Otherwise returns false.
        """
        if self.head  is not None :
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False


    def to_string(self):
        """
        Return the linked list elements as a string of format:
        {fN->sN->lN->Null}
        """
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> '
                current = current.next
            data_str += 'NULL'
            return data_str
    def __str__(self):
        """
        Return the linked list elements as a string of format:
        {fN->sN->lN->None}
        """

        string = ""
        current_node = self.head

        while current_node:
            string += (f"{ {current_node.value} }->")
            current_node = current_node.next
        
        string += "None"
        return string
    
