#Python supports the for and while loops.
#Loops are used to repeat a block of code.

#The for loop is used for sequential traversal
#It may be used fir iterating through strings, tuples, 
#List, or dictionaries.

#String 
iterable= (9,8,7,6,5,4,3,2,1)
for i in iterable:
    print(i, end=" ")
print("blastoff!")

#List
iterable= [9,8,7,6,5,4,3,2,1]
for i in iterable:
    print(i, end=" ")
print("blastoff!")

#Dictionary
iterable = dict({'nine': 9,
                'eight': 8,
                'seven':7,
                'six': 6,
                'five': 5,
                'four': 4,
                'three': 3,
                'two': 2,
                'one': 1
                })
for i in iterable:
    print("%d" %(iterable[i]), end=" ")
print("blastoff!")

#The while loop must be provided a condition.
#As long as the condition is true, its code
#block will be executed

i = 9
while (i > 0):
    print(i, sep=" ", end=" ")
    # The must be a line of code in the code block 
    #The forces the condition to become false, else
    #the loop will repeat infinitely
    i = i - 1
print("blastoff!")

i= 8
while (i > 0):
    print(i, sep=" ", end=" ")
    # The must be a line of code in the code block 
    #The forces the condition to become false, else
    #the loop will repeat infinitely
    i = i - 2
print("blastoff!")

i = 9
while (i > 0):
    print(i, sep=" ", end=" ")
    # The must be a line of code in the code block 
    #The forces the condition to become false, else
    #the loop will repeat infinitely
    i = i - 1
print("blastoff!")

i = 9
while (i > 0):
    if (i % 2 == 0):
        print(i, sep=" ", end=" ")
    # The must be a line of code in the code block 
    #The forces the condition to become false, else
    #the loop will repeat infinitely
    i = i - 1
print("blastoff!")


#Odd number 1 -10
i = 9
while i > 0:
    if i % 2 != 0:  # Check if i is odd
        print(i, end=" ")
    i = i - 1

print("blastoff!")
