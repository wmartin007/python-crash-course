## 6.1
#Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person = {
	'first_name': 'Allie',
	'last_name': 'Martin',
	'age': 26,
	'city': 'Talmo'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print(person)

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
		'code based on which (if any) of these criteria are met.'
}
print('concatenate :')
print(glossary['concatenate'] + '\n')
print('for loops :')
print(glossary['for loops'])

