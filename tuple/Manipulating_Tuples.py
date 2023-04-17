# Manipulating Tuples:
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "Shrilanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# Tuple Methods:
Tuple1 = (0, 1, 2, 3, 3, 4, 5, 1, 2, 2)
res = Tuple1.count(3)
print("Count of 3 in Tuple is:", res)

# index() Method:
# if element is not present in tuple it generate "value error"
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print("First occurence of 3 is", res)

res = Tuple.index(3, 4, 8)  # tuple.index(element,start,end)
print(res)

lentuple = len(Tuple1)
print(lentuple)
