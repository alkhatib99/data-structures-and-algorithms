class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LL:
    def __init__(self, head=None):
        self.head = head


def zip_two_ll(list1, list2):
    '''
    Merge two linked lists

    Input : two linked lists 
    Output : new linked list from merging the old lists
    '''
    current_1 = list1.head
    current_2 = list2.head
    while current_1 and current_2:
        temp_1 = current_1.next
        temp_2 = current_2.next
        current_1.next = current_2
        if temp_1:
            current_2.next = temp_1
        current_1 = temp_1
        current_2 = temp_2


def print_ll(root):
    current = root.head
    temp = ''
    while current:
        print(current.val)
        temp = temp + str(current.val) + ' '
        current = current.next
    return temp


if __name__=="__main__":
    ll_1 = LL(Node(1))
    ll_1.head.next = Node(2)
    ll_1.head.next.next = Node(3)

    ll_2 = LL(Node('A'))
    ll_2.head.next = Node('B')
    ll_2.head.next.next = Node('C')
    zip_two_ll(ll_1, ll_2)
    print_ll(ll_1)
