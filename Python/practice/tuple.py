#tuples tutorial
newtuples=( "cherry","kiwi","mango","apple","chanachur","pani","coconute")
print(type(newtuples))

# access a targeted item by index number
print(newtuples[0])

# negative index number to catch items in list
print(newtuples[-3])

#Use a range of indexes to print the items in the list

print(newtuples[2:7])

# update tuples
newtuples1=( "cherry","kiwi","mango","apple","chanachur","pani","coconute")
a = list(newtuples1)
a.append("juice")
print(a)

# unpack tuples
newtuples2=( "cherry","kiwi","mango","chili","sandwich")

(a,*b) = newtuples2
print(b)

# loop tuples
newtuples3=( "cherry","kiwi","mango","chili","sandwich")

for v in newtuples3:
    print(v)
# range (looping)
for v1 in range(len(newtuples3)):
        print(v1)

# while loop tuples
# newtuples4=( "cherry","kiwi","mango","chili","sandwich")
#
# # i = 0
# # while i < len(newtuples4):
# #     print(newtuples4)

# join tuples
newtuples5=( "cherry","kiwi","mango","chili","sandwich")
newtuples6=( "cherry1","kiwi2","mango3","chili4","sandwich5")

# join = newtuples5 + newtuples6
# print(join)

# multiple the items
print(newtuples5 * 2)

# tuples methoods (Returns the number of times a specified value occurs in a tuple)

newtuples7=( "cherry","kiwi","mango","chili","sandwich")

count = newtuples7.count("cherry")
print(count)
# tuples methoods (Searches the tuple for a specified value and returns the position of where it was found)

newtuples8=( "cherry","kiwi","mango","chili","sandwich")
index = newtuples8.index("mango")
print(index)

