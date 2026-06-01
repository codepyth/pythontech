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

numbers = [23, 43, 54, 2, 89, 90, 44]

largest = numbers[0]


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


def get_food():
    return "Typing my order down"


def place_order():
    person = get_user()
    food = get_food()
    return print(f"Hi, {person} {food}")


place_order()
