thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)

thisdict["color"] = "red" # or thisdict.update({"color": "red"})
thisdict.update({"year": 2020})

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.pop("model")

for x, y in thisdict.items():
  print(x, y)

del thisdict

thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print( myfamily["child1"]["name"] )

# Method	      Description
# clear()	      Removes all the elements from the dictionary
# copy()      	Returns a copy of the dictionary
# fromkeys()  	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()     	Returns a list containing a tuple for each key value pair
# keys()	      Returns a list containing the dictionary's keys
# pop()       	Removes the element with the specified key
# popitem()   	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary