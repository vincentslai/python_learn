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