## A Simple Example

## In your list of cars, most brands should be printed in title case.
## However, bmw should be printed in upper case. A for loop with an if
## statement will handle this scenario
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

## Ignoring Case When Checking for Equality
## Testing for equality is case sensitive in Python. Ex: Audi != audi
## If you want to test the value of a variable regardless of case, you
## can convert the value to lowercase before the operation

car = 'Audi'
car.lower() == 'audi' 
## this will return true and doesn't affect the original value

## Checking Inequality
## When determining whether two values are not equal, use !=

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")
	
## Checking Whether a Value Is in a LIst

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

## You can use not in to check if a value doesn't appear in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

## Boolean Expressions
## Boolean values are often used to keep track of certain conditions

game_active = True
can_edit = False

## Simple if Statements
## if conditional_test:
##     do something

age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

## if-else statements
## Similar to a simple if statement, if-else takes it one step further
## by giving Python a set of code to execute when the if statement 
## returns false.
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

## The if-elif-else Chain
## Often, you'll need to test more than two possible situations. To
## evaulate these you can use Python's if-elif-else syntax. It runs each
## conditional test in order and executes the code following the first
## test that the condition passes

age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

## Rather than printing the price within the if-elif-else block, you can
## make the code more concise by just setting the price inside the chain
## and running a print statement after the chain

age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")
## An else block is not required. In the above example it is possible
## to have ended with elif age >= 18: instead of else

## Testing Multiple Conditions
##  The if-elif-else chain is powerful, but it's only appropriate to use
##  when you just need one test to pass. As soon as Python finds one 
##  test that passes, it skips the rest of the tests.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
## This code would not work properly using an if-elif-else block. It would
## evaluate the first statement as true and just add mushrooms before
## finishing the pizza.
