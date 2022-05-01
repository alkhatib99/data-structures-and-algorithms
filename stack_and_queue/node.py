class Node:
    """
    The Node class has two properities for the va;ue stored in the node and pointer to next node
    """
    def __init__(self,value):
        """
        The initialization of the Node class
        """
        self.data =value
        self.next = None