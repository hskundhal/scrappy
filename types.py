
# dictionaries are using same location in memoory
dict1 = { 'value':11}
dict2 = dict1

print(dict1)
print(dict2)

dict1['value'] = 12
print(dict1)
print(dict2)

# List is continous in memory ---- Linked List is spread around and dont have indexes.