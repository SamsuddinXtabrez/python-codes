#copy list
number=[1,2,3,3,4,5,5,6]
number1= number.copy()
print(number1)
print(number)

#join two list
name = ["a","b","c"]
name2 = [1,2,3,4]
# name3 = name + name2
# print(name3)

name.extend(name2)
print(name)
