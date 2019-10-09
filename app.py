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
if user_answer == "y" or "Y":
    print("Sounds great, let's go")
elif user_answer == "n" or "N":
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
