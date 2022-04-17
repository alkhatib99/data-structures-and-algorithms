from LinkedList.linkedlist.linked_list import LinkedList
def kthFromEnd(self,k):
    """
    This method return the node’s value that is k places from the tail of the linked list.
    argument: a number, k, as a parameter.

    """
    current =self.head
    length = 1
    while current.next:
        length += 1
        current = current.next
    current = self.head
    if k < 0:
        raise Exception("k must be non-negative number")
    elif k >= length:
        raise Exception('Index out of range')
    value = length-k-1
    for i in range(length):
        if i == value:
            result=current.value
            return result
        current = current.next

LinkedList.kthFromEnd=kthFromEnd
if __name__ =="__main__":
    print("razzan")
    ll =LinkedList()
    ll2 =LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(5)
    ll.append(7)
    print(ll.__str__())
    x=ll.kthFromEnd(0)
    print(x)
    ll2.insert(2)
    ll2.insert(4)
    ll2.insert(6)
    ll2.insert(8)
    ll2.insert(10)
    ll2.insert(12)
  





