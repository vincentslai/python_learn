print("==== Function ====")
def report_person():
    print("Report a person !")

report_person()

def report_person1(name):
    print("Name is :" + name)

report_person1("Cindy")

def report_person2(name = 'annoymous'): #You can put the arguments equal to 'BLANK' or any default Value to prevent the error called when no arguments were pass
    print("Person name is :" + name)

report_person2()

print("Function with numbers")

def add_num(num1, num2):
    print (num1+num2)

result = add_num(2,4)

print(result) #result will show None, in order for us to use the result of num1 + num2 we need to use return.

def add_num1(num1, num2):
    return num1+num2

result1 = add_num1(4,3)
print (result1 + 10) # This will finally add the add_num + 10

# Max and Min
print ("==== Max - Min ====")
print (max(10,4))
print (max([2,5,10,1,100,67,85, 11])) #The max or min can be used on a list. It will print the hightest or lowest value.

#Enumerate
#The usage of enumerate is to shows the index of the list.
print("")
print("==== Enumerate ====")
mylist = ['a', 'b', 'c', 'd']
for index,item in enumerate(mylist):
    print(f"item {item} is at index {index}")

#.join
print("=== Join ===")
print("--".join(mylist))

#Exercise one: return True if there is a word "Secret" in the string
def secret_check(mystring):
    if 'secret' in mystring:
        return True
    else:
        return False

print(secret_check("There is a secret word"))

#There is a shorter way to do this function
def check_secretword(mystring):
    return 'secret' in mystring #basically the return value already return true or false, so save the long if statement.

print(secret_check("There is secret in the air"))

#Exerise two: Change the vowel to x, and print out the string
def replace_vowel(theString):
    output = list(theString)

    for index,theLetter in enumerate(theString):
        for vowel in 'aeiou':
            if theLetter.lower() == vowel:
                output[index] = 'x'
    output = ''.join(output)
    return output

print(replace_vowel("biomechanics"))

# Modulus Operator %
print("==== Modulus Operator ====")
def even_odd_check(number1):
    if number1 % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

even_odd_check(37)

# sum 
print(sum([2,4,5,10,101,23]))

