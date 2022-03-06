
def insertShiftArray(arr,insert):
    """
    Insert value in the middle of an array
    """
    result=[]
    length = ceil(len(arr)/2)
    for i in range(len(arr)):
        if i==length:
            result=result+[insert]
        result=result+[arr[i]]
    return result

def ceil(num):
    floor = int(num)
    if floor != num:
        return floor + 1
    return floor

print(insertShiftArray([1,2,4,5],7))