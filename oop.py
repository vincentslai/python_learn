#SCOPE
#LEGB Rule
#Local
print("==== Local Variable example ====")
def doSomething():
    x = "Inside"
    print(x)

doSomething()

#Enclosing
print("==== Enclosing level ====")
z = 'This is global level'

def encl():
    z = 'enclosing level' 
    def insideDef():
        print(z) 
        #Python going to look for global, which doesnt have one.
        #The next one Up is on the enclosing level, that is why z from
        #enclosing level get print out :)
    insideDef()
encl()

#Global
print("==== Global Variable ====")
xyz = "Global variable"

def globalDef():
    print (f"This {xyz} came from outside of the function")

globalDef()

#Built In variable example will be like len, sum, max, min

#Global keyword : use with caution, most people don't change global variable, but in chase you need to.
print ("==== Global keyword - 'Do Not use if not necessary' ====")
a = 'outside value'

def callFunction():
    global a
    a = 'inside value'
    return a
    
print(callFunction())
print(a)

#OOP : Object Oriented Programming allows programmers to create their own objects that have methods and attributes.
class SampleOOP():
    pass
x = SampleOOP()

print(type(x)) # This function shows what type is certain item

class Car():

    #CLASS OBJECT ATTRIBUTES
    industry = 'automotives'

    def __init__(self, carModel, carType, carYear):
        self.carModel = carModel
        self.carType = carType
        self.carYear = carYear

car1 = Car("BMW", "Series 5", "2019")

print(car1.carModel)
print(car1.carType)
print(car1.carYear)
print(car1.industry)

car2 = Car("Acura", "RDX", "2019")

print(car2.carModel)
print(car2.carType)
print(car2.carYear)
print(car2.industry) # The class object attributes will always be the same for all of them

print("==== OOP Method ====")

class Circle():

    pi = 3.14

    def __init__(self, radius = 1): #you can initial the value, incase there is no value get pass
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

myCircle1 = Circle(4)
print(myCircle1.radius)
print(myCircle1.area())

#OOP Inheritance
print("")
print ("==== OOP Inheritance ====")

class Animal():
    def __init__(self, fur):
        self.fur = fur
    
    def report(self):
        print("animal")

    def eat(self):
        print("eating!")

a = Animal('yellow')
a.eat()
a.report()

class Dog(Animal):
    def __init__(self, fur):
        Animal.__init__(self, fur)
        print("dog created")
    
    def report(self): #You can override the animal method by creating another report
        print("This is from Dog class")

print("=== called from inheritance ===")
d = Dog('Fuzzy')
d.eat()
d.report()
print(d.fur)

print("")
print("=== Special method ===")

class Book():

    def __init__(self, bookTitle, bookAuthor, bookPages):
        self.bookTitle = bookTitle
        self.bookAuthor = bookAuthor
        self.bookPages = bookPages
    
    def __repr__(self):
        return f"Title of the book is {self.bookTitle}, Author of the book is {self.bookAuthor}."
    
    def __len__(self): #define what len will return in this method
        return self.bookPages

myBook = Book("All about Python", "Jose", 275)
print(myBook)
lengthBook = len(myBook) 
print(lengthBook)

# Exercise 1: Create bank account taking 2 attrivutes : Owner and Balance.
# Two methods Deposit and withdraw, cannot withdraw more money than what the owner has.

class createBank():
    def __init__(self, customerName, balance, withdraw = 0):
        self.customerName = customerName
        self.balance = balance
        self.withdraw = withdraw
    
    def depositAmount(self, deposit1 = 0):
        self.balance = self.balance + deposit1
        return f"Thank you. Deposit is complete. Current balance: ${self.balance}"

    def withdrawAmount(self):
        if(self.balance > self.withdraw):
            self.balance = self.balance - self.withdraw
            return f"Thank you. Withdraw is complete. Current balance: ${self.balance}"
        else:
            return f"Not enough balance, current balance $ {self.balance}"
            
    def __repr__(self):
        return f"Customer : {self.customerName}, has $ {self.balance} in the account."
    
newBankAcc = createBank("Jason Bourne", 1000, 3000)
print(newBankAcc)
print(newBankAcc.depositAmount(500))
print(newBankAcc.withdrawAmount())

#Decorator
print("")
print("=== decorator ===")
def hello(name="Jose"):
    print("the hello function has been run")

    def greet():
        print("    This is inside greet")

    def welcome():
        print("    welcome yeah")  

    if name == "Jose":
        return greet
    else:
        return welcome

    greet()

hello()

print("")
print("=== decorator #2 function returning function, function with argument ===")
def hello1():
    print("Hello There!")

def other(func):
    print("Print some code")

    func()

other(hello1)

print("")
print("=== Decorator #3 : Creating our own decorator - using @ ")
def new_decorator(abc):

    def wrap_func():
        print("print some code before executing abc")

        abc()

        print("Print some more code after the abc being called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Print from Function needs decorator")

# But instead of using this reassignment you could use the @ (at) instead
#func_needs_decorator = new_decorator(func_needs_decorator)   --> this replace by putting @new_decorator

func_needs_decorator()



