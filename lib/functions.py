#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# def greet_with_default(name):
#     print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

    result = add(45 + 55)
    print(result)

def halve(number):
    return number / 2


greet_programmer()              # Should print: Hello, programmer!
greet("Alice")                  # Should print: Hello, Alice!
greet_with_default()            # Should print: Hello, programmer!
greet_with_default("Bob")       # Should print: Hello, Bob!
print(add(3, 4))                # Should print: 7
print(halve(10))                # Should print: 5.0