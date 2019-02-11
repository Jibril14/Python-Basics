# Python set type
# A Set is a collection which is unordered, unchangeable and unique element only
# We cannot change an item in a set but we can add new items
# Set is writing with a curly braces {}

# Exercise 1: Create of a set
items = {"Apple", "Banana", "Guava", "Mango"}
print(type(items))

# Exercise 2: Add an item to a set
# Since sets are unordered, we can never be sure in which order the items will appear
items.add("Kewy")
print(items)

# Exercise 3: Removing items from a set
items = {"Apple", "Banana", "Guava", "Mango"}
removed_item = items.pop()
print(removed_item)
print(items)

# Exercise 4: Removing item with remove() and discard() method
items.remove("Banana")
items.discard("Mango")
print(items)

# Exercise 5: Check the length of a set. Return 4 since set store only unique values 
fruits = {'banana', 'orange', 'mango', 'lemon','lemon' }
x = len(fruits)
print(x)

# Exercise 6: Empty a set with the clear() method
y = fruits.clear()
print(fruits) 

# Exercise 7: Delete the whole set
del fruits
# print(fruits) return fruit not define

# Exercise 7: Set constructor, create a set from another data type
items = ["Apple", "Banana", "Guava", "Mango"]
item = set(items)
print(item)

# Exercise 8: Join two set with the union() or update() method. this returns a new set consiting of the joined sets
set1 = {'item1', 'item2', 'item3', 'item4'}
set2 = {'item4', 'item5', 'item6'}
set3 = set1.union(set2)
print(set3)

# Exercise 9: Join two set with the difference() method. this method never return the duplicate
set1 = {'item1', 'item2', 'item3', 'item4'}
set2 = {'item4', 'item5', 'item6'}
set3 = set1.difference(set2)

# Exercise 10: Check if items in one set is unique to that set only. return true
fruits_1 = {'banana', 'orange', 'mango' }
fruits_2 = {'lemon', 'guava', 'banana' }
z = fruits_1.isdisjoint(fruits_2)
print(z)