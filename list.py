#The list is one of Python's main ordered collections.

#This line of code creates an empty list.
nums = []
print(nums)

#This line of code creates a list of 5 integers 
nums = [1,2,3,4,5]
print(nums)

#These lines of code are accessing an element value in 
#the list by using its index
print(nums[1])
nums[4] = 6
print(nums)

# if an attempt is made to access an element outside of the 
#bounds of the list and IndexError will be thrown
#print(nums[5])
#nums[-6] = 0
#We may use negative indices in the square brackets.
#In the case if this list, -5, -4, -3, -2, -1 are the
#only valid indices, with -1 being the index for the last 
#element and -5 being the index for the first element
print(nums[-1])
print(nums[-5])

# The Python len function tells us the number of elements in a list
print(len(nums))

#This line of code is creating a list of value of mixed types
mixed = [1,'one', 2, 'two', 3, 'three']
print(mixed)

#While loop
i = 0
while (i < len(nums)):
    print(nums[i], end=" ")
    i = i + 1
print()


#Numbers less than 6
i = 0
while (i < len(nums)):
    print(nums[i] < 6, end=" ")
    i = i + 1
print()


#Python has inbuilt functions that may be used to manipulate lists.

#The append functions may be used to add one element at a time to a list
names = []
print(names)

#These lines of code will use the append function to add elements one at a time
#to the list
names.append('Sammy')
names.append('Mia')
names.append('Dean')
names.append('Copper')
print(names, '- original list')

#These lines of code ass multiple elements to the list using a loop
for i in range (1,5):
    names.append(i)
print(names, '- add multiple elements using a loop')

#This line of code adds a Tuple to a list
names.append(('Chessie', 'Lexi'))
print(names, '- add tuple')

#This line of code adds a list to a list
names.append([1,2])
print(names, ' - add list')

#The insert function may be used to add elements at a desired position in a list.
names.insert(0, 'Pixie')
names.insert(5,0)
print(names, '-insert function')

#The extend function maybe used to add multiple elements to the end of a list
names.extend(['Lea', ' Fritz', 'Lea'])
print(names, '- extend function')

#The reverse function may be used to reverse the elements in a list
names.reverse()
print(names, ' - reverse function')

#The remove function may be used to remove a desired value from a list
names.remove(('Chessie', 'Lexi'))
print(names, ' - remove function')

#An error will be generated if the value doesn't exist in the list
#names.remove([1,2,3])

#Only the first occurence of the value will be removed from the list
names.remove('Lea')
print(names,'-removes functions first value only')

#The remove function only removes one element at a time 
#To remove a range of elements, a loop must be used 
names.reverse()
print(names)
for i in range(0,5):
    names.remove(i)
print(names, ' - removes function range')

#The pop function cam also be used to remove and return an element from a list
#By default, it removes omnly the last elements of the list
last = names.pop()
print(last)
print(names, '- pop function')

#To remove an element from a specific postion of a list, the index of the element
#mayb be passed as an argument to the pop function
first = names.pop(0)
print(first)
print(names, '- pop function with index')
