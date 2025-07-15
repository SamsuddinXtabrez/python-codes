# python set (not duplicate allow in this set)
myset = {"sahil","jr","neymer","messi","jr"}
print(type(myset))

# len function use
# print(len(myset))

#Access Items (But you can loop through the set items using a for loop or ask if a specified value is present in a set, by using the in keyword)
for k in myset:
    print(k)
print("ss" in  myset) # specific item ctach if exits in the sets if don't exist then false
print("sahil" in  myset) #  specific item ctach if exits in the sets if exist then true

# add items
thisset = {"apple", "banana", "cherry"}
thisset.add("tipu")
print(thisset)


# update methood using
thisset1 ={"apple","banana","kola","bichi"}
mylist23 ={"sandwich","apple 23"}
thisset1.update(mylist23)
print(thisset1)

# remove item () and Discard item () methood using
myset4 ={1,2,3,4,5,6,7,8,9,10,20}
myset4.remove(20)
print(myset4)

# or discard () methood (discard any item by write the item in the discard methood)

myset4.discard(4)
print(myset4)

#or clear () methood (clear all items in the list or set)
myset4.clear()
print(myset4)

# loop sets

for d in myset4:
    print(d)

# join sets (using by union() set methood)

number1 ={1,2,3,4,5,6,7}
number2 ={8,9,10}
number3 = number1.union(number2)
print(number3)

# or update methood
number2.update(number1)
print(number2)

