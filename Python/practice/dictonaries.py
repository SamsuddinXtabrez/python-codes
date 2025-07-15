# access item
thisdict = {
    "samsuddin":{
        "name":"sahil",
        "roll": 19,
        "class":  9,
        "school": "adarsha school"
    },
    "rabeya" :{
        "name":"rabeya",
        "calss":3,
        "roll":7,
        "school": "adardsha school"
    },
    "year":2025
}
print(thisdict['year']) # simple way to access any items
# access items
x=thisdict.get("samsuddin")
print(x)

# The keys() method will return a list of all the keys in the dictionary.
x1 = thisdict.keys()
print(x1)

#The values() method will return a list of all the values in the dictionary.
x2 = thisdict.values()
print(x2)

# change items in dictonaries
info ={
    "Sahil":{
        "birth":2009,
        "date": "1 october",
        "place": "bhuiyaarbag",
    },
    "year23":2025
}
info["year23"] = 2005
print(info["year23"])

# update methood
info123 ={
    "Sahil":{
        "birth":2009,
        "date": "1 october",
        "place": "bhuiyaarbag",
    },
    "year2345":5056
}

info123.update({"Sahil":"Sahil is a mastermind of football"})
print(info123["Sahil"])

