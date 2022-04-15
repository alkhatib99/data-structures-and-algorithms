def binary_search(arr,key):
    
    """
    Function return the index of the search ky if found it,
    or -1  if didn't found it 
    """
    
    indexMid=ceil(len(arr)/2)
    mid=arr[indexMid]
    high=arr[len(arr)-1]

    low=arr[0]
    mid=arr[len(arr)-1]
    if key == high:
        return (len(arr)-1)
    elif key == low :
        return 0
    elif key == mid :
        return indexMid
    elif key > mid:
        for i in range(indexMid,len(arr)):
            if(arr[i]==mid):
                return i
    elif key< mid:
        for i in range(indexMid,0,-1):
            if(arr[i]== mid):
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