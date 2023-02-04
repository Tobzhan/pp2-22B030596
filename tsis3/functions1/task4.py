"""

You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

"""
def is_prime( number ):

    if number == 1:
        return True

    for i in range( 2, number ):
        if ( number % i == 0 ):
            return False
    
    return True


def filter_prime( mylist ):
    newlist = list()
    for i in range( len( mylist ) ):
        #print( mylist[ i ])
        if ( is_prime( mylist[ i ])):
            newlist.append( mylist[ i ])

    return newlist

mylist = list( (1, 5, 8, 9, 11, 13, 15, 17, 19) )
print ( filter_prime( mylist ))