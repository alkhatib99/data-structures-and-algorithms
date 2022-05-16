def insertion_sort(arr):
    i=1
    for i in range(len(arr)):

        j=i-1
        temp=arr[i]

        while (j >= 0) and (temp < arr[j]):
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = temp


if __name__=="__main__":
    arr=[8,4,23,42,16,15]

    insertion_sort(arr)

    print(arr)