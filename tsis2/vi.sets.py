thisset = {"apple", "banana", "cherry", "apple"} #Set items are unordered, unchangeable, and do not allow duplicate values.
print(thisset)
print(len(thisset))
print(type(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

for x in thisset:
    print(x)
    
print("banana" in thisset)

thisset.add("orange")
thisset.remove("banana")
print(thisset)

#set3 = set1.union(set2)

# add()	                 Adds an element to the set
# clear()	             Removes all the elements from the set
# copy()	             Returns a copy of the set
# difference()	         Returns a set containing the difference between two or more sets
# difference_update()    Removes the items in this set that are also included in another, specified set
# discard()	             Remove the specified item
# intersection()	     Returns a set, that is the intersection of two other sets
# intersection_update()  Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	         Returns whether two sets have a intersection or not
# issubset()	         Returns whether another set contains this set or not
# issuperset()	         Returns whether this set contains another set or not
# pop()	                 Removes an element from the set
# remove()	             Removes the specified element
# symmetric_difference() Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	             Return a set containing the union of sets
# update()               Update the set with the union of this set and others
