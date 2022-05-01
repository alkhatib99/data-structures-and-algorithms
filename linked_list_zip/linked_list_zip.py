

from linked_list.linked_list import LinkedList, Node

def zip_linked_list(list1, list2):
    '''
    Merge two linked lists

    Input : two linked lists 
    Output : new linked list from merging the old lists
        '''
    first = list1.head
    second = list2.head

    if not first and not second:
        return "There is no lists to zip"
    elif not first:
        return list2.__str__()

    elif not second:
        return first.__str__()
    
    new_ll=LinkedList()
    while first or second:
        if first:
            new_ll.insert(first.value)
            first=first.next
        if second:
            new_ll.insert(second.value)
            second=second.next
    return new_ll

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
