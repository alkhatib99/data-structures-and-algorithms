def reverse_array(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr





# Define a empty array
a=[]
# Take the array as a string from the user 
user=input('Enter the array: ')
# split the string into array of strings with delimeter ',' 
split_list=user.split(',')
# converto the array of split strings to float array 
map_list=list(map(float,split_list))

a=map_list
print(a)
a=reverse_array(a)    
print(a)