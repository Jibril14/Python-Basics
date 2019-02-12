# Python mapping type dictionary
# A dictionary is a colllection that is unordered, changeable and index
# Dictionary is written with a curly braces and has key value pair separated with colon

# Exercise 1: create a dictionary called person, with keys; first name
# last name and age
person = {
    "first_name": "Abdullahi",
    "last_name": "Abdulwasiu",
    "age": 22
}
print(person)

# Exercise 2: Accessing items in a dictionary with it key name. eg change the person age
person["age"] = 44
print(person)
print(person["first_name"])

# Exercise 3: Accessing items in a dictionary with the get() method
x = person.get("age") 
print(x)

# Exercise 4: Add gender, marital status, skills, country, city to the person dictionary
person.update({"gender": "male", 
            "marital status": "single", 
            "skills": ["Python", "JS", "React", "Sql"],
            "country": "Nigeria",
            "city": "Lagos"})
print(person)

# Or 
print("This is the second example 'below'")
person["gender", "marital status", "skills", "country", "city"] = "male", "single", "Python", "Nigeria", "Lagos"
print(person)

# Exercise 5: print person name and skills
x = person["first_name"]
y = person["last_name"]
z = person["skills"]
w = x + " " + y + " " + str(z)
print(w)

# Exercise 6: Make a copy of person dictionary with copy() method
person_copy = person.copy()
print(person_copy)

# Exercise 7: Create a Nested dictionary
children = {
    "child_1":{
        "name": "Andrew Coman",
        "age": 10
    },
    "child_2":{
        "name": "Jon Doe",
        "age": 7
    },
    "child_3":{
        "name": "Snow Gabza",
        "age": 5
    }

}
print(children)

# Exercise 8: Removing item from a dictionary
x = children.pop("child_3")
print(x)
print('now') 

# Exercise 9: Python Dictionary method keys() returns the keys of the dictionary as a list
print(children.keys())
x = children["child_1"].keys()
print(x)

# Exercise 10: values() method returns a list of all the values in a dic
print(children.values())

# Exercise 11: Looping through a dictionary to return it keys
for x in children:
    print(x)

# Exercise 12: Looping through a dic to return it values
for y in children:
    print(children[y])

# Exercise 13: Loop through both keys and values with the items() method
for x,y in children.items():
    print(x)

# Exercise 14: Creating dictionary through dictionary comprehension
my_dic =  {x:x**2 for x in range(5)}
print(my_dic)
