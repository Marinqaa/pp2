# lab 2
"""
Python lists
Python tuples
Python sets
Python dicts
Python while
Python for
"""

# list
fruits = ["banana", "apple", "grapes"]
print(fruits)
list1 = ["cde", 635, False, 54, "friends"]
print(type(list1))




drinks = ["tea" , "juice" ,"coffee" ,"juice" , "coffee"]
print(drinks)
print(len(drinks))
print(drinks[1])
print(drinks[-1])
print(drinks[2:5])
print(drinks[:5])
print(drinks[3:])

drinks[1:3] = ["milk"]
print(drinks)
drinks.insert(2, "water")
drinks.append("Cola")
drinks.remove("tea")
print(drinks)

names = list(("Arnur", "Aidos", "Asan", "Karina", "Sabina", "Anel"))
names.pop(1)
names.pop()
del names[3]
print(names)

del names

names1 = list(("Arnur", "Aidos", "Asan", "Karina", "Sabina", "Anel"))
names1.clear()
print(names1)

KBTU = ["discrete stuctures", "pp1", "pp2"]
[print(i) for i in KBTU]

for i in range(len(KBTU)):
    print(KBTU[i])






