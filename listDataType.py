# list: order collection, mutable
marks = [3,5,6,"harry",True,6,7,2,32,345,23] 
print(marks)
print(type(marks))

# list index:
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

#Negative Indexing:
print(marks[-3]) 
print(marks[len(marks)-3]) # positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

if 7 in marks:
  print("Yes")
else:
  print("No")
  
# same thing applies for strings as well!
if "arry" in "Harry":
  print("Yes")

print(marks)
print(marks[0:])
print(marks[0:len(marks)])
print(marks[1:8])
print(marks[1:8:3])

# List Comprehensionprint
lst1 = [i for i in range(4)]
print(lst1)
lst2 = [i*i for i in range(4)]
print(lst2)
lst3 = [i*i for i in range(10) if i%2==0]
print(lst3)

# Example 1:Accepts items with the small letter "o" in the new list 
names = ["Mila","Sarah","Bruno","Rosa","Sana"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Example 2: Accepts items which have more than 4 letters
namesLenth_4 = [item for item in names if (len(item) > 4)]
print(namesLenth_4)