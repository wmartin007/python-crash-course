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
