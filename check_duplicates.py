# Find the duplicates on a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# My solution
new_list = []
duplicates = []
for letter in some_list:
    if letter in new_list:
        duplicates.append(letter)
    new_list.append(letter)
print(duplicates)
duplicates.clear()

# Proposed solution
for letter in some_list:
    if some_list.count(letter)>1:
        if letter not in duplicates:
            duplicates.append(letter)
print(duplicates)