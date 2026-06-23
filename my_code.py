#Assignment Problems
#1.Write a program that asks the user for their name and age, then prints a sentence like:
user_name = input("enter your name:")
age = input("enetr your age:")

print("Hello",user_name,",you are",age,"years old!")


 
#2.Take two numbers as input from the user and print their sum, difference, product, and quotient
x = float(input("enter any num1:"))
y = float(input("enetr any num2:"))

sum = (x+y)
difference = (x-y)
product = (x*y)
quotient = (x%y)

print(sum)
print(difference)
print(product)
print(quotient)

#3.Ask the user to enter two integers and one float. Convert them all to floats and print their average
a = int(input("enter any integer num1:"))
b = int(input("enetr any integer num2:"))
c = float(input("enetr a float value:"))

sum = float(a+b+c)
avg = sum/3

print("The Average is:",avg)

#4.The user enters a string containing a number (eg., "45").Convert it to:
# an integer,
# a float,
# a string again and 
# Print all three values with their types.
a = input("enter any num:")
b = int(a)
c = float(b)
d = str(c)

print(b,type(b))
print(c,type(c))
print(d,type(d))

#5.Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2
x = 10 + 3 * 2 ** 2

print(x)# As because the precedence value the highest predence will get solved first that why>>>

#6.Write a program to swap values of two numbers entered by the user.






#7.Ask the user for a temperature in celsuis (string input).Convert it to float, then calucate and print temperature in Fahreneit.
#conversion formula: FahrenheitTemp = (CelsiusTemp*(9/5))+32
temp = input("enetr the temprature in celsius:")
CelsiusTemp = float(temp)

FahrenheitTemp = (CelsiusTemp * (9/5))+32

print("The tempertaure in Fahrenheit is:",FahrenheitTemp)


#8.take the radius (r) as user input and print the area.
#Use theformula; Area = pi*r^2. (value of pi = 3.14)

r = float(input("enetr the radius:"))
PI = 3.14
Area = PI * (r**2)

print("The Area is:",Area)


#9.Ask the user for : Principal(P),Rate(R),Time(T).Convert all to float and compute simple intrest:
#SI = (P*R*T)/100

P = float(input("enter the Principal:"))
R = float(input("enter the rate:"))
T = float(input("enter the time:"))

SI = (P*R*T)/100

print("The Simple Intrest is:",SI)


#10.Take a decimal  number as input (like 45.78 )and output is:
#integer part - 45
#fractional part - .78

x = float(input("enetr a decimal number:"))
x1 = int(x)
x2 = float(x-x1)
print("The integer part is:",x1)
print("The fractional part is:",x2)




