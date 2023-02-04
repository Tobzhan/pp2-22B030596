"""

Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)

"""

def fah_to_cen( fah ):
    return (5 / 9) * (fah - 32)

f = int ( input() )
print( '%.2f' %fah_to_cen( f ) )