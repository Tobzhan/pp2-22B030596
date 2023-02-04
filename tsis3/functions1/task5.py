"""

Write a function that accepts string from user and print all permutations of that string.

"""
import itertools
def permutation( str ):
    return list(itertools.permutations( str ))

str = input()
print (permutation( str ))