## Chapter 7 - User Input and While Loops

## How the input() Function Works
# The input() function pauses your program and waits for the user to 
# enter some text. Once Python recieves the user's input, it stores it
# in a variable to make it convenient for you to work with.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# You can store your prompt in a varable and pass that variable to the 
# input() function. This allows you to build your prompt over several
# lines, then write a clean input() statement

prompt = "If you tell us who you are, we can personalize the messages "
prompt += "you see. \nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

## Using int() to Accept Numerical Input
# When you use the input() function, Python interprets everything
# entered as a string. We can't calculate or compare this input to an
# integer. We resolve this issue by using the int() function, which 
# tells Python to treat the input as a numerical value.

age = input("How old are you? ")
age = int(age)


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride this ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

## The Modulo Operator
# The modulo operator (%) divides one number by another and returns the
# remainder. This is useful to determine if a number is even or odd.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")

## Accepting Input in Python 2.7
# You should use the raw_input() function in 2.7. This interprets all
# input as a string just as input() does in Python 3. input() in 2.7
# interprets the user's input as Python code and attempts to run the
# input. 

## Introducting while Loops
# The for loop takes a collection of items and execults a block of code
# once for each item in the collection. In contrast, the while loop runs
# as long as, or while, certain conditions are true.

# This example uses a while loop to count from 1 to 5:
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
# the += operator is shorthand for x = x + 1 (x += 1)

## Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
# The loop will repeat until the user types 'quit'. However, the terminal
# will still print quit before it leaves the loop. We can fix that by 
# including an if statement in the loop

message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

## Using a Flag
# 	In the previous example, we had the program perform certain tasks
# while a given condition was true. But what about more complicated
# programs in which many different events could cause a program to stop
# running? 
# 	For example, in a game, several different events can end the game. 
# When a player runs out of ships, their time runs out, or the cities
# they were supposed to protect are all destroyed, the game should end.
# It needs to end if any one of these events happens. If many possible
# events occur to stop the program, trying to test all these conditions
# in one while statement becomes complicated and difficult.
#	For a program that should run only as long as many conditions are
# true, you can define one variable that determines whether or not the
# entire program is active. This variable, called a flag, acts as a 
# signal to the program. We can write our programs so they run while the
# flag is set to True and stop running when any of several events sets
# the value of the flag to False. As a result, our overall while 
# statement needs to check only one condition: whether or not the flag
# is currently set to True. Then, all our other tests (to see if an
# event has occurred that should set the flag to False) can be neatly
# organized in the rest of the program.

active = True # This is the flag
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)

## Using break to Exit a Loop
# 	To exit a while loop immediately without running any remaining code
# in the loop, regardless of the results of any conditional test, use
# the break statement. This break statement directs the flow of your
# program; you can use it to control which lines of code are executed 
# and which aren't, so the program only executes code that you want it 
# to, when you want it to.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

## Using continue in a Loop
#	Rather than breaking out of a loop entirely without executing the
# rest of its code, you can use the continue statement to return to the
# beginning of the loop based on the result of a conditional test.
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
		# The above tells python if the modulo is 0, return to the start
		# of the loop. If the modulo isn't 0, the rest of the loop is 
		# executed and Python prints the current number
	print(current_number)

## Avoiding Infinite Loops
#	Every while loop needs a way to stop running so it won't continue to
# run forever. The following loop will run forever:
# x = 1
# while x <= 5:
#	print(x)
# It has no way to increment x so x will always be one and the condition
# will always be true. It will print 1 forever. If you do accidentally 
# write an infite while loop, press ctrl-c or close the terminal window
# displaying your program's output.

## Using a while Loop with Lists and Dictionaries
#	So far, we've worked with only one piece of user information at a
# time. We received the user's input and then printed the input or a
# response to it. The next time through the while loop, we'd receive 
# another input value and respond to that. But to keep track of many
# users and pieces of information, we'll need to use lists and
# dictionaries with our while loops.
#	A for loop is effective for looping through a list, but you should
# not modify a list inside a for loop because Python will have trouble
# keeping track of the items in the list. To modify a list as you work
# through it, use a while loop. Using while loops with lists and 
# dictionaries allows you to collect, store, and organize lots of input
# to examine and report on later.

## Moving Items from One List to Another
#	Consider a list of newly registered but unverified users of a 
# website. After we verify the users, how can we move them to a separate
# list of confirmed users? One way would be t use a while loop to pull
# users from the list of unconfirmed users as we verify them and then
# add them to a separate listof confirmed users.

# Start with users that need to be verified, and an empty list to hold
#  confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

## Removing All Instances of Specific Values from a List
#	In Chapter 3 we used remove() to remove a specific value from a list.
# This only worked on the first instance of a value from the list.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)
