## 6.1
#Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person_0 = {
	'first_name': 'Allie',
	'last_name': 'Martin',
	'age': 26,
	'city': 'Talmo'
}
print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])
print(person_0)

## 6.2
#Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.

fav_numbers = {
	'luke': 4,
	'william': 13,
	'allie': 11,
	'sookie': 100,
	'elsa':1,
}

print("Luke's favorite number is " + str(fav_numbers['luke']))
print("William's favorite number is " + str(fav_numbers['william']))

## 6.3
#A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
	#Print each word and its meaning as neatly formatted output. You might
	#print the word followed by a colon and then its meaning, or print the word
	#on one line and then print its meaning indented on a second line. Use the
	#newline character (\n) to insert a blank line between each word-meaning
	#pair in your output.

glossary = {
	'concatenate': 'to join two strings or other applicable object ' +
		'types together.',
	'for loops': 'for loops are used to perform some action on each ' +
		'item in a list.',
	'lists': 'lists are used to store multiple objects together',
	'if-elif-else': 'if-elif-else statements can be used to evaluate ' +
		'if an element meets certain criteria and executes blocks of ' +
		'code based on which (if any) of these criteria are met.',
}
print('concatenate :')
print(glossary['concatenate'] + '\n')
print('for loops :')
print(glossary['for loops'])

## 6.4
#Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.

for word, definition in glossary.items():
	print(word + " :\n" + definition + '\n')

## 6.5
#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#• Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#• Use a loop to print the name of each river included in the dictionary.
#• Use a loop to print the name of each country included in the dictionary.

rivers = {
	'mississippi': 'the united states',
	'nile': 'egypt',
	'amazon': 'brazil',
}

for river, country in rivers.items():
	print("The " + river.title() + " river runs through " + country.title() + ".")
print('\n')
for river in rivers.keys():
	print(river)
print('\n')
for country in rivers.values():
	print(country)
	
## 6.6 Polling. Use the code in favorite_languages.py (page 104)
#• Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

poll_list = ['edward', 'allie', 'william', 'sarah', 'luke']

for name in poll_list:
	if name in favorite_languages.keys():
		print(name.title() + ", thank you for taking the favorite languages poll.")
	else:
		print(name.title() + ", please go take the poll.")

## 6.7 People
#Start with the program you wrote for Exercise 6-1 (page 102).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

person_1 = {
	'first_name': 'William',
	'last_name': 'Martin',
	'age': 29,
	'city': 'Talmo'
}

person_2 = {
	'first_name': 'Taylor',
	'last_name': 'Martin',
	'age': 27,
	'city': 'Jefferson'
}

persons = [person_0, person_1, person_2]

for person in persons:
	print(person)

## 6.8 Pets
#Make several dictionaries, where the name of each dictionary is the
#name of a pet. In each dictionary, include the kind of animal and the owner’s
#name. Store these dictionaries in a list called pets. Next, loop through your list
#and as you do print everything you know about each pet.

sookie = {
	'species': 'cat',
	'color': 'calico',
	'owner': 'allie',
}
elsa = {
	'species': 'cat',
	'color': 'black',
	'owner': 'william',
}
ernie = {
	'species': 'dog',
	'color': 'tan',
	'owner': 'joe',
}

pets = [sookie, elsa, ernie]

for pet in pets:
	print(pet)

## 6.9 Favorite Places
#Make a dictionary called favorite_places. Think of three
#names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.

favorite_places = {
	'william': ['lake tahoe', 'maldives', 'talmo'],
	'allie': ['talmo', 'mexico', 'bahamas'],
	'luke': ['home', 'nanas', 'grams'],
}

for name, places in favorite_places.items():
	print(name.title() + ", your favorite places are:")
	for place in places:
		print("\t" + place.title())

## 6.10 Favorite Numbers
#Modify your program from Exercise 6-2 (page 102) so
#each person can have more than one favorite number. Then print each person’s
#name along with their favorite numbers.
fav_numbers = {
	'luke': [2,4],
	'william': [13,87],
	'allie': [11,91],
	'sookie': [0,100],
	'elsa': [1,11],
}

for name, numbers in fav_numbers.items():
	print(name.title() + ", your favorite numbers are: ")
	for num in numbers:
		print("\t" + str(num))

##6.11 Cities
#Make a dictionary called cities. Use the names of three cities as
#keys in your dictionary. Create a dictionary of information about each city and
#include the country that the city is in, its approximate population, and one fact
#about that city. The keys for each city’s dictionary should be something like
#country, population, and fact. Print the name of each city and all of the information
#you have stored about it.

cities = {
	'atlanta': {
		'state': 'georgia',
		'population': 5500000,
		'fact': 'known as hotlanta',
		},
	'new york': {
		'state': 'new york',
		'population': 8500000,
		'fact': 'big apple',
		},
	'los angeles': {
	'state': 'california',
	'population': 4000000,
	'fact': 'city of angels',
	},
}

for city, info in cities.items():
	print(city + ":")
	for k, v in info.items():
		print("\t" + k + ":" + str(v))

## 6.12 Extensions

