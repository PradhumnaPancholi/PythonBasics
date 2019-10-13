# this is me trying to learn python
# getting hang of syntax and basics quickly coz tutorials are boring and toooo basic
# I hope this works out, I don't even know how to comment out things

print("Hello Python 3")  # the classic

# all the basics things are pretty similar to javascript instead of naming convention and defining variable
# Here is the example,
language_name = "Python"

# Note:-
# 1.Python uses Snake Case for naming convention instead of Pascal or Camel Case
# 2.No use or "var", "let", or "const" to define variable

# Example to take user input (from console)
user_name = input("Please enter your name: ")
user_answer = input(user_name + ", Are you excited to learn Python? Y/N : ")

# Example of Else If
if user_answer == "y" or user_answer == "Y":
    print("Sounds great, let's go")
elif user_answer == "n" or user_answer == "N":
    print("Well, your choice if you wanna quit")
else:
    print("Not a valid input, pal")

# Note :-
# 1. Slightly different syntax but very readable and smooth transition
# 2. For "And", "Or ", and "And" operators, actual keywords are used instead of special characters

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

# A simple Calculator

num_1 = input("Please enter a number : ")
num_2 = input("Enter another number : ")
result = float(num_1) + float(num_2)
print("Result : " + str(result))

# What I learned/used :-
# 1. taking user inputs
# 2. data types and parsing in python (just same as any other language)

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

# A simple/small madlib game.

love_thing = input("Enter a thing that taught you love : ")
patient_thing = input("Enter a thing that taught you patient : ")
pain_thing = input("Enter a thing that taught you pain : ")

print(love_thing.capitalize() + " taught me love")
print(patient_thing.capitalize() + " taught me patient")
print(pain_thing.capitalize() + " taught me pain")

# What I learned :- Basically to generate a meaningless madlib(actually meme) using python

# ----------------------------------------------------------------------------------------------------------------------------------
# Arrays
# ----------------------------------------------------------------------------------------------------------------------------------

# one can store anything in array just like any other programming language
heroes = ["iron man", "captain america", "wolverine", "doctor strange", "thor"]
guardians = ["groot", "rocket", "star lord", "gamora", "mantis", "drax"]
print(heroes)
print(heroes[0])
print(heroes[2:])
print(heroes[2:4])

heroes.extend(guardians)
print(heroes)

heroes.append("spider man")
print(heroes)
heroes.insert(4, "black widow")
print(heroes)
heroes.remove("gamora")
print(heroes)
heroes.count("iron man")
print(heroes)
heroes.pop()
print(heroes)
heroes.clear()
print(heroes)


# ----------------------------------------------------------------------------------------------------------------------------------
# Tuples
# ------------------------------------------------------------------------------------------------------------------------------------

coordinates = (23.767767676, 3.658)
print(coordinates[0])

# tuple is just way to store a list which is immutable - cannot be modified//


# -----------------------------------------------------------------------------------------------------------------------
# Functions

def get_cube(num):
    return num*num*num

print(get_cube(3))

# functions just like any other programming languages

# -----------------------------------------------------------------------------------------------------------------------
# Dictionaries

months_dictionary  = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May", # jokes on me
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(months_dictionary.get("Oct"))
print(months_dictionary["Oct"])

# -----------------------------------------------------------------------------------------------------------------------
# Loops

# 1. While loop - built a simple guessing game

secret_word = "theoffice"
user_guess = ""
guess_limit = 3
guess_index = 0
guesses_ran_out = False

while user_guess != secret_word and not(guesses_ran_out):
    if guess_index < guess_limit:
        user_guess = input("Enter your guess: ")
        guess_index += 1
    else:
        guesses_ran_out = True

if guesses_ran_out:
    print("Better luck next time")
else:
    print("You Won!!!")


# 2. For Loop - just printing things off

friends = ["Chandler", "Joey", "Pheobe", "Monica", "Ross", "Rachel"]

for friend in friends:
    print(friend)

# ----------------------------------------------------------------------------------------------------------------------
# TRY - EXCEPT
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as error:
    print(error)
# except:
#     print("Invalid Input")
# not giving any "type" of exception will cause into catching any error and that something a good dev shouldn't do.

# ----------------------------------------------------------------------------------------------------------------------
# Dealing with Files
# this is most interesting part

# you have 4 options while handling a file
# 1. w  - write
# 2. r  - read
# 3. a  - append
# 4. r+ - read & write

# Reading a file
friends_file = open("friends_list.txt", "r")
print(friends_file.readlines())
friends_file.close()

# Writing a file
central_perk_employees_file = open("central_perk_employees.text", "w")
central_perk_employees_file.write("Gunther - Probably owner")
central_perk_employees_file.close()
# Note- writing on an existing file will end up overwriting a data, if you want to add data, use append

# Appending  a file
friends_file = open("friends_list.txt", "a")
friends_file.write("\nMike - Pianist")

