fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in "banana":
    print(x)

for x in range(2, 30, 3):
    print(x)
else:
  print("Finally finished!")

for x in [0, 1, 2]:
    pass # if loop is empty