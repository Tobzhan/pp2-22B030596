"""
Write a function that computes the volume of a sphere given its radius.
"""

def volume( r ):
    return (4 * 3.14 * r**3) / 3

r = int(input() )
print( "%.2f" %volume( r ))