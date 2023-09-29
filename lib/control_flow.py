#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "admin" or username == "ADMIN" and password== "12345":
        return "Access granted"
    else :
        return "Access denied"

print(admin_login("sudo", "12345"))
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))
print(admin_login("ADMIN", "sudo"))
print(admin_login("sudo", "pls"))
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        response = "brisk"
    elif temperature > 40 and temperature < 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
        
    return (f"It's {response} out there!")

print(hows_the_weather(33))
print(hows_the_weather(50))
print(hows_the_weather(99))
print(hows_the_weather(75))


def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(5))
print(fizzbuzz(15))

    

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "a":
        return None
    else:
        print(f"Invalid operation!")
    # return "None"
        
print(calculator("+", 3, 5))
print(calculator("-", 8, 5))
print(calculator("*", 2, 5))
print(calculator("/", 10, 5))        
print(calculator("nope", 3, 5))
    
