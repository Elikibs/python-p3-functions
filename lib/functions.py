#!/usr/bin/env python3

# Function 1
def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

# Function 2
def greet(name):
    print(f"Hello, {name}!")

greet("Elisha")

# Function 3
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Maureen")

# Function 4
def add(num1, num2):
    return num1 + num2

print(add(3, 4))

# Function 5
def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

print(halve(6))