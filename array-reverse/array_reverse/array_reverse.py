
def reverse_array(arr):
    """
    This method will recive an array a argument
    and return a new array reversed of recived array.

    """
    
    new_arr = []
    # looping into the array as reversed by range method
    #       define the stop point and the step  
    for i in range (len(arr)-1,-1,-1):
        new_arr.append(arr[i])
    
    return new_arr;




if __name__=="__main__":
        
    # Define a empty array
    a=[]
    # Take the array's element  as a string from the user 
    user=input('Enter the array: ')
    # split the string into array of strings with delimeter ',' 
    split_list=user.split(',')
    # converto the array of split strings to float array 
    map_list=list(map(float,split_list))

    a=map_list
    print(a)
    a=reverse_array(a)    
    print(a)