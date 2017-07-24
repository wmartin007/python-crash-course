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
	print("\nName: " + name)
	print("Language: " + language)
