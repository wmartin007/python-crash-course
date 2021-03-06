## Chapter 8 - Functions ##
# Functions are named blocks of code designed to perform a particular task.
# You call the name of the function when you want it to do this task.
# You'll want to store functions in seperate files called modules to help
# organize your main program files.

# Defining a Function #
#Here's a simple functions named greet_user() that prints a greeting.

def greet_user():
    """Display a cimple greeting"""
    print("Hello")

greet_user()

# Passing Information to a Function #
#By modifying the previous example, we can tell the function to greet a user by
#name.

def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('william')
#The function now takes a value and passes it to the print statement inside. The
#username in the above example is called a parameter. The name william is an
#argument. Sometimes these terms are used interchangably.

# Passing Arguments #
#Because a function definition can have multiple parameters, a function call
#may need multiple arguments. You can pass arguments to your functions in a
#number of ways. You can use positional arguments, which need to be in the
#same order the parameters were written; keyword arguments, where each argument
#consists of a variable name and a value; and lists and dictionaries of values.

# Positional Arguments
#When you call a function, Python must match each argument in the function call
#with a parameter in the function definition. The simplest way to do this is
#based on the order of the arguments provided. Values matched up this way are
#called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
#You can call a function as many times as needed.
describe_pet('dog','willie')

#Order does matter in the example above. However, you can use keyword arguments
#to ignore the order of your arguments.

describe_pet(animal_type='cat',pet_name='sookie')
describe_pet(pet_name='elsa',animal_type='cat')

# Default Values
#When writing a function, you can define a default value for each parameter. If
#an argument is provided for a parameter in the function call, Python uses the
#argument value. If not, it uses the parameter's default value.

def describe_pet(pet_name, animal_type='dog'):
    """Display info about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('ernie') #pet_name = 'ernie' also works


# Equivalent Function Calls
#Because positional arguments, keyword arguments, and default values can all be
#used together, often you'll have several equivalent ways to call a function.
#Consdier the following def for describe_pets() with one default value
#provided: def describe_pet(pet_name, animal_type = 'dog'). With this definition
#an argument always needs to be provide for pet name, and this value can be
#provided using the positional or keyword format.

# Avoiding Argument Errors
#You'll undoubtedly encounter errors about unmatched arguments. For example,
#if we try to call describe_pets() without any arguments, Python will give us
#an error saying information is missing from the function call.

# Return Values
#A function doesn't always have to display its output directly. Instead, it can
#process some data and then return a value or set of values. The value a
#function returns is called a return value. The return statement takes a value
#from inside a fucntion and sends it back to the line that called the function.
#Return values allow you to move much of your program's grunt work into
#functions, which can simplify the body of your program.

# Returning a Simple Value

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

print('\n')
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#When you call a function that returns a value, you need to provide a variable
# where the return value can be stored.

# Making an Argument Optional
#Sometimes it makes sense to make an argument optional so that people using
#the function can choose to provide extra information only if they want to.
#Here's an attempt at including a middle name in our previous function:

def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#However, middle names aren't always needed, and this function wouldn't work
#as is without all three arguments. To make middle name optional, we can give
#the middle name argument an empty default value and ignore the argument unless
#the user provides a value. We also need to move it to the end of the list of
#parameters.

def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print('\n')
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)

# Returning a Dictionary
#A function can return any kind of value you need it to, including more
#complicated data structures like lists and dictionaries.

def build_person(first_name, last_name):
    """Return a dictionary o information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

#We can extend this function to accept optional values like middle name, age,
#occpuation, or any other information you want to store about a person. Ex:

def build_person(first_name, last_name, age = ''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

##Using a Function with a while Loop
#You can use functions with all the Python structures we've learned about so
#far. For example, let's use the get_formatted_name() function with a while
#loop to greet users more formally.

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

##Passing a List
#You'll often find it useful to pass a list to a functions. Let's use functions
#to make working with lists more efficient.

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

##Modifying a List in a Function
#When you pass a list to a function, the function can modify the list.

#Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design until none are left.
#Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#Display all completed models
print("\nThe following models have been printed:")
for model in completed_models:
    print(model)

#We can improve this code by writing two functions, where each does a specific
#job. The first function will handle printing the designs, and the second will
# sumamrize the prints that have been made.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simulate creating a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)

#The output is the same as the version without functions, but the code is more
#organized. It will also be easier to expand and maintain than the version w/o
#functions.

## Preventing a Function from Modifying a List
#Sometimes you'll want to prevent a function from modifying a list. You can send
#a copy of the list instead of the list itself to the function like this:
# function_name(list_name[:]) - the slice notation makes a copy of the list
#to send to the function.


## Passing an Arbitrary Number of Arguments
#Sometimes you won't know ahead of time how many arguments a fucntion needs to
#accept. Pythons allows a function to collect an arbitrary number of arguments
#from the calling statement.

#Lets consider a function that builds a pizza. It needs to accept a number
#of toppings, but you can't know ahead of time how many toppings a person will
#want. The function in the following has one parameter, *toppings, but it will
#collect as many arguments as the calling line provides.

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Now we can replace the print statement with a loop that runs through the list
#of toppings and describes the pizza being ordered.

def make_pizza(*toppings):
    """Summarzie the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)


