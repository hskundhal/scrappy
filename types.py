
# dictionaries are using same location in memoory
dict1 = { 'value':11}
dict2 = dict1

print(dict1)
print(dict2)

dict1['value'] = 12
print(dict1)
print(dict2)

# Numpy arrays use continous in memory ---- 
# pythons built in List have reference to location in memory for data. reference itself is 8 bytes
# python is built using c,c++
# Linked List is spread around and dont have indexes.