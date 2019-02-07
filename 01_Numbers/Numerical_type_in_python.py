# Python Numerical type are Integer, Float and Complex
# Integer are positive or negative whole number without decimal
# e.g -4, 654, 2001, -90000081

# Floating point numbers are positive or negative numbers containing decimal
# e.g 44.5, -8764.1, 2.5, 4.6e100 (4.6*10e100)

# Complex numbers are numbers writing with "J" as the imaginary part
# eg 2 + 5j,  -16j, 12j




# Exercise 1: Addition of two numbers
x = 2
y = 3
print(x+y)

# Exercise 2: Addition of two numbers
num_one = 30.2
num_two = 20
result = num_one-num_two
print(result)

# Exercise 3: Addition of two numbers
x = 10
x += 5
print(x)

# Exercise 4: Division of numbers
print(50/10)
print(y)

# Exercise 5: Floor division of numbers
x = 100
y = 25
print(x//y)
# N.b Variable name x have been re-define multiple time 
# Variables once declared can be redeclear again in python.

# Exercise 6: Multiplication of numbers
print(2*10*4)

# Exercise 7: Exponential 

x = 2
y = 3
z = x**y
print(z)

# Exercise 8: Modulus

x = 10
y = 3
print(x%y)


# Exercise 9: Complex Number
x = 3 + 4j
y = 4 + 5j
print(x-y)

# Exercise 10: To verify the type of any object in Python
x = 4j - 9
print(type(x))

# Converting from one type to another
# Exercise 11: Convert int to a float
x = 5
y = float(x)
print(y)

# Exercise 12: Converting float to an int
x = 5.4
t = int(x) ## return 5
print(type(t)) ## return int

# Exercise 13: Complex float to Complex
x = 5.5
y = complex(x)
print(y)

# Some python built in Functions use for numbers eg print(), float() etc
# Exercise 14: abs() function returns absolute value of a number
num = -4.5
num_abb = abs(num)
print(num_abb)

# Exercise 15: Return absolute value of a complex number
x = 3 - 4j
print(abs(x))

# Exercise 16: bin function return the binary version of a number(requires an int)
x = 32
print(bin(x))

x = 64
print(bin(x))

# Exercise 17: Convert a string to a float
x = "12"
y = float(x)
print(y)

# Exercise 18: pow() function return a power of a number
x = -4.4
y = pow(x, 2)
print(y)

print(pow(3, 2, 5)) # (3**2)%5

# Exercise 19: round() function round a number up. Zero decimal places by default
x = 3.66644
z = round(x)
print(z)

print(round(x, 2)) # 2 decimal places
# Compairing round with floor below 

import math  
print(math.floor(x)) # round a number down to nearest whole number




# Python Built in Math function can be use to perform operations on numbers
# We can import the math module and start using it methods

# Exercise 20: math.sqrt() methods returns the square root of a number
import math
x = math.sqrt(25)
print(x)

# Exercise 21: math.pi returns the pi value
r = 2
area = math.pi * (r*r)
print(area)

# Exercise 22: math.ceil() method round a number upward to nearest integer
print(math.ceil(5.8))


# Exercise 23: Find the Cosine of 90
import math
print(math.cos(90))

# Exercise 24: Find the arc sin of x ie asin(x)
x = 0.8664
print(math.asin(x))

# Exercise 25: Float formating ie 2 decimal places
x = 2/3
print("Result is {val:2.2}".format(val=x))

# Exercise 26: Take two input from user and comput their sum
x = input("Fist Num:" )
y = input("Second Num:" )
z = float(x) + float(y)
print(z)