# list methods:

l = [11, 45, 2, 3, 4, 5, 1, 1, 1]
print(l)

# appends items to the end of existing list
l.append(7)
print(l)

l.sort()
print(l)
l.sort(reverse=True)
print(l)

l.reverse()
print(l)
# index() : this method returns the index of the first occuresnce of the list item.
print(l.index(1))
print()

print(l.count(1))
print(l)

# this code change original list
m = l  # it make refrence that is not recommended
m[0] = 0
print(l)
# copy method is make copy not change original list
m = l.copy()
m[0] = 0
print(l)

#
l.insert(1, 899)  # specific index and the item to be inserted
print(l)

# add a list to a list
m = [900, 1000, 1100]
# it change l
l.extend(m)
print(l)
# concatenate two lists and make new list
colors1 = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
colors = colors1 + colors2
print(colors)
