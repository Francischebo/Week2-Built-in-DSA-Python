# initialize an empty list
my_list = []

# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert an element at the second position
my_list.insert(1, 15)

# extend the list with another list
my_list.extend([50, 60, 70])

# remove the last element from the list
my_list.pop()

# sort the list in ascending order
my_list.sort()

# find the index of the value 30 in the list
idx = my_list.index(30)

# print the list and the index
print(my_list)
print(idx)