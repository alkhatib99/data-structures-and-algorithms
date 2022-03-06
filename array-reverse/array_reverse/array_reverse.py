def reverseArray(list):
    answer = []
    for i in range(len(list)-1, -1, -1):
        answer.append(list[i])
    return answer





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