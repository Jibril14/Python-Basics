# Python sequence type List
# Python list act as dynamic array
# A list is collection which is ordered and changeable
# python list contain any datatype and is writting with a square bracket

# Exercise 1: Example of a list
items = ["Apple", "Banana", "Guava", "Mango"]

# Exercise 2: Print out elements in a list
item = ["Apple", "Banana", "Guava", "Mango"]
print(item)

# Exercise 3: Accessing element of a list (eg print out Lettuce)
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Lettuce', 'Onion', 'Carrot']
x = vegetables[3]
print(x)

# Exercise 4: Range indexing (eg print out last two elements)
print(vegetables[-2:])

# Exercise 5: Change element of a list (list is mutable unlike string, tuple etc elements)

tech_skills = ['HTML', 'CSS', 'JS', 'React','Redux', 'Python', 'Sql']
tech_skills[4] = 'Angular'
print(tech_skills)

# Exercise 6: To check if an item exist in a list
x = "Python" in tech_skills
print(x) 

if "React" in tech_skills:
    print("I'm also a React Developer")
else:
    print("Not a React Developer")

# Python list support a number of python built in methods
# Exercise 6: get the number of item in a list
tech_skills = ['HTML', 'CSS', 'JS', 'React','Redux', 'Python', 'Sql']
print(len(tech_skills))

# Exercise 7: append() method add an item to the end of a list
countries = ["Nigeria", "Ghana", "Kenya","Rwanda", "Algeria", "Egypt", "Cameroon"]
countries.append("Senegal")
print(countries)

# Exercise 8: extend() method add elements from one list to the end of another list
items_1 = ["Phone", "Watch"]
items_2 = ["PC", "Airpod", "Shoe"]
(items_1.extend(items_2))
print(items_1)


# Exercise 9: Join or Concatenating two or more list
items_3 = ["Headset", "Charger", "Camera"]
print(items_1 + items_3)

# Exercise 10: sort() method arrange list items alpabetically'/ ascending order
fruits = ['banana', 'orange', 'mango', 'apple', 'lemon']
fruits.sort()
print(fruits)

# Exercise 11: count() method return the number of specify element in a list
fruits = ['banana', 'orange', 'apple', 'mango', 'apple', 'lemon']
print(fruits.count("apple"))#returns 2

# Exercise 12: pop() method remove element at a specified position. by default last element
# pop() method return the removed item from a list

grade = [98, 80, 70, 40, 76, 65]
print(grade.pop(3))
print(grade.pop())

# Exercise 13: remove() method remove element with specified value. by default last element
grade = [98, 80, 70, 40, 76, 65]
grade.remove(40)
print(grade)

# Exercise 14: index() method return the index of the first occurence of element specified
fruits = ['banana', 'orange', 'kewi', 'apple', 'mango', 'apple', 'lemon']
print(fruits.index("apple"))

# Exercise 15: insert() method add element to a specified index.
fruits = ['banana', 'orange', 'kewi', 'apple', 'mango', 'apple', 'lemon']
fruits.insert(0, "cashew")
print(fruits)

# Exercise 16: reverse() method Reverse the order of the string ie descend it
fruits.reverse()
print(fruits)

# Exercise 17: clear() method remove all elements from a list
fruits.clear()
print(fruits)

# Exercise 18: del() method delete the list completely
del fruits

# Exercise 19: list() method or constructor to make a list
x = "apple", "banana", "guava", "chery"
y = list(x)
print(y)

# Exercise 20: unpacking list
data = ['Vitaline', 'Messi', ('Dec', 7, 1978)]
first_name, last_name, date_of_birth = data 
print(f'His name is' + " " + first_name + " " + last_name )
print(date_of_birth)