#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Use negative indexing to print the last item in the tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[3:6])

# একটি টিউপলে থাকা সব উপাদান for লুপ দিয়ে প্রিন্ট করো।

fruits1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for v1 in fruits1:
    print(v1)

# দুটি টিউপল জোড়া লাগিয়ে একটি নতুন টিউপল তৈরি করো।
fruits2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
fruits3 = ("apple1", "banana2", "cherry3", "orange4", "kiwi5", "melon6", "mango7")

join = fruits2 + fruits3
print(join)

# Create a tuple of 4 numbers and print its length.
fruits4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for v2 in range(len(fruits4)):
    print(v2)

# Create a tuple with (name, age, city) and unpack it into variables.

information = ("sahil", 13 , "dhaka")
(a,b,c) = information
print(a)
print(b)
print(c)

# Create a tuple with 4 colors. Change the second item to "black"
color = ("red" , "green" ,"purple" ,"black","white")
a = list(color)
a.append("white 333")
print(a)
