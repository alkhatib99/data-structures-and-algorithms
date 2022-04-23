def binary_search(sorted_array,key):
    
  """
    Function return the index of the search ky if found it,
    or -1  if didn't found it """
    
  start = 0
  end = len(sorted_array)
  mid = end // 2
  print(start, mid, end, key)
   
  if end == 1:
    return 0
  if end == 0:
    return -1

  try:
    while mid >=1:
      if key == sorted_array[mid]:
        return mid
      elif key < sorted_array[mid]:
          end = mid -1
          mid = (end + start) // 2
      elif key > sorted_array[mid]:
          start = mid +1
          mid = (end + start) // 2
        
  except IndexError:
    return -1
