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
print ("==== Global keyword = 'Do Not use if not necessary' ====")
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

