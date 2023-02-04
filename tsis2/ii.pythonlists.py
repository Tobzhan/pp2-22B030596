thislist = ["apple", "banana", "cherry"]
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(len(thislist))
print(type(thislist))

print(thislist[2:5])
thislist[1] = "blackcurrant"
thislist[1:2] = ["blackcurrant", "watermelon"]

thislist.append("orange")

thislist.insert(1, "kiwi")
thislist.remove("watermelon")
thislist.pop(1)
del thislist[0]
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
thislist.clear()
print(thislist)
del thislist

#list3 = list1 + list2
