# print("Ya Allah meri madad Farma")
#
# databc = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
#
# counter = 1
# for i in databc:
#     print(f"{counter} = {i}: {ord(i)}")
#     counter = counter + 1

# Uploaded the questioner


# Let's rewrite to check the largest number
import pdb

# numbers = [23, 43, 54, 2, 89, 90, 44]

# largest = numbers[0]

# for i in numbers:
#     # breakpoint()
#
#     if i > largest:
#         largest = i
#
# print(largest)


# Let's understand Procedural vs Object-oriented programming

# Procedural: we write functions step by step and use them top to bottom

def get_user():
    return "I'm"

#
# def get_food():
#     return "Typing my order now"
#
#
# def place_order():
#     person = get_user()
#     food = get_food()
#     return print(f"Hi, {person} {food}")
#
#
# place_order()

#
# mystring = "Hello"
# myfloat = 4.863
# myint = 28
#
# if mystring == "Hello":
#     print("String: %s" % mystring)
#
# if isinstance(myfloat, float) and myfloat == 4.863:
#     print("Float: %f" % myfloat)
#
# if isinstance(myint, int) and myint == 28:
#     print("Integer: %d" % myint)
#
#
# print(...)


# print("Last print")



# mylist = [1,2,3]
# print(mylist[2])



# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = even_numbers, [odd_numbers]
# print(all_numbers)



# TODO: change this code

# x = object()
# y = object()


# print(x)
# x_list = [x]
# y_list = [y]
# big_list = [2,5]
#
# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))
#
#
# print(big_list.count(x))
# # testing code
# if x_list.count(x) == 1 and y_list.count(y) == 1:
#     print("Both lists have the same count of Items")
# if big_list.count(x) == 0 and big_list.count(y) == 0:
#     print("Great!")


# name = "John"
# print("Hello, %s!" % name)


# name = "John"
# age = 23
# print("%d is %s years old." % (age, name))


# mylist = [1,2,"uiu"]
#
#
# print("A list: %s" % mylist)


# data = ["John", "Doe", 53.44]
# format_string = "Hello"
#
# print(format_string % data)


# astring = "Hello world!"
# print("single quotes are ' '")
#
# print(len(astring))


# astring = "Hegto worldorld!"
# print(astring[0:9:2])


# statement = True
# another_statement = True
# if statement is True:
#     print("statements are true")
# elif another_statement is True: # else if
#     print("another_statements are true")
# else:
#     print('its all done')


# x = [1,2,3]
# y = [1,2,3]
# print(x == y) # Prints out True
# print(x is y) # Prints out False

# x = [1, 2, 3]
# y = [1, 2, 3]
#
# print(id(x))
# print(id(y))

#
# print(not False) # Prints out True
# print((not False) == (False)) # Prints out False


# change this code
# number = 10
# second_number = 10
# first_array = []
# second_array = [1,2,3]
#
# if number > 15:
#     print("1")
#
# if first_array:
#     print("2")
#
# if len(second_array) == 3:
#     print("3")
#
# if len(first_array) + len(second_array) == 3:
#     print("4")
#
# if first_array and first_array[0] == 1:
#     print("5")
#
# if not second_number:
#     print("6")


#
# numbers = [23, 43, 54, 2, 89, 90, 44]
#
# for prime in numbers:
#     print(prime)


# Prints out the numbers 0,1,2,3,4
# for x in range(5):
#     print(x)
# print("NOw")
# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x, end=' ')
#
# print("then")
# # Prints out 3,5,7
# for x in range(3, 8, 2):
#     print(x, end=" ")

# print("Hello", "how are you?", sep="---")



# count = 0
# while count < 5:
#     print(count, end=" ")
#     count += 1



# def flates_are():
#     print("This is First floor in this Flat")
#
# flates_are()


# def sum_two_numbers(a, b):
#     return a + b
#
#
# print(sum_two_numbers(34, 76))


# Modify this function to return a list of strings as defined above
# def list_benefits():
#     return ['convenient', 'reliable', 'smooth', 'usable']
#
# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return f"list is very {benefit}"
#
# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()



# class MyClass:
#     vab = "blah"
#
#     def myfunction(self):
#         vab = "chachu"
#         print(f"This is a message inside the class", self.vab)
#
# myobjectx = MyClass()
#
# myobjectx.myfunction()


# class MyClass:
#     variable = "blah"
#
#     def function(self=None):
#         variable = 'i am variable from function'
#         print("This is a message inside the class.", self.variable)
#         print("This is a message inside the class.", variable)
#
# myobjectx = MyClass()
#
# myobjectx.function()


# phonebook = {}
# phonebook["John"] = 938477566
# phonebook["Jack"] = 938377264
# phonebook["Jill"] = 947662781
# print(phonebook)


# phonebook = {"josi": 2341, "kon": 5431, "Same": 765 }

# del phonebook["josi"]
# print(phonebook)
# phonebook.pop("Same")
# print(phonebook)
# for name , number in phonebook.items():
#     print('Phone number of %s is %d' % (name, number))


# phonebook = {
#     "John": "32",
#     "Jake": 938377264,
#     "Jill": "32"
# }
# your code goes here

# testing code
# print(phonebook.values())
# if "32" in phonebook.values():
#     print("Jake is listed in the phonebook.")



# game.py
# import the draw module
# import draw
#
# def play_game():
#     return "I am playing"
#
# def main():
#     result = play_game()
#     draw.draw_game(result)
#
# # this means that if this script is executed, then
# # main() will be executed
# if __name__ == '__main__':
#     main()


# def surface_area_of_cube(data: float) -> int:
#     return 6 * data ** 2
#
#
# result = surface_area_of_cube(data = 4.6)
#
# print(result)



# from dataclasses import dataclass
#
# @dataclass
# class User:
#     name: str
#     age: int
#     email: str
#
#
# user = User("Haseem", 30, "waseem@example.com")
#
# print(user.name)
# print(user.age)
# print(user)


# class Car:
#     def __init__(self, name, price, email):
#         self.name = name
#         self.price = price
#         self.email = email



# from dataclasses import dataclass
#
# @dataclass
# class Vehicle:
#     name : str
#     price : float
#     email : str
#
# obj = Vehicle("Waseem", 30, "waseem@example.com")
# print(obj)
# print(obj.name)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
#
# print(len(list1), " ", list2, " ", list3)


# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# thislist = ["apples", "banana", "cherry"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[2:])


# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# print(type(thistuple))
# thislist.extend(thistuple)
# print(type(thislist))


# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.pop(2)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# i = 0
# print(range(len(thislist)))
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# parinto = [hu for hu in fruits if "an" in hu]
#
# print(parinto)

# newlist = [x for x in range(10)]
# print(range(10))
# print(newlist)

#
# numbers = [5, 2, 8, 1, 3]
#
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(numbers)


# numbers = [5, 2]
#
# j = 0
#
# numbers[j]     = 5
# print(numbers)
# numbers[j + 1] = 2
#
# print(numbers)



original = ["apple", "banana", "cherry"]

new_list = original.copy()

# print(new_list)

# print(object(original))


import copy

# original = [[1, 3], [7, 4]]
#
# shallow = copy.copy(original)
#
# shallow[0][0] = 100
# print("Shallow: ", original)
#
#
#
# deep = copy.deepcopy(original)
#
# deep[0][0] = 100

# print("Deep: ", deep)



# import copy
#
# original = [[1, 3], [7, 4]]
#
# shallow = copy.copy(original)
# deep = copy.deepcopy(original)
#
# shallow[0][0] = 100
# deep[0][0] = 200

# print("Original:", original)
# print("Shallow:", shallow)
# print("Deep:", deep)
#
#
# import copy
#
# original = [[1, 3], [7, 4]]
#
# shallow = copy.copy(original)
# deep = copy.deepcopy(original)
#
# print(id(original))
# print(id(shallow))
# print(id(deep))



import copy
#
# original = [[1, 3], [7, 4]]
#
# shallow = copy.copy(original)
# deep = copy.deepcopy(original)
#
# print("shallow: ", shallow, "deep: ", deep)
# print(original is shallow)       # False
# print(original[0] is shallow[0]) # True
#
# print(original is deep)          # False
# print(original[0] is deep[0])    # False



# import copy
#
# original = [[1, 2], [3, 4]]
#
# shallow = copy.copy(original)
# shallow[0].append(99)
# print(original)   # [[1, 2, 99], [3, 4]]  ← changed too!
#
# original2 = [[1, 2], [3, 4]]
#
# deeper = copy.deepcopy(original2)
# deeper[0].append(99)
# print(original2)   # [[1, 2, 99], [3, 4]]  ← changed too!



# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
#
# a = car.items()
# print("items: ", a)
#
# c = car.values()
# print("values: ", c)
#
# f = car.keys()
# print("keys: ", f)


# from functools import wraps
# import time
#
#
# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*arg, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*arg, **kwargs)
#         print("Result: ", result)
#         end_time = time.perf_counter()
#
#         total_time = end_time - start_time
#         return  result
#     return timeit_wrapper
#
#
# @timeit
# def calculate_something(num):
#     total = sum((x for x in range(0, num**2)))
#     return total
#
#
# if __name__ == '__main__':
#     calculate_something(10)




# def retry(thisone):
#     def wrapper(*args, **kwargs):
#         for attemp in range(1,4):
#             try:
#                 print("Try no: ", attemp)
#                 result = thisone(*args, **kwargs)
#                 return result
#             except Exception as e:
#                 print("Failed : ", attemp)
#
#         print("All 3 attempts failed")
#     return wrapper
#
# @retry
# def calculator(a, b):
#     print("sum: ", a*b)


# so = calculator(3,2)

# Context Managers will go here.

# class MyContext:
#
#     def __enter__(self):
#         print("Entering context")
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")
#
#
# with MyContext():
#     print("Hello from inside")


#
# def count_to_five():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# for number in count_to_five():
#     print(number)
#
# print("Now simple List...")
#
# def count_in_gisto():
#     return [1,2,3,4]
#
#
# for gist in count_in_gisto():
#     print(gist)



def normal():
    print("Creating list...")
    return [1, 2, 3]


def generator():
    print("Starting generator...")
    yield 1
    yield 2
    yield 3


print("NORMAL:")
x = normal()
print(x)

print("GENERATOR:")
y = generator()
print(next(y))
print("Done")