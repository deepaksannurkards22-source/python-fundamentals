print("Hello world!!")

print("Day 1. Let's go!!")

#Variable
name = "Deepak"
age = 24
height = 5.9
is_learning = True

print(name)
print(age)
print(type(age))
print(type(height))
print(type(is_learning))

#Input/Otput
user_name = input("Enter your name:")
print("Welcome to data science.",user_name)

a = 10
b = 3

print(a+b) #addition
print(a-b) #Subtraction
print(a*b) #multiplication
print(a/b) #division 
print(a//b) #floor division
print(a%b) #modulo - remainder
print(a**b) #power

#1.Simple Calculator:
#Ask user to enter two numbers
#print their sum, differnce, product, and division result

num1 = int(input("Enter the first num:"))
num2 = int(input("Enter the second num:"))

sum = (num1 + num2)
difference = (num1 - num2)
product = (num1 * num2)
division = (num1 / num2)

print(sum)
print(difference)
print(product)
print(division)

#2.Temperature Converter:
#Ask user to enter temperature in Celsius
#Convert to Fahrenheit: F = (C × 9/5) + 32
#Print the result with a clear message

temp = input("enetr the temprature in celsius:")
CelsiusTemp = float(temp)

FahrenheitTemp = (CelsiusTemp * (9/5))+32

print("The tempertaure in Fahrenheit is:",FahrenheitTemp)

#3.Area Calculator:
#Ask user for length and width of a rectangle
#Print the area and perimeter

L = float(input("Enter the lengeth:"))
W = float(input("Enter the width:"))

Area = L * W
Perimeter = 2 * (L + W)
print("The Area of a rectangle is:",Area)
print("The Perimeter of a rectangle is:",Perimeter)


#4.Swap two variables:
#Take two variables: a = 5, b = 10
#Swap their values WITHOUT using a third variable
#Print the result
#(Hint: Python lets you do this in one line — figure out how)

a = 5
b = 10

a, b = b, a

print("a =",a)
print("b =",b)



#5.Simple Interset Calculator:
#Ask user for Principal, Rate, and Time
#Calculate Simple Interest: SI = (P × R × T) / 100
#Print the result

P = float(input("enter the Principal:"))
R = float(input("enter the rate:"))
T = float(input("enter the time:"))

SI = (P * R * T)/100

print("The Simple Intrest is:",SI)
