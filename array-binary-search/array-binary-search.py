def binary_search(arr,key):
    high=len(arr)-1
    low=0
    mid=0
    while low<=high:
        mid=(high+low)//2
        if arr[mid] < key :
            low=mid+1
        elif arr[mid] > key:
            high=mid+1
        else:
            return mid

    return -1



arr=[2,3,4,10,40]
x=10
resault=binary_search(arr,x)
if resault != -1:
    print(f"Elemnt found in index:{resault}")
else:
    print("Element not found")