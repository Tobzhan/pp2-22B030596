"""
Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
"""

def is_prime( number ):

    if number == 1:
        return True

    for i in range( 2, number ):
        if ( number % i == 0 ):
            return False
    
    return True

mylist = list(( 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ))
print(list( filter ( is_prime, mylist )))