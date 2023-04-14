# Tuple: immutable, same as list
tup = (1, 5, 6)
print(type(tup), tup)
tup1 = (1,)  # single item tuple
# tup[0]=90 that means it is immutable

# Tuple indexing
print(tup[0])
print(tup[1])
print(tup[2])
# + and - indexing same as string
print(tup[-1])
print(tup[2])

if 342 in tup:
    print("Yes 342 is present int this tuple")

# slicing
tup2 = tup[1:4]
print(tup2)

# list are mutable
# tuples are immutable
# strings are immutable