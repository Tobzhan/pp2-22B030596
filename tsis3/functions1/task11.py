"""
Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
"""

def is_palindrome( s ):
    if ( s == s[::-1] ):
        return True
    else:
        return False

s1 = "banana"
s2 = "appa"
print( is_palindrome( s1 ))
print( is_palindrome( s2 ))