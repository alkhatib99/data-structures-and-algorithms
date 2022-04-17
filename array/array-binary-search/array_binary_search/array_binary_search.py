def binary_search(arr,key):
    
    """
    Function return the index of the search ky if found it,
    or -1  if didn't found it 
    """
    
    index_mid=ceil(len(arr)/2)
    
    mid=arr[index_mid]
    high=arr[len(arr)-1]
    low=arr[0]
    if key == high:
        return (len(arr)-1)
    elif key == low :
        return 0
    elif key == mid :
        return index_mid
    elif key > mid:
        for i in range(index_mid,len(arr)-1):
            if(arr[i]==key):
                return i
    elif key< mid:
        for i in range(index_mid,0,-1):
            if(arr[i]== key):
                return i        
    return -1
    
def ceil(num):
    floor = int(num)
    if floor != num :
     return floor +1
    else :
        return floor

arr=[2,3,4,10,40]
x=10
resault=binary_search(arr,x)
if resault != -1:
    print(f"Elemnt found in index:{resault}")
else:
    print("Element not found")