li = [1,2,3,4,5,6,6,7,8,9]
print(li)

li[1] = 33

print(li)

#access list item
hablu = ["doramon","shinchan", "ninja hattori", "pokemon", "motu patlu"]
print(hablu[1])
print(hablu[3])

# add items in list
hablu1 = ["doramon","shinchan", "ninja hattori", "pokemon", "motu patlu"]
hablu1.append("jhony jhony yes papa")
print(hablu1)
# insert
hablu1.insert(6,"kiteretsu")
print(hablu1)
# remove items in order of syntax
hablu1.remove("shinchan")
print(hablu1)
hablu1.pop(2)
print(hablu1)
del hablu1[0]
print(hablu1)
