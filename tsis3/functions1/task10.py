"""
Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
"""

def unique( mylist ):
    newlist = list()
    for i in range( len( mylist) ):
        if ( mylist[ i ] in newlist ):
            continue
        else:
            newlist.append( mylist[ i ])

    return newlist

mylist = list (( 123, 123, 56, 12 , 56, 789))
mylist2 = list (( "ABC", "XYZ", "AABBCC", "ABC", "AABBCC"))

print ( unique( mylist ))
print ( unique( mylist2 ))