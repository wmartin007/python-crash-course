## Chapter 4 - Working with Lists
## Making Numerical Lists

## range() function
## range(x,y) will tell python to start at x and count to y (but no including y)
for value in range(1,5):
	print(value)
## This will print 1,2,3 and 4 on separate lines

## Using list() with range()
## You can wrap list() around range and python will create a list of that range
numbers = list(range(1,6))
print(numbers)

## range() can also take a third input to tell python to skip by that number

even_numbers = list(range(2,11,2))
print(even_numbers)

## You can creat almost any set of numbers you want by using the range() function.
## By using range() in a for loop, you can append values to a list
squares = []
for value in range(1,11): ## for loop to loop through integers 1-10
	square = value**2 ## assigning the square of the current int to the variable
	squares.append(square) ## appending current variable to the list
	## squares.append(value**2) is a more concise way to write this
print(squares)


## Simple Statistics with a List of Numbers
## A few python functions are specific to lists of numbers

digits = list(range(0,10))
print("\nDigits List:")
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

## List Comprehensions
## List comprehensions are an approach to generate list in one line of code.
## It combines the for loop and creation of new elements in one line, and
## automatically appends each new element.

squares = [value**2 for value in range(1,11)]
print(squares)


## Working with Part of a List
## Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) ## Will print the items at index 0, 1 and 2 (not 3)
print(players[1:4])
print(players[:4]) 
## If you omit the first index in a slice, Python will
## automatically start at the beginning of the list

print(players[2:]) ## The same syntax works if you want a slice to go to the end of the list

## Looping Through a Slice
##  You can use a slice in a for loop if you want to loop through a subset
##  of the elements in a list.

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

## Copying a List
## To copy a list, you can make a slice that includes the entire original
## by omitting the first and second index ([:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends's favorite foods are:")
print(friend_foods)

## NOTE: using friends_foods = my_foods won't work to create a copy
##		 of this list. It points the friends_foods list to the 
## 		 my_foods list


## Tuples
##  Python refers to values that cannot be changed as immutable, and an
##  immutable list is called a tuple. A tuple looks just like a list except 
##  you use parenthes instead of square brackets. Once you define a tuple,
##  you can access individual elements by using each items index just as
##  you would in a list

## Ex: We have a rectangle that should always be a certain size, we can
## ensure that it's size doesn't change by putting the dimensions in a 
## tuple.
print("\n"*5+"Dimensions")
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

## dimensions[0] = 250 will return a type error stating 'tuple' object
## does not support item assignment

## Looping Through All Values in a Tuple
for dimension in dimensions:
	print(dimension)

## Writing over a Tuple
## Though you can't modify a tuple, you can assign a new value to the
## variable that holds a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

