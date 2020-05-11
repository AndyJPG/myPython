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

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, "a"}

set1.update(set2)
print(set1)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "age": 5
}

for x in thisdict:
    print(x + " : " + str(thisdict[x]))

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

if "brand" in thisdict:
    print("yes")

thisdict.pop("age")
print(thisdict)

a = 33
b = 44

if b > a:
    print("b > a")
elif b == a:
    print("b = a")
else:
    print("b < a")

if bool(a):
    print("a is true")

if b >= a:
    pass

i = 0
while i < 9:
    i += 1

    if i >=6:
        print("i am dead")
        break

    if i == 3:
        continue

    print(i)

while i < 15:
    if i == 6:
        print("i am back")
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

for x in "apple":
    print(x)

for x in range(6):
    print(x)

for x in range(2, 20, 2):
    print(x, "incremental 2")
else:
    print("last statement")


def unknown_para(*kids):
    print("The yungest child is " + kids[2])


unknown_para("Emil", "Tobias", "Linus")


def unknown_keyword(**kid):
    print("His last name is " + kid.get("lname"))


unknown_keyword(fname="Tobias", lname="Refsnes")


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)


def fibonacci_no(i):
    numbers = [0, 1]
    while len(numbers) < i:
        numbers.append(numbers[-1] + numbers[-2])
    print(numbers)


fibonacci_no(7)


def fibonacci_recurse(i, p=0, c=1):
    if i > 0:
        print(p)
        fibonacci_recurse(i-1, c, p+c)


fibonacci_recurse(10)

x = lambda a : a + 10
print(x(5))


def myfunc(n):
    return lambda a : a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))