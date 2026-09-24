import math
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

number = int(input("input a number between 7 and 10 digits: "))

""" welp this didn't work :(
for i in range(len(str(number))): #iterates the correct amount times for the number given
    if i == 0:
        i = len(str(number)) - 7
    slice = int(number // (1000000 / (10 ** i))) #gets the number for the slice depending on how long the number is
    #print(10000 / (10 ** i)) #prints to help with debugging
    #print(number)  #prints to help with debugging
    number = number % (1000000 / (10 ** i))  #makes a new number without the sliced off number
    print(slice) #printing :)
"""

for i in range(len(str(number))): #iterates as many times as there are numbers in the string
    slice = int(number // (10 ** (len(str(number)) - 1)))   #gets the leftmost number slice
    number = number % (10 ** (len(str(number)) - 1)) #get the rest of the number without the slice
    print(slice)  #printing :)


print("\n#3.11") #blank line and exercise number
#3.11

going = True
total_gallons = 0   #making all dem variables
total_miles = 0
miles_per_gallon = 0
while going == True:
    gallons = int(input("Enter The Gallons Used (-1 to end): "))

    if gallons == -1:
        break

    miles = int(input("Enter Miles Driven: "))

    miles_per_gallon = miles / gallons

    print(f"The Miles/Gallon for this trip was: {miles_per_gallon}")

    total_gallons += gallons #adding to the totals
    total_miles += miles

    print() #extra line

total_miles_per_gallon = total_miles / total_gallons
print(f"The Total Miles/Gallon for everything was: {total_miles_per_gallon}")



print("\n#3.12") #blank line and exercise number
#3.12
#yes. all of the variables are scoobert variants (I gave up on unique names)
#scoobert gets sliced up and killed
#scoobert2 is the list of individual numbers
#scoobert3 is the initial number

scoobert = int(input("input a 5 digit integer: "))
scoobert3 = scoobert


#yoinked this code from 3.9
#i realize now that this isn't the easiest way to do it, but I already had the code for it so yk why not
scoobert2 = []
for i in range(len(str(scoobert))): #iterates as many times as there are numbers in the string
    slice = int(scoobert // (10 ** (len(str(scoobert)) - 1)))   #gets the leftmost number slice
    scoobert = scoobert % (10 ** (len(str(scoobert)) - 1)) #get the rest of the number without the slice
    scoobert2.append(slice)
    

if scoobert2[0] == scoobert2[4] and scoobert2[1] == scoobert2[3]:
    print(f"{scoobert3} is a palindrome")
else:
    print(f"{scoobert3} is not a palindrome")



print("\n#3.12") #blank line and exercise number
#3.12

#3.14 = 627
#3.141 = 2454
treadmill = True
i = 1
j = 0
pi = 0
place = []
place2 = []
while treadmill == True:

    if j % 2 == 1:
        pi -= (4 / i)
    else:
        pi += (4 / i)
    print(f"{j + 1}\t{pi}")
    if math.floor(pi * 100) / 100 == 3.14:
        place.append((j, pi))
        
    if math.floor(pi * 1000) / 1000 == 3.141:
        place2.append((j, pi))
    if i == 6001:
        treadmill = False
    i += 2
    j += 1

    #so these print statements are ROUGH, but I'm pretty sure this is what y'all want
print(place) #for 3.14
print(place2) # for 3.141