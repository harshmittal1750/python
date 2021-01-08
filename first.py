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
