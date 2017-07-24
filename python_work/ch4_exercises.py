## Chapter 4 - Working with lists


## FOR loops
## Python's for loops work when you want to do the same action
## with every item in a list.

magicians = ['alice', 'david', 'carolina'] ##  Defines list
for magician in magicians:
	## This tells python to pull a name from the list magicians and
	## store it in the variable magician
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	## This is the action taken for the current variable and will be
	## repeated for every item in the list
## The variable created in the for loop is temporary.

print("Thank you everyone. That was a great magic show!")



## 4.1 Pizzas

## Store 3 different kinds of pizza in a list
pizzas = ['italian sausage', 'pepperoni', 'mushroom']

## Make a for loop to print that you like that kind of pizza for each 
for pizza in pizzas:
	print("I like " + pizza + " pizza.")

## After the loop, add a sentence to print
print("I really love pizza!")

print("\n\n")
## 4.2 Animals
## Make a list of animals that have something in common
animals = ['gorilla', 'zebra', 'giraffe']

## Use a for loop to print a statement about each animal
for animal in animals:
	print('You can find a ' + animal + " in the zoo!")
## Add a line to the end of the program that states what each of these
## animals have in common.
print('All of these animals belong in the zoo.')

print('\n\n')

## 4.3 Counting to twenty
## Use a for loop to print the numbers from 1 to 20 inclusive

for value in range(1,21):
	print(value)

## 4.4 One Million
## Make a list of the numbers from one to one millions and use a for loop to print the numbers

one_million = list(range(1,1000001))
##print(one_million) ## commented out to save time

## 4.5 Summing a million
## Show min, max, and sum of our previous list
print(min(one_million))
print(max(one_million))
print(sum(one_million))

## 4.6 Odd Numbers
## Use the 3rd argument of range() to make a list of odd numbers from 1 to 20.
## Use a for loop to print each number.
odds = list(range(1,21,2))
for value in odds:
	print(value)

## 4.7 Threes
## Make a list of the multiples of 3 from 3 to 30. Use a for loop to print each

threes = list(range(3,31,3))
for value in threes:
	print(value)

## 4.8 Cubes
## Make a list of first 10 cubes and use a for loop to print each
cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
	print(cube)

## 4.9 Cube Comprehension
## Use list comprehension to generate a list of the first 10 cubes

cubes_list = [value**3 for value in range(1,11)]
print(cubes_list)

## 4.10 Slices
## Using one of the programs you wrote in this chapter, add 
## several lines to the end of the program that do the following:

## Print the first three items in the list
print(cubes[:3])

## Print three items from the middle of the list
print(cubes[2:5])

## Print the last three items in the list
print(cubes[-3:])

## 4.11
## Start with the program from 4.1. Make a copy of the list of pizzas 
## and call it friend_pizzas, then do the following:
## add a new pizza to the original list
## add a different pizza to the friend_pizzas list
friend_pizzas = pizzas[:]
pizzas.append('supreme')
friend_pizzas.append('hawaiian')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

## 4.12
## More Loops

## 4.13 Buffet
## Store 5 simple basic foods that a buffet might offer in a tuple
buffet = ('fried chicken', 'mashed potatoes', 'corn', 'hamburgers', 'french fries')
print("\n\nThe buffet consists of:")
for food in buffet:
	print(food)

## Restaurant changes it's menu. Replace 2 of the items with different foods

buffet = ('baked chicken', 'french fries', 'corn', 'hamburgers', 'french fries')
print("\nThe new buffet menu is:")
for food in buffet:
	print(food)
