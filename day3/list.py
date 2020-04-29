# List / Collection / Array

# name1 = "John"
# name2 = "Mary" 
# name3 = "Sue"
# name4 = "Gary"

names = ["John", "Mary", "Sue", "Gary", "RJ"]

# length shows length of array
print(len(names))

# Index positions
print(names[0]) # 0 is the index position 
print(names[3])

# list[start:end]
print(names[0:2])
print(names[2:4])
print(names[0:3:2])
print(names[0::2]) # every other item for list

# Manipulating lists
print(names.append("James")) # output prints 'none'
print(names)

names.remove("Sue") # removes items by name
print(names)
names.pop(0) # pop is used to remove using index position
print(names)

rickys = ["Ricky", "Ricky", "Ricky", "Ricky"]
rickys.remove("Ricky")
print(rickys)
rickys.pop(1)
print(rickys)