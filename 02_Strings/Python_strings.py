
# String literal in python is surrounded by either single or double quote
# Literals are display with the prin() function eg print("Hi")


# Exercise 1: Write a string with single quote
x = 'I am a boy'
print(x)

# Exercise 2: Write a multi-line string with three single or double qoute
y = '''Apple,
       Banana,
       Chery'''
print(y)

# Exercise 3: Use different quote inside of a string
x = "Dome is the 'salt' of the ground"
print(x)  

# Exercise 4: String Concatenation
x = "The girl"
y = "is beautiful!"
z = x + " " + y
print(z)

# String indexing and slicing
# square bracket can be use to access elements of a string
# Exercise 5: Return the sixth element of the string 

a = "Hello World"
print(a[6])

# Exercise 6: Get the 3th to 7th element
print(a[3:8])

# Exercise 7: Negative Indexing, print from 3nd to the last to first element
print(a[-8:6]) 

# Exercise 8: Get the last 3 elements
print(a[-3:]) 

# Exercise 9: The len() function can be use to return the length of a string
print(len(a))

# String Methods
# Python has a set a string method which we can use on string eg capitalize(), strip()

# Exercise 10: Strip method removes any white spaces from beginning or string end
x = "   Hello World! "
print(x.strip())

# Exercise 11: Convert the first letter of a string to a Capital letter
string = 'hello world'
print(string.capitalize()) 

# Exercise 12: Replace a letter of a string
string = "Nike"
x = string.replace("N", "M")
print(x) 

# Exercise 13:String cannot be mutate. ie change part of a string
'''x = "Nike"
y = x[0] = "M" ''' #error

# Exercise 14: Instead use the replace mehod or string concatenation
x = "Nike"
y = x[1:]
z = "M"
print(z + y)

# Exercise 15: Reversing a string in python
x = "ekiN"
print(x[::-1]) 

# Exercise 15: Use the split function to split up a string into strings
x = "Hello,People,of the World"
y = x.split(",")
print(y)

# Exercise 16: Check if a word is in a String
x = "The boy said he is a Nigerian"
y = "said" in x
print(y) #return true

# Exercise 17: Format a number into a String
age = "10" #N.b age is string
x = "Garba started school at the age of" + " " + age
print(x)

# Exercise 18: We can use the format method to format a number into a string
Money = 5000
a = "Give me {}$ for the job"
x= a.format(Money)
print(x)

print("I will take {}N per month".format(Money))

# Exercise 19: Formated string literal or f Strings
name = "Abdullahi Abdulwasiu Jibril"
age = 22
print(f"My name is {name} and i'm {age} years old!") 

# Exercise 20: Older method of string formating using % character
print("im going to inject %r here"  % 'Mbappe')

# Exercise 21: String formating
chaoclates = 5
candies = 2
price = 10 
my_order = "I need {1} chaocolates and {2} candies for {0}$"
print(my_order.format(price, chaoclates, candies))
# Some characters are illegal inside of a string. we use \ follow by the char

# Exercise 22: Escaping special character eg  double quote in another double quote a string
print("We are the so-called \"Pythonister\" from the Motherland")


