## 7.1 Rental Car
#Write a program that asks the user what kind of rental car they
#would like. Print a message about that car, such as “Let me see if I can find you
#a Subaru.”

rental_car = input("What kind of car would you like to rent? ")
print("Let me see if I can find you a " + rental_car)


## 7.2 Restaurant Seating
#Write a program that asks the user how many people
#are in their dinner group. If the answer is more than eight, print a message saying
#they’ll have to wait for a table. Otherwise, report that their table is ready.

party_size = input("How many people are in your dinner party? ")
party_size = int(party_size)
if party_size > 8:
	print("Sorry, your party is large and there will be a wait for the "+
		"table.")
else:
	print("Your table is ready. Please follow me")

## 7.3 Multiples of Ten
# Ask the user for a number, and then report whether the number is a
# multiple of 10 or not.

number = input("Please enter a number: ")
number = int(number)
if number % 10 == 0:
	print("Your number is a multiple of 10!")
else:
	print("Your number is not a multiple of 10 :(")

## 7.4 Pizza Toppings:
# 	Write a loop that prompts the user to enter a series of pizza
# toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you'll add that topping to their pizza.
prompt =("\nPlease enter a topping for your pizza: ")
prompt += ("\n(Enter 'quit' when you're finished entering toppings) ")

while True:
	topping = input(prompt)
	
	if topping == 'quit':
		break
	else:
		print("I'll add " + topping + " to your pizza.")

## 7.5 Movie Tickets
#	A movie theater charges different ticket prices depending on
#a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#$15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket.

while True:
	age = input("Please enter your age to see the price of a ticket: ")
	age = int(age)
	if age < 3:
		print('Price: Free')
	elif age <= 12:
		print('Price: $10')
	else:
		print("Price: $15")
	break
