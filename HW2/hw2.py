
print("#2.3") #printing problem number
#2.3
grade = 95     #creating a value for grade because the exercise didn't give one
if grade >= 90:
    print(f"Congrate! You're grade is {grade}!") #printing a congrats message then the grade


print("\n#2.4") #blank line and exercise number
#2.4
#Display all results for arithmetic operators for 27.5 and 2
print("27.5 + 2 = ", 27.5 + 2)
print("27.5 - 2 = ", 27.5 - 2)
print("27.5 * 2 = ", 27.5 * 2)
print("27.5 ** 2 = ", 27.5 ** 2)
print("27.5 / 2 = ", 27.5 / 2)
print("27.5 // 2 = ", 27.5 // 2)

print("\n#2.5") #blank line and exercise number
#2.5
#creating variables for future arithmetic
radius = 2  #Turns out with a radius of 2 the circumference and area are the same
pi = 3.14159

#performing arithmetic
diameter = 2 * radius
circumference = 2 * pi * radius
circle_area = pi * radius * radius

#printing results
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Circle Area:", circle_area)

print("\n#2.6") #blank line and exercise number
#2.6
#getting a number
num = int(input("Please input an integer: "))

#determining and printing if it's odd or even
if num % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")


print("\n#2.7") #blank line and exercise number
#2.7
num1a = 4
num1b = 1024
num2a = 10
num2b = 2.5


#if/else statements used to find if the number is cleanly divisible by the other to determine if it is a multiple of that number
#num1
if num1a % num1b != 0:
    print(f"{num1b} is a multiple of {num1a}")
else:
    print(f"{num1b} is not a multiple of {num1a}")

#num2
if num2a % num2b != 0:
    print(f"{num2b} is a multiple of {num2a}")
else:
    print(f"{num2b} is not a multiple of {num2a}")


print("\n#2.8") #blank line and exercise number
#2.8
print("number\tsquare\tcube") #printing the headers
for i in range(5): #iterating through the numbers 0 - 5, performing calculations, and then printing them in a table 
    number = i
    square = i ** 2
    cube = i ** 3

    print(f"{number}\t{square}\t{cube}")


print("\n#3.4") #blank line and exercise number
#3.4
"""
fill in the missing code

for ***:
    for ***:
        print('@')
    print()
"""

for i in range(2): #to make 2 lines
    for j in range(7): #iterates 7 times, once for each @
        print("@", end="") #"end=""" makes it so the print doesn't start a new line each time
    print() #adds a blank line


print("\n#3.9") #blank line and exercise number
#3.9

number = 82347

for i in range(len(str(number))): #iterates the correct amount times for the number given
    slice = int(number // (10000 / (10 ** i))) #gets the number for the slice depending on how long the number is
    #print(10000 / (10 ** i)) #prints to help with debugging
    #print(number)  #prints to help with debugging
    number = number % (10000 / (10 ** i))  #makes a new number without the sliced off number
    print(slice) #printing :)