"""
LET'S REWIND WHAT FUNCTIONS DO WE KNOW SO FAR AND LEARN WHAT WE CAN DO
"""

# We've used, for example, PRINT() which will perform a specific action with the value that we enter.
print("Hola Mundo")
print("DONE")

# We can create our own functions with def: def FunctionName(ValueToBeIntroduced): WhatWeWantToDo


def hola():
    print("Hola Mundo!")
    print("Ultimate Python")
    print("Welcome Eduardo")


hola()

# Parameters


def hello(name):  # Here we introduced a value within the parentheses.
    print("Hello World!")
    print(f"Welcome {name}")


# Adding that previous value within the parentheses turned the function into an OBLIGATORY-variable function, so the function will always have to be called along with a variable. If not, then the call of the function won't work.
# hello() -- Error

hello("eduardo")
hello("Xyzzz")

# IMPORTANT: The value that we put within the def value parentheses is called PARAMETER.
# When you call the function and introduce a custom value within a def function parentheses, it becomes an ARGUMENT.

# Several parameters: When you create a function, you can configue it so it mandatorily receives a certain number of desired arguments.


def bonjour(nom, age):
    print(f"Ton nom est {nom} et ton âge est {age}")


# bonjour("eduardo") -- Error

bonjour("eduardo", 29)
