## Chapter 6 - Dictionaries
## Python dictionaries allow you to connect pieces of related informtaion

## A Simple Dictionary
## This simple dictionary stores information about a particular alien:

alien_0 = {'color': 'green', 'points': 5}

## The dictionary stores the alien's color and point value

print(alien_0['color'])
print(alien_0['points'])

## A dictionary in Python is a collection of key-value pairs. Each key 
## is connected to a value, and you can use a key to access the value
## associated with that key. A key's value can be a number, a string,
## a list, or even another dictionary. You can use any object that you
## create in Python as a value in a dictionary.

## Accessing Values in a Dictionary
## To get a value associated with a key, give the name of the dictionary
## and then place the key inside a set of square brackets.

print(alien_0['color']) ## alien_0 is the dictionary, 'color' is the key

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

## Adding New Key-Value Pairs
## You can add new key-value pairs to a dictionary at any time. Let's
## add the alien's x- and y-coordinates. 
print(alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

## Starting with an Empty Dictionary
## Sometimes it's more convenient to start with an empty dictionary and
## add to it. To start filling an empty dictionary, define a dictionary
## with an empty set of braces and then add each key-value pari on it's
## own line. 

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
## Typically you'll use empty dictionaries when storing user supplied
## data in a dictionary or when you write code that generates a large
## number of key-value pairs automatically. 

## Modifying Values in a Dictionary
## To modify a value in a dictionary, give the name of the dictionary
## with the key in square brackets and then the new value you want
## associated with that key. For example, consider an alien that changes
## from green to yellow as the game progresses:
print("The alient is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

## For a more interesting example, let’s track the position of an alien that
## can move at different speeds. We’ll store a value representing the alien’s
## current speed and then use it to determine how far to the right the alien
## should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

## Move the alien to the right.
## Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

## Removing Key-Value Pairs
## When you no longer need a piece of information that's stored in a
## dictionary, you can use the del statement to completely remove a
## key-value pair. 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

## A Dictionary of Similar Objects
## The previous example involved storing different kinds of information
## about one object, an alien in a game. YOu can also use a dictionary
## to store one kind of information about many objects.
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
## When you know you'll need more than one line to define a dictionary,
## press enter after the opening brace. Then follow the format we used 
## above (indent, key-value pair, comma, new line). Then put the closing
## brace on a new line after the last key-value pair. 

print("Sara's favorite language is " + 
	favorite_languages['sarah'].title() +
	".")
## This example also shows how you can break up a long print statement
## over several lines. 

## Looping Through a Dictionary
##	Looping Through All Key-Value Pairs
##	Lets consider a new dictionary designed to store information about a
##	user on a website. The following dictionary would store one person's
##	username, first name, and last name.

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}
# We already know how to access any single piece of information about
# user_0 based on what we've learned so far in this chapter. If we want
# to see everything stored in this user's dictionary we can use a for loop.

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

# To write a for loop for a dictionary, you create names for the two
# variables that will hold the key and value in each key-value pair. The
# variables can be named whatever you wish. for k, v in user_0.items()
# would also work. The .items() method returns a list of key-value pairs.
# You'll notice the key-value pairs are not printed in the order that
# they're stored. 

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title()+
	".")

## Looping Through All the Keys in a Dictionary
## The keys() method is usefull when you don't need to work with all
## values in a dictionary.

for name in favorite_languages.keys():
	print(name.title())

## Looping through keys is actually the default behaviror when looping
## through a dictionary, so the code would have exactly the same output
## if you wrote: for name in favorite_languages and left out the .keys()


## Let's print a message to some friends about the languages they chose

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language "+
		"is " + favorite_languages[name].title() + "!")

## You can use the keys() method to find out if a particular person was
## polled. This time, let's find out if Erin took the poll:

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

## Looping Through a Dictionary's Keys in Order
## You can use the sorted() function to get a copy of the keys in order

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

## Looping Through All Values in a Dictionary
## The values() method will return a list of values without any keys.

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
## This will return a list without checking for duplicates. To avoid
## the repetition, we can use a set. A set is similar to a list except
## that each item in a set must be unique.

for language in set(favorite_languages.values()):
	print(language.title())

## Nesting
## Nesting is when you store a set of dictionaries in a list or a list
## of items as a value in a dictionary. You can nest a set of 
## dictionaries inside a list, a list of items in a dictionary, or even
## a dictionary inside another dictionary.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

# A more realistic example would involve more than three aliens with 
# code that automatically generates each alien. We'll use range to 
# generate a fleet of 30 aliens.

# Make an empty list for storing aliens
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# Let's assume the game progresses and now we want the first 3 aliens
# to change to yellow.

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
# Show first 5 aliens
for alien in aliens[0:5]:
	print(alien)
print("...")

# It's common to store a number of dictionaries in a list when each 
# dictionary contains many kinds of information about one object, as we 
# did when we created a dictionary for each user on a website. All of
# the dictionaries in a list should have an identical stucture so you 
# can loop through the list and work with each dictionary object in the
# same way.

## A List in a Dictionary

# Rather than putting a dictionary inside a list, it's sometimes useful
# to put a list inside a dictionary. For example, consider describing a
# pizza someone might be ordering. In a list you can only really store 
# the toppings, but in a dictionary that can be just one aspect of the
# pizza you're describing.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza with the "
	+ "following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

# You can nest a list inside a dictionary any time you want more than
# one value to be associated with a single key in the dictionary. Suppose
# we allowed more than one favorite language to be chosen in our previous
# example of favorite programming languages.
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edwards': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

# You can refine this program futher by including an if statement at the
# beginning of the dictionary's for loop to see whether each person has
# more than one favorite language by checking the value of len(languages).

# NOTE: You should not nest lists and dictionaries too deeply. If you're
# nesting items much deeper than the preceding examples, most likely a
# simpler way to solve the problem exists.

## A Dictionary in a Dictionary

# You can nest a dictionary inside another dictionary, but your code
# can get complicated quickly. 

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
