# Python sequence type tuple 
# A tuple is a collection  which is ordered and unchangeable
# tuple is writen in round bracket

# Exercise 1: create a tuple
item = ("Apple", "Banana", "Mango", "Guava")
print(item)

# Exercise 2: indexing and accesing items in tuples
item = ("Apple", "Banana", "Mango", "Guava")
print(item[1:3])

# Tuples are unchangeable, but we can convert the tuple into a list, change
# the list and convert the list back into a tuple
# Exercise 3: Change the third element in the tuple
item = ("Apple", "Banana", "Mango", "Guava")
items_1 = list(item)
items_1[0] = "lemon"
item = tuple(items_1)
print(item)

# Tuples support a number of built in python methods
# Exercise 4: Print the number of elements in a tuple
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Potato', 'Lettuce', 'Onion', 'Carrot')
print(len(vegetables))

# Exercise 5: count() method, count a specify item
print(vegetables.count("Potato"))

# Exercise 6: Index() Return the index of the first element with the specified value
vegetables = ( 'Potato', 'Cabbage', 'Lettuce', 'Potato', 'Onion', 'Carrot')
x = vegetables.index("Potato")
print(x)

# Exercise 7: Tuple constructor
grade = 80, 90, 66, 98
x = tuple(grade)
print(x)

# Exercise 8: Tuple unpacking
data = ("Abdullahi", "Abdulwasiu", (12, "Jan", 1986))
first_name, last_name, (day, month, year) = data
print(first_name +" "+ last_name + " "+ month)
print(first_name +" "+ last_name + " "+ (month))#same thing









