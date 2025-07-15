### Here we are going throug all the operations for hashing
# Declaration: a hash map is declared like any other variable. The syntax is {}

hash_map = {}

# If you want to initialize it with some key value pairs, use the following syntax:
hash_map = {1:2, 3:4, 5:3, 6:1}

# Checking if a key exists: simply use the `in` keyword
print(1 in hash_map)
print(2 in hash_map)

# accessing a value given a key: use square brackets, similar to an array.
hash_map[5] # 3


# Adding or updating a key: use square brackets, similar to an array.
# If the key already exists, the value will be updated

hash_map[6] = 10

# Deleting a key: use the del keyword. Key must exist or you will get an error.
del hash_map[1]

# get size 

print(len(hash_map))

# Get keys: use .keys(). You can iterate over this using a for loop.

keys = hash_map.keys()
for key in keys:
    print(key)

# get values: use .values(). You can iterate over this using a for loop

values = hash_map.values()
for val in values:
    print(val)

