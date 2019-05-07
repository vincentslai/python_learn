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

#result = add_num(2,4)

#print(result) #result will show None, in order for us to use the result of num1 + num2 we need to use return.

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

#Check if the sum of the two numbers is 10, is true or false
print("Task 1 : Check if the sum of two numbers is 10")
def check_ten(n1,n2):
    return (n1+n2) == 10

print(check_ten(8, 2))

print("Task 3 : change the first string to Upper case")
def first_upper(mysrting1):
    return mysrting1[0].upper()

print(first_upper("minimum"))

print("Task 4: Print the last 2 string from the string, if less than 2 string show error")
def last_two(mystring2):
    if len(mystring2) < 2:
        return "Error"
    else:
        return mystring2[-2:]

print(last_two("D"))


print("Task 5: Check if there is 1,2,3 in the list")
def seq_check(num3):
    for i in range(len(num3)-2):
        #0, 1,2, 3, .... n-2 
        if num3[i] == 1 and num3[i+1] == 2 and num3[i+2] == 3: #because of this +1 and +2 that is why it doesnt need to go all the way to the end of the list
            return True
    return False

print(seq_check([1,3,5,6,1,2,3,5,6,9,10]))

print("task 6: Given 2 strings, find the difference between the two")
print("==== using 'abs' : absolute value function ====")
def compare_len(s1,s2):
    return abs(len(s1)-len(s2))

print(compare_len("pinching", "recommends"))

print("task 7: given a list of integers, if the length of the list is an even number return the sum, if odd return the max value")
def sum_or_max(list1):
    length = len(list1)
    if length % 2 == 0:
        return sum(list1)
    else:
        return max(list1)

print(sum_or_max([1,5,3,6,10,100,2,88,38]))