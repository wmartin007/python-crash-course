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
