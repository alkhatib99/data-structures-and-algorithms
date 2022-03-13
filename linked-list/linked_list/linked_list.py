class LinkedList:
    """
    This is the LinkedList class
    """

    def __init__(self):
        """
        This is the initialization of the linked list
        """
        self.head = None

    def insert (self,value):
        """
        Inserts node into the beginning of the linked list (not append)
        """
        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node

    def includes(self,value):
        """
        Returns true if node with value is in linked list. Otherwise returns false
        """
        if self.head  is not None :
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False


    def to_string(self):
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> '
                current = current.next
            data_str += 'NULL'
            return data_str
    def __str__(self):
        string = ""
        current_node = self.head

        while current_node:
            string += (f"{ {current_node.value} }->")
            current_node = current_node.next
        
        string += "None"
        return string




class Node:
    """
    This is the Node class
    """
    def __init__(self,value):
        """
        This is the initialization of the Node class
        """
        self.value =value
        self.next = None