import random
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)
'''this will print days'''


a_a, b_b, c_c = 1, 2, "hey"


print(a_a)
print(b_b)
print(c_c)

dtring = "hello harsh"

print(dtring)  # will print string
print(dtring[0])  # will print first charcater
print(dtring[2:5])  # will print third char to 5th
print(dtring[2:])  # will print from third char
print(dtring*5)  # string will be printed 5 times
print(dtring + "good" + "morning")  # concatinate

'''/////////
//////////////////
/////////////////////////'''

# lists
list = [1, 2, 3, 4, 54, 54, 233443, 345, 2,
        3, 14, 14, "hey", "gneks", "3443.24"]
print(list)  # will print whole list
print(list[0])
print(list + list)


tuple = ("defr", 1, 2, 3, 4, 54, 54, 233443, 345, 2,
         3, 14, 14, "hey", "gneks", "3443.24")
print(tuple)  # will print whole tuple
print(tuple[1])
print(tuple + tuple)

# dictionary

'''/////////
//////////////////
/////////////////////////'''

dictionary = {}

dictionary['three'] = "this is three "
dictionary[3] = "this is numerial three "

longdictionary = {'name': 'harsh', 'roll': '1082', 'dept': 'cse'}

print(dictionary)
print(dictionary['three'])
print(dictionary[3])
print(longdictionary)
print(longdictionary.keys())
print(longdictionary.values())

a = 60

print(a >> 2)
print(a >> 3)
print(a >> 4)
print(a >> 5)
print(a >> 6)
print(a >> 7)
print(a >> 8)
print("========================================================================================================================")

print(a << 2)
print(a << 3)
print(a << 4)
print(a << 5)
print(a << 6)
print(a << 7)
print(a << 8)

print("========================================================================================================================")

b = 13
print(b >> 1)
print(b >> 2)
print(b >> 3)
print(b >> 4)
print(b >> 5)
print(b >> 6)
print(b >> 7)
print(b >> 8)
print("========================================================================================================================")
print(b << 1)

print(b << 2)  # 13 * 2^2
print(b << 3)  # 13 * 2*2*2
print(b << 4)  # 13 * 2*2*2*2
print(b << 5)  # 13 * 2*2*2*2*2
print(b << 6)  # 13 * 2*2*2*2*2*2
print(b << 7)  # 13 * 2*2*2*2*2*2*2
print(b << 8)  # 13 * 2*2*2*2*2*2*2*2


varIable = 10000

if (varIable == 121):
    print("1231221")
else:
    print("bye")

print("404")

x = "hey"
y = " "


def fun():
    print(x + y+"user")


fun()


def func():
    global x
    x = "helolo"
    print(x+"x")


func()


x = 54
y = "helolo"
z = 232342.3243123
q = 1j
w = ["apple", "banana", "cherry"]
e = ("apple", "banana", "cherry")
r = range(6)
t = {"name": "John", "age": 36}
o = {"apple", "banana", "cherry"}
i = frozenset({"apple", "banana", "cherry"})
p = True
u = b"Hello"
b = bytearray(5)
m = memoryview(bytes(5))

a = range(6)

print(type(x))
print(type(y))
print(type(q))
print(type(w))
print(type(e))
print(type(r))
print(type(t))
print(type(o))
print(type(i))
print(type(p))
print(type(u))
print(type(m))
print(type(b))

print(random.randrange(1, 10))


a = "harsh mittal"
print(a[1:10])

'''if index number is 1 then it will count from 2nd letter of string and last index number is 10 then it will count till 9'''

# loop in string

for a in "banana":
    print(a)

a = "harsh"

print(len(a))

txt = "i do love her"

print("do love her" in txt)

text = "the best thing is she loves me too"

if "love" in text:
    print("oh god")

if "live" not in text:
    print("oh god")
b = "Hello, World!"
print(b[-5:-2])
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())

a = "          a     H e l l o, W o r l d!             "
print(a.strip())
a = "Hello, World!"
print(a.replace("H", "beff"))
a = "Hello World!"
print(a.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

bloodGroup = "b+"
txt = "my bg is {}"
print(txt.format(bloodGroup))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
quantity = "3aerg"
itemno = 567
price = 49.95
myorder = "I want to pay {0} dollars for {1} pieces of item {2}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon", "kiwi", "kiwi....w24413.."]
print(thislist)

thislist = ["cpple", "banana", "aherry"]
thislist.append("aotr")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
thislist.insert(1, "orange")

thislist.insert(1, "orange")
thislist.insert(1, "orange")

print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thistuple = ("apple", "banana", "cherry")
thislist = ["kiwi", "orange"]
thislist.extend(thistuple)
print(thislist)


#lists in details
