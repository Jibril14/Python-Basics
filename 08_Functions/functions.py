# A function is a block of code which only runs when it is called
# We can pass data known as parameters into a function
# a function can return a data as a result.




# Exercise 1: Write a function to check if a single number is an even
def my_check(x):
    return x % 2 == 0
print(my_check(31))

# Exercise 2: Write a function that calculate my age base on current year and birth year
def cal_age(cur_year, birth_year):
    age = cur_year - birth_year
    return age
print("My Age:", cal_age(2018, 2017))

# Exercise 3: Write a function to return all the even number in a list
def myfunc(nums):
    myeven = []
    for  x in nums:
        if x % 2 == 0:
            myeven.append(x)
    return myeven
print(myfunc([1,2,3,4,5,6,]))

# Exercise 4: Write a function to check the employee that work for most of the hour
# giving name and work hour in the list. Hint [(name, workhour)]
def my_func(work_hour):
    current_hour = 0
    employee_of_month = ""

    for employee, max_work_hour in work_hour:
        if max_work_hour > current_hour:
            current_hour = max_work_hour
            employee_of_month = employee
        else:
            pass
    return current_hour, employee_of_month
    
data = [("John", 4000),("Ana", 2000), ("Banabas",6000), ("Abdullahi", 200)]
print(my_func(data))


# Exercise 6: Giving a list of ints, return True if the Array contains a 3 next to a 3 somewhere.

def my_list(lst):
    for i in range(0, len(lst)-1):
        if lst[i]==lst[i+1]:
            return True
    return False
print(my_list([1,2,3,4,55]))


# Exercise 7: Giving a string, return a string where for every character in the 
# original make it each character to be tripple.

def my_func(text):
    my_triple = ""
    for x in text:
        my_triple += x*3
    return my_triple
print(my_func("boy"))

# Exercise 8: Write a function that return a giving sentence in a reverse. eg boy hood is sweet = sweet is hood boy 

def rev_sentence(sen):
    words = sen.split()
    words_rev = words[::-1]
    words_join = " ".join(words_rev)
    return words_join
print(rev_sentence("sweet"))


def rev_sentence2(sen2):
    return " ".join(reversed(sen2.split()))
print(rev_sentence2("boy hood is sweet"))



# Exercise 9: Write a function that convert a temperature degree in celcius to degree in ferenheit
def convert_temp(cel):
    return str(32 + (9/5) * cel) + "°F"
print(convert_temp(10))


# Exercise 10: Area of a Room; Write a program that asks the user to enter the width and length
# of a room as ﬂoating point numbers. , then display the area of the room.

def area_room(width, length):
   
    return width * length
def main():
    x = float(input("Please Enter the width in meters: "))
    y = float(input("Please Enter the length in meters: "))
    print(area_room(x, y))
if __name__ == "__main__":
    main()


# Exercise 11: Write a function or phrase that check weather a word or phrase is a palindrone
# A palindrone is a word or phrase that read the same backward as forward eg "popo", "nurses run"

def palindrone(word):
    word = word.replace(" ", "")
    return word == word[::-1]
print(palindrone("nurses run"))
print(palindrone(['m', 'a', 'd','a', 'm'])

# Example 2
text = input("Enter word or phrase:")
palindrone = True

for i in range(0, len(text) //2):
    if text[1] != text[len(text)-1-1]:
        palindrone = False

if palindrone:
    print("yes")
else:
    print("Not a palindrone")

def sum_numbers(nums):  # normal function
    return sum(nums)
def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    #ie apply f to lst
    print(summation)#15
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) 

