#!/usr/bin/env python3
import math

def admin_login(username, password):
    # your code here
    if username.lower() =="admin" and password =="12345":
        return "Access granted"
    else:
        return "Access denied"
    

admin_login("sudo", "12345")
admin_login("admin", "12345")
admin_login("ADMIN", "12345")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        response = "brisk"
        return f"It's {response} out there!"
    elif 40 <= temperature <= 65:
        response = "a little chilly"        
        return f"It's {response} out there!"
    elif temperature > 85:
        response = "too dang hot"
        return f"It's {response} out there!"
    else:
        response = "perfect"
        return f"It's {response} out there!"


hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0 and num% 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    else:
        return num
    
    
fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)


def calculator(operation, num1, num2):
    # your code her
    if (operation == "+"):
        return num1 + num2
    elif (operation == "-"):
        return num1 - num2
    elif (operation == "/"):
        return num1 / num2
    elif (operation == "*"):
        return num1 * num2
    else:
        print("Invalid operation!")
        return None
    
calculator("*",1,2)