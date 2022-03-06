def insert_shift_array(arr, val):
    """
    Insert value in the middle of an array
    """

    new = []

    c = len(arr) - (len(arr) // 2)

    new.extend(arr[:c])
    new.append(val)
    new.extend(arr[c:])

    return new


#arr = [1,2,4,6,7]
#arr = insert_shift_array(arr, 5)
#print(arr)

#arr = [1,3,4,7,9]
#arr = isa2(arr, 2)
#print(arr)