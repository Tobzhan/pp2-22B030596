thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

thistuple1 = ("apple",) # do not forget comma
print(type(thistuple1))

thistuple3 = tuple(("apple", "banana", "cherry")) # note the double round-brackets

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
x = tuple(y)
p = ("mango",)
x += p
print(x)
del x


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
