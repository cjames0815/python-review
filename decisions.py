#Expressions in python evaluate to true or false.
#Expressions use the comparision operators: <,
#>, <=, >=, ==, !=

x = 4

print(x < 5)
print(x > 5)
print(x == 5)
print(x != 5)

#Python supports the if, if-else, if-elif-else, and 
#nested if decisions structures

#The if decision structure test its condition
#and if the condition is true, it executes the code 
#block its given

#Here is the short hand version of the if decision
#The shorthand version may be used when there is only 
#one statement to be executed
if (x > 5): print('x is less than 5 is true.')

#The if-else decision structure test its condition
#and if the condition is true, it executes the code block
# it's given. If the condition is false, the code block
#given to the else is executed
if(x == 5):
    print('x is equal to 5 is true.')

else:
    print('x is equal to 5 is false.')

#Here is the shorthand version of the if-else decision.
print('x is equal to 5 is true.') if(x == 5) else print('x is equal to 5 is false.')

#The if-elif-else decision structure tests multiple 
#conditions. The code block given to the condition that's true,
#is executed if none of the condtions are true
#The code block given to the else is executed
if(x > 5):
    print('x is equal to true')
elif (x ==5):
    print('x is equal to 5 is true')
elif(x < 5):
    print('x is less than 5 is true')
else:
    print('None of the condtions are true.')

if(x > 5):
    print('x is equal to true')
elif (x ==5):
    print('x is equal to 5 is true')
elif(x < 5):
    print('x is less than 5 is true')
else:
    print('None of the condtions are true.')

if(x > 5):
    print('x is equal to true')
elif (x ==5):
    print('x is equal to 5 is true')
elif(x < 5):
    
    #This code block won't be executed even
    #though its condition is true because only 
    #the first true code block will be executed
    print('x is less than 5 is true')
else:
    print('None of the condtions are true.')

#A nested if decision is an if statement that id a target 
# of another if statement
if (x < 5):
    print('x is less than 5 is true.')
    if(x != 5):
        print('x is not equal to 5 is true.')

#Comparision operators may be chained together.
a = 5 
b = 10
c = 15

if a < b < c:
    print('b is greater than a and less than c')

#Python supports the match-case decision struction This
#decision structure is useful when many conditions need to be tested.
#It require Python 3.10 or never.
grade = 'A'

match grade:
    case 'A':
        print('Super Work!')
    case'B':
        print('Good Job!')
    case'C':
        print('You made it.')
    case'D','F':
        print('Oh, dear...')
    case _:
        print('Invalid grade.')

#Python supports the ternary operator.
result = 'x is equal to 5 is true.' if (x == 5) else'x is equal to 5 is false'
print(result)
print(('x is equal to 5 is true.' if (x == 5) else'x is equal to 5 is false'))

# The ternary oprator may be written using tuples.
#(false value, true value) [expression to test]
#x = 5
result = ('x is equal to 5 is false.', 'x is equal to 5 is true.')[x == 5]
print(result)

# The ternary operator may be written using dictionaries.
result = {True:'x is equal to 5 is false.', False: 'x is equal to 5 is true.'}[x == 5]

#Expressions in python may also use the logical operators:
#and, or , not
num = 150

# This if-else decision structure tets if num is between 1 and 100
if(num >= 1 and num <= 100):
    print('num is between 1 and 100.')
else:
    print('num is not between 1 and 100.')

# This if-else decision structure tets if num is not between 1 and 100
if(num < 1 or num > 100):
    print('num is not between 1 and 100.')
else:
    print('num is  between 1 and 100.')

foundIt = False

# This if-else decision structure tests if foundIt is False.
if(not foundIt):
    print('foundit is False.')
else:
    print('foundIt is True.')