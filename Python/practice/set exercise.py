# ➤ Create a set with 5 fruit names.
fruites = {"apple","banana","lichi","dragon fall","grapes"}

# Check if "apple" exists in the set.
fruites1 = {"apple","banana","lichi","dragon fall","grapes"}
print("apple" in fruites1)

# ➤ Print all items in the set using a for loop.
for a in fruites1:
    print(a)

# ➤ Create a set and add "kola" to it.
fruites2 ={"apple","banana","lichi","dragon fall","grapes","mango"}
fruites2.add("kola")
print(fruites2)

# ➤ Create an empty set and add 3 numbers to it.
numberslist ={}
numberadd ={1,2,3,4}
number3 =numberadd.union(numberslist)
print(number3)

# ➤ Remove "mango" from a set using remove().
fruites2.remove("mango")
print(fruites2)

# ➤ Use pop() to remove a random item from the set.
fruites2.pop()
print(fruites2)

# ➤ Loop through a set of 5 city names and print each.
city ={"narayanganj","dhaka","kumilla","dhanmondi","bosundhara"}
for f in city:
    print(f)
