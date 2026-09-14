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


phonebook = {
    "John": "32",
    "Jake": 938377264,
    "Jill": "32"
}
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


def surface_area_of_cube(data: float) -> int:
    return 6 * data ** 2


result = surface_area_of_cube(data = 4.6)

print(result)