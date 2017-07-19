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

print("I really love pizza!")

##

