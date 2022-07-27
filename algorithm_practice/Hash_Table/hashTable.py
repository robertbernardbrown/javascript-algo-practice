# class HashTable :
#     def __init__( self ):
#         self.table = []
#         self.size = 10
#         self.hash_table = self.create_buckets()

#     def create_buckets(self):
#         return [[] for _ in range(self.size)]

#     def add( self, key, val ):
#         # Get the index from the key
#         # using hash function
#         hashed_key = hash(key) % 10
          
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
  
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
              
#             # check if the bucket has same key as
#             # the key to be inserted
#             if record_key == key:
#                 found_key = True
#                 break
  
#         # If the bucket has same key as the key to be inserted,
#         # Update the key value
#         # Otherwise append the new key-value pair to the bucket
#         if found_key:
#             bucket[index] = (key, val)
#         else:
#             bucket.append((key, val))

        
#     def search( self, k ):
#         hash = self.hash(k)
#         return self.table[hash]

#     def remove( self, k ):
#         hash = self.hash(k)
#         if not self.table[hash]:
#             return -1
#         self.table[hash] = None
#         return 1
    
#     def hash( self, key ):
#         return hash(key)

#     def __str__(self):
#         return "".join(str(item) for item in self.table)

# class HashTable:
  
#     # Create empty bucket list of given size
#     def __init__(self, size):
#         self.size = size
#         self.hash_table = self.create_buckets()
  
#     def create_buckets(self):
#         return [[] for _ in range(self.size)]
  
#     # Insert values into hash map
#     def set_val(self, key, val):
        
#         # Get the index from the key
#         # using hash function
#         hashed_key = hash(key) % self.size
          
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
  
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
              
#             # check if the bucket has same key as
#             # the key to be inserted
#             if record_key == key:
#                 found_key = True
#                 break
  
#         # If the bucket has same key as the key to be inserted,
#         # Update the key value
#         # Otherwise append the new key-value pair to the bucket
#         if found_key:
#             bucket[index] = (key, val)
#         else:
#             bucket.append((key, val))
  
#     # Return searched value with specific key
#     def get_val(self, key):
        
#         # Get the index from the key using
#         # hash function
#         hashed_key = hash(key) % self.size
          
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
  
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
              
#             # check if the bucket has same key as 
#             # the key being searched
#             if record_key == key:
#                 found_key = True
#                 break
  
#         # If the bucket has same key as the key being searched,
#         # Return the value found
#         # Otherwise indicate there was no record found
#         if found_key:
#             return record_val
#         else:
#             return "No record found"
  
#     # Remove a value with specific key
#     def delete_val(self, key):
        
#         # Get the index from the key using
#         # hash function
#         hashed_key = hash(key) % self.size
          
#         # Get the bucket corresponding to index
#         bucket = self.hash_table[hashed_key]
  
#         found_key = False
#         for index, record in enumerate(bucket):
#             record_key, record_val = record
              
#             # check if the bucket has same key as
#             # the key to be deleted
#             if record_key == key:
#                 found_key = True
#                 break
#         if found_key:
#             bucket.pop(index)
#         return
  
#     # To print the items of hash map
#     def __str__(self):
#         return "".join(str(item) for item in self.hash_table)
  
  
# insert some values
# hash_table.add('gfg@example.com', 'some value')
# print(hash_table)
# print()
  
# hash_table.set_val('portal@example.com', 'some other value')
# print(hash_table)
# print()

# hash_table.set_val('portal@example.com', 'some other value2')
# print(hash_table)
# print()
  
# # search/access a record with key
# print(hash_table.get_val('portal@example.com'))
# print()
  
# # delete or remove a value
# hash_table.delete_val('portal@example.com')
# print(hash_table)
# print()
# print('k')

# hash_table.__str__()

from contextlib import nullcontext
from mimetypes import init


# class Hashmap:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [[] for i in range(self.MAX)]
        
#     def get_hash(self,key):
#         hash_key = 0
#         for char in key:
#             hash_key += ord(char)
#         return hash_key % 100

#     def add(self,key,value):
#         hash_key = self.get_hash(key)
#         found = False
        
#         for index,element in enumerate(self.arr[hash_key]):
#             if element[0] == key and len(element) == 2:
#                 self.arr[hash_key][index] = (key,value)
#                 found = True
#                 break
#         if not found:
#             self.arr[hash_key].append((key,value))
                
#     def get(self,key):
#         hash_key = self.get_hash(key)
#         for element in self.arr[hash_key]:
#             if element[0] == key:
#                 return element[1]
            
#     def __delitem__(self,key):
#         hash_key = self.get_hash(key)
#         for index,element in enumerate(self.arr[hash_key]):
#             if element[0] == key:
#                 del self.arr[hash_key][index]
            
#     def print_hm(self):
#         values = [i for i in self.arr if i != []]
#         return values

#     # To print the items of hash map
#     def __str__(self):
#         return "".join(str(item) for item in self.arr)

class Hashmap:
    def __init__(self):
        self.size = 100
        self.hashmap = [[] for _ in range(self.size)]

    def __str__(self):
        return "".join(str(item) for item in self.hashmap)

    def hashFunc(self, key):
        hashValue = hash(key) % self.size
        return hashValue

        # for i in key:
        #     num += ord(key[i])
        # hash = num % self.size
        # return hash

    def getValue(self, key):
        keyHash = self.hashFunc(key)
        found = False
        bucket = self.hashmap[keyHash]

        for index, element in enumerate(bucket):
            record_key, value = element
            if record_key == key:
                return bucket[index][1]
        if not found:
            return False

    def setValue(self, key, value):
        keyHash = self.hashFunc(key)
        found = False
        bucket = self.hashmap[keyHash]

        for index, element in enumerate(bucket):
            record_key, record_value = element
            if record_key == key:
                found = True
                bucket[index] = (key, value)
                break        

        if not found:
            bucket.append((key, value))

    def deleteValue(self, key):
        keyHash = self.hashFunc(key)
        found = False
        bucket = self.hashmap[keyHash]

        for index, element in enumerate(bucket):
            record_key, value = element
            if record_key == key:
                found = True
                del bucket[index]
                break        

        if found:
            return True
        else:
            return False


hash_table = Hashmap()

print(hash_table)
hash_table.setValue('key', 13)
hash_table.setValue('key', 20)
print('second')
print(hash_table)
print('ssss')
print(hash_table.getValue('keys'))
print(hash_table.deleteValue('keysss'))
print(hash_table)
