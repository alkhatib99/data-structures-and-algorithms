from LinkedList.linkedlist.linked_list import LinkedList, Node

def __contains__(self,value):
    """
    This method search in the linked list for a given value , and 
        return True if the value exist and return False not exist
    """
    if self.head==None:
        return False
    else:
        x= self.head
        while x != None:
            if x.value==value:
                return True
            x=x.next
        return False
LinkedList.__contains__=__contains__

def append(self,value):
    """
    this method to add nodes in the end of the list
    """
    node=Node(value)
    currentNode=self.head
    if currentNode:
        while currentNode.next:
            currentNode=currentNode.next
        currentNode.next=node
    else:
        self.head=node
LinkedList.append=append
def insert_before(self,value, newValue):
    """
    adds a new node with the given new value immediately before the first node that has the value specified
    """
    if self.head is None:
        print("List has no element")
        return

    if value == self.head.value:
        new_node = Node(newValue)
        new_node.next = self.head
        self.head = new_node
        return

    n = self.head
    print(n.next)
    while n.next is not None:
        if n.next.value == value:
            break
        n = n.next
    if n.next is None:
        print("item not in the list")
    else:
        new_node = Node(newValue)
        new_node.next = n.next
        n.next = new_node

LinkedList.insert_before=insert_before
def insert_after(self,value,newValue):
    """
    adds a new node with the given new value immediately after the first node that has the value specified
    """
    if self.head is None:
        print("List has no element")
        return
    n = self.head
    print(n.next)
    while n is not None:
        if n.value == value:
            break
        n = n.next
    if n is None:
        print("item not in the list")
    else:
        new_node = Node(newValue)
        new_node.next = n.next
        n.next = new_node
LinkedList.insert_after=insert_after
if __name__ =="__main__":
    print("Abood")
    ll =LinkedList()

    ll2 =LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(5)
    ll.append(7)
    print(ll.__str__())
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)
    ll2.insert(8)
    ll2.insert(10)
    ll2.insert(12)
    ll.insert_after(3,7)
    print(ll.__str__())
    ll.insert_before(3,5)
    print(ll.__str__())





