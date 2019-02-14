# python object oriented programming
# python classes and object
# Almost everything in python is an object, with it properties and methods
# A class is like an object constructor or a blue print for creating an objects
# To create a class the keyword class is used
# When we instantiate a class, we get an object
# Objects can contain methods. Methods in objects are functions that belong to the object
# __init__ allow us to create an instance of the class attributes
# self keyword mean allow us to connect properties to the actual instance of the class


# Exercise 1: Create a class named person, use the __init__() function to assign values
# for name and age.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Abdullahi Abdulwasiu", 22)
print(person.name)
print(person.age)
print(f"My name is {person.name} and I'm {person.age} years old")
print(Person) # return the class name

# Exercise 2: Create a class named Dog, Create 3 attributes, one should be class object atribute. Create a
# method named bark that print out the name of the dog.

class Dog:
    specie = 'mammal' # this is a class object attribute
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof my name is {}".format(self.name)) 

my_dog = Dog("Tiger", "Shepard")
my_dog2 = Dog("Bingo", "Shepard")
print(type(my_dog))


my_dog.bark()
my_dog2.bark()


# Exercise 3: Create an object that calculate the circumferance of a circle giving the formular pie*pie*r

class Cirle():
    pie = 3.142
    def __init__(self, radius):
        self.r = radius

    def my_circ(self):
        return self.r * self.pie**2

circumferance = Cirle(10)
print(circumferance.my_circ())



# Exercise 4: Calculate the area of the circle above giving the formular pie*r*r
class Cirle():
    pie = 3.142
    def __init__(self, radius):
        self.r = radius
        self.area = self.pie * self.r **2

circumferance = Cirle(10)
print(f"The area of circle is {circumferance.area}")


# Exercise 5: Calculate the area of square. Inheritance. Inherit from a base class and
# have access to it methods. Also overide a method from the base class

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

area_of_a_square = Square(10)
x = area_of_a_square.area()
print(x)

# Exercise 5: Calculate the distance between two lines and the slope of the lines 
# giving two Coordinates. (x1 x2) & (y1 y2). formula d=sqrt of (x2-x1)**2/(y2-y1)**2
 # slope = (x2-x1)/(y2-y1)
def Line():
    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2
        
    def my_distance(self):
        x1, x2 =  self.cord1
        y1, y2 = self.cord2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def my_slope(self):
        x1, x2 =  self.cord1
        y1, y2 = self.cord2
        return (x2-x1)/(y2-y1)

x_vals = (2,3)
y_vals = (3,2)
#my_line = Line(x_vals, y_vals)
#print(my_line.my_distance())
#print(my_line.my_slope())



# Exercise 5: Create a bank account class that has two attributes 'Owner' and 'balance' 
# and two methods for the attributes deposite and withdraw.

class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposite(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("withdrawal accepted")
        else:
            print("Sorry not enough funds!")

    def __str__(self):
        return f"Owner : {self.owner} \n Balance: {self.balance}"


a = Account("Mike",  1000)
a.owner
a.balance
a.deposite(100)

print(a)
a.withdrawal(1100)
a.withdrawal(50)