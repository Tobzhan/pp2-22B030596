"""

Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

"""

def reversed_str( str ):
    return list(reversed( str ))

str = input()
print ( "".join(reversed_str( str )) )