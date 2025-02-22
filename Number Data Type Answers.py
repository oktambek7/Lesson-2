# 1.Create a program that takes a float number as input and rounds it to 2 decimal places.
num = float(input("Enter a float number: "))
rounded_num = round(num, 2)
print(f"The number rounded to 2 decimal places is: {rounded_num}")

#2.Write a Python file that asks for three numbers and outputs the largest and smallest.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")

#3.Create a program that converts kilometers to meters and centimeters.

kilometers = float(input("Enter the distance in kilomters:"))
meters = kilometers * 1_000 
centimeters = kilometers * 100_000
print(f"{kilometers} kilometers is equal to {meters} meters and {centimeters} centimeters.")

#4.Write a program that takes two numbers and prints out the result of integer division and theremainder.

a=int(input("enter a number:"))
b=int(input("enter a number:"))
print(a%b)

#5.Make a program that converts a given Celsius temperature to Fahrenheit.
celsius = float(input("Enter the temperature in Celsius: "))
farenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {farenheit} degrees Farenheit. ")

 #6. Create a program that accepts a number and returns the last digit of that number.

number = int(input("Enter a number"))
last_digit = abs(number) % 10
print(f"The last digit of {number} is {last_digit}.")

#7. Create a program that takes a number and checks if it’s even or not.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number. ")
else:
    print(f"{number} is an odd number. ")
