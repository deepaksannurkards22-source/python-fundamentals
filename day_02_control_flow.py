# if/elif/else:

age = int(input("enter your age: "))

if (age < 18):
    print("you are a minor")
elif (age >= 18 and age < 60):
    print("you are an adult")
else:
    print("you are a senior citizen")

# For loop:

#Print numbers 1 to 10
for i in range(1, 11):
    print(i)

#Print each character in a string
name = "Deepak"
for char in name:
    print(char)

#While loop:

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  #Without this line , infinite loop

# Nested if inside loop:

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

#Program 1 — FizzBuzz (a classic, shows up in actual interviews):
#For numbers 1 to 30:
#- If divisible by 3: print "Fizz"
#- If divisible by 5: print "Buzz"
#- If divisible by both: print "FizzBuzz"
#- Otherwise: print the number

n = int(input("Enter any num:"))

if n % 3 == 0:
    print("Fizz")

if n % 5 == 0:
    print("Buzz")

if (n % 3 == 0 and n % 5 ==0):
    print("FizzBuzz")

else:
    print(n)


#Program 2 - Grade Calculator:
#Ask user to enter marks (0-100)
#If marks >= 90: print "Grade A"
#If marks >= 75: print "Grade B"
#If marks >= 60: print "Grade C"
#If marks >= 40: print "Grade D"
#Below 40: print "Fail"

marks = int(input("Enter the marks:"))

if  (marks >= 90):
    print("Grade A")
if  (marks >= 75):
    print("Grade B")
if  (marks >= 60):
    print("Grade C")
if  (marks >= 40):
    print("Grade D")

else: 
    print("Fail")



#Program 3 - Number Guessing game:
#Set a secret number (e.g. secret = 7)
#Ask user to guess
#If guess is correct: print "You got it!"
#If guess is too high: print "Too high"
#If guess is too low: print "Too low"
#(Use a while loop so they keep guessing until correct)

secret = 7
guess = int(input("Guess a number:"))

if  (guess == secret):
    print("you got it!")
if  (guess >> secret):
    print("too high")
if  (guess << secret):
    print("too low")
else:
    i = 1
    while i == 7:
        print("No you gueesed it wrong")