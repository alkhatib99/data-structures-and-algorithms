from linked_list.linked_list import LinkedList
class HashTable():

    def __init__(self ,size=1024):
        """initialization hash table"""
        self.size= size 
        self.arr = [None]*size
         
    

    def hash(self, key):
        """method to hash value using ASCII code and return it"""
        hashed = 0
        for char in key:
            hashed += ord(char)
        hash_index= hashed*77 % self.size 
        return hash_index
    
    def set(self ,key ,value):
        """method to store (key, value) pairs in the key index of list"""
        hash_key = self.hash(key)
        if self.arr[hash_key]== None:
            self.arr[hash_key]=[[key,value]]
        else:
            self.arr[hash_key].append([key, value])

        
    def get(self, key):
        """method  that return the value of the key"""
        hashed = self.hash(key)
        try:
            return self.arr[hashed][0][1]
        except:
            return "None"
    def contains(self, key):
        ""
        hashed = self.hash(key)
        if self.arr[hashed][1][0] == key:
            return True
        else:
            return False

    def delete(self , key):
        """function that set the value of key to None"""
        h = self.hash(key)
        for index , element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]