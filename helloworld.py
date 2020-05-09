print("Hello, World!")

#This is a comment.

"""
more line
comment
"""

_myText = "Fives is greater than two!"
x, y, z = "apple", "grape", "orange"

def myFunc():
    # global x
    x = "hello"
    if 5 > 2:
        print(_myText + " " + x)

myFunc()

print("Globle number : " + x)

y = 6
print(type(y))

x = 1.34e100
print(x)

x = 3+5j
y = 5+2j
print(x+y)

import random

print(random.randrange(1, 10))

print(z[0].upper())
print(z[2:6])
print(len(z))

print("o" in z)

txt = "my number is {} and {}"
txt1 = "my no {1} is {0}"
print(txt.format(x, y))
print(txt1.format(x, y))

print(isinstance(x, complex))

alist = [1,2,4,5,3]
print(alist)

for x in alist:
    print(x)

alist.append(9)
alist.insert(2, 10)

#copy list
copylist = alist.copy()
copylist.sort()
print(copylist, alist)

aset = {"apple", "orange"}

aset.add("grape")
print(aset)

