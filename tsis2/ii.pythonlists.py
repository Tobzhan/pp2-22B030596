thislist = ["apple", "banana", "cherry"]
thislist1 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(len(thislist))
print(type(thislist))

print(thislist[2:5])
thislist[1] = "blackcurrant"
thislist[1:2] = ["blackcurrant", "watermelon"]

