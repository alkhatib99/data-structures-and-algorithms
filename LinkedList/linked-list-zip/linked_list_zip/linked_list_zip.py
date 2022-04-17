

from LinkedList.linkedlist.linked_list.linked_list import LinkedList, Node


def zip_linked_list(list1, list2):
    '''
    Merge two linked lists

    Input : two linked lists 
    Output : new linked list from merging the old lists
    '''
    # Long_len : the length of longest one 
    # first : the first list if it wasn't empty
    long_len= len(list1) if len(list1)>len(list2) else len(list2)
    list1,list2=list1.head,list2.head
    if not list1 and not list2:
        raise Exception("There is no lists to zip")
    elif not list1:
        return str(list2)
    elif not list2:
        return str(list1)

    new = LinkedList()

    while list1 or list2:
        if list1:
            new.insert(list1.value)
            list1=list1.next
        if list2:
            new.insert(list2.value)
            list2=list2.next
    return (new.__str__)


def print_linked_list(root):
    current = root.head
    temp = ''
    while current:
        print(current.val)
        temp = temp + str(current.val) + ' '
        current = current.next
    return temp


if __name__=="__main__":

    ll_1 = LinkedList(Node(1))
    ll_1.head.next = Node(2)
    ll_1.head.next.next = Node(3)

    ll_2 = LinkedList(Node('A'))
    ll_2.head.next = Node('B')
    ll_2.head.next.next = Node('C')
    zip_linked_list(ll_1, ll_2)
    print_linked_list(ll_1)
