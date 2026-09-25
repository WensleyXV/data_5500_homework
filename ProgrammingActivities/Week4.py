import random
"""
Programming Activity 1

Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""

sum = 0.0
for i in range(1, 1000):
    
    sum = sum + (1/(2**i))

print(sum)
# The result is 1 (well technically really really close to one, but the program returns 1)

print()
"""
Programming Activity 2

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""


colors = ["pink", "black", "purple"]
for i in colors:
    print(i)


print()
"""
Programming Activity 3

Update the loop in activity 2 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""
colors = ["pink", "black", "purple"]
for i in colors:
    for j in range(len(i)):
        print(i[j])
    print()


print()
"""
Programming Activity 4

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""

scoobert = []
for i in range(10):
    scoobert.append(random.randint(0, 1000))
   

print(scoobert) #doesn't say to print it, but I'm gonna anyway


print()
"""
Programming Activity 5

Using the list you generated in programming activity 4, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""
for i in range(len(scoobert)): 
    if i == 0: #this if statement is here so I don't get value errors for trying to do scoobert[-1] :)
        pass
    else:
        if scoobert[i] % 2 == 0 and scoobert[i - 1] % 2 == 0:
            print(scoobert[i - 1], scoobert[i])


print()
"""
Programming Activity 6

Write a Python program that creates a list of all even numbers from 2 to 100 using list comprehension.
"""
#I think this is what y'all mean by list comprehension, but I could be totally wrong
num_list = []
for i in range(1, 100):
    if i % 2 == 0:
        num_list.append(i)

print()
"""
Programming Activity 7

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. Use list comprehension to remove these spaces from each string in the list.
"""

beach = ["  hello", "mybadg ", "trains  ", " yourmom", "weird", "nice", " purple", "circle ", "sweet"]

no_space = []
slice = 0
rslice = 0

end = False
for space in beach:
    slice = 0
    rslice = 0
    end = False
    for k in range(len(space)):
        
        if space[k] != " ":
            
            end = True
            
            continue
        if space[k] == " " and end == False:
            #if end == True:
                #continue
            slice += 1
        elif space[k] == " ":
            rslice += 1
            continue
    if slice > 0:
        no_space.append(space[slice:])
    elif rslice > 0:
        no_space.append(space[:-rslice])
    else:
        no_space.append(space)

print(no_space)

#there was most definitely an easier way to do that, but it works.
#bro since when is string.slice a thing holy cow

print()
"""
Programming Activity 8

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements 
and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

age = int(input("age: "))
weight = int(input("weight: "))
front = False

if age >= 12:
    front = True
elif age == 11 and weight >= 90:
    front = True
elif age <= 11 and weight >= 100:
    front = True
else:
    front = False

if front:
    print("The child can sit in the front seat.")
else:
    print("The child cannot sit in the front seat.")