
def insert_shift_array(arr,insert):
    """
    Function takes and array and new value
     to insert new value to the middle of array
    """
    result=[]
    middle = ceil(len(arr)/2)
    for i in range(len(arr)):
        if i==middle:
            result=result+[insert]
        result=result+[arr[i]]
    return result

def ceil(num):
    floor = int(num)
    if floor != num:
        return floor + 1
    return floor

print(insert_shift_array([1,2,3,4,5],7))