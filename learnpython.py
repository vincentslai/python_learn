my_number = 2+1

print("oh Hello there!")
print("the resut of 2+1 is %d" % my_number)
print(100/25)
print(2**3) #2 the power of 3

salaries = {'john': 10, 'Mike': 20, 'David' : 50}
salaries['Cindy'] = 40
print(salaries)

people = {'john':{'salary':10, 'age':30}}
print(people["john"])
print(people["john"]["age"])

print(salaries.keys())
print(salaries.values())
print(salaries.items())

# Tuples
t = (1,2,3,'a', 2.3)
print(t)

# Sets
randNumber =[1,4,5,2,1,66,12,42,9,90]
print(set(randNumber))

firstName = "Andrew"
age = 4

print("Hi, my name is {} and I am {} years old".format(firstName, age))
print(f"Hello, my name is {firstName} and I am {age} years old")

# Comparison and logical operators
print(3<2)

username = "admin"
print (username == "admin")

print (1 == 2 or 2>3) # and need to be both to be true where else or one can be true.

if 1==2:
    print("Access Granted")
elif 1==1:
    print("tada")
else:
    print("All other condition were False")

#Loops
print(" ==== For Loop ====")
seq = [1,2,3,4,5]
for item in seq: #the item is a temporary variable name 
    print("hello") #just show 5 hello
    print(item *3)

myString = ("Hello")
for char in myString:
    print(char)

personelSalaries = {'John': 10, 'Saly': 20, 'Lisa': 30}
for employee in personelSalaries:
    print (employee)
    print (personelSalaries[employee])

#Tuple Unpacking
myPairs = [('a', 1), ('b', 34), ('c', 103)]
print("===== ===== ===== TUPLE ===== ===== =====")
#len = length
print(len(myPairs)) #print how many tuple pairs

for items in myPairs:
    print(items)

for item1, item2 in myPairs:
    print(item1)
    print(item2)

# While Loop and 
print("==== while loop ====")
i = 1
while i < 5: 
    print (f"i is currently: {i}")
    i = i+1

# Range
for x in range(0,5):
    print (x)
xResult = list(range(0, 11, 2)) #The third variable is the stepping, so step 0, 2, 4, ...
print(xResult)

print('s' in 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.') #the 'in' function is to see if there is 's' inside a very long string  - the element is inside the the other 