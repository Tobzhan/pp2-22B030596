"""
Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:
"""

def histogram( nums ):
    for i in range( len( nums )):
        for j in range( nums[ i ]):
            print ("*", end='')
        print ("\n")

histogram([4, 9, 7])