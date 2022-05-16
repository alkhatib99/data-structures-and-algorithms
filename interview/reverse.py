from linked_list.linked_list import LinkedList
from linked_list_insertion.linked_list_insertion import append
from stack_and_queue.stack import Stack
def reverse(list):
    head=list.head
    if head is None :
        return None

    new_list=LinkedList()
    temp=Stack()
    while head:
        temp.push(head.value)
        head=head.next
    while not (temp.is_empty()):
        append(new_list,temp.pop())

    return new_list


LinkedList.reverse=reverse

if __name__=="__main__":

    ll=LinkedList()
    append(ll,1)
    append(ll,2)
    append(ll,3)
    append(ll,4)
    append(ll,5)
    
    print(ll)

    print(reverse(ll))