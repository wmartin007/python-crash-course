## 5.1 Conditional Tests
car = 'ford'
print("Is car == 'ford'. I predict True.")
print(car == 'ford')

print("\nIs car == 'audi'. I predict False")
print(car == 'audi')

## 5.2 More Conditional Tests
my_car = 'dodge'
fav_car = input(print("What's your favorite car brand?"))
if fav_car.lower() == my_car:
	print("Your favorite car is what I drive!")
else:
	print("Your favorite car is a " + fav_car + ".")

age = int(input(print("What's your age?")))
if age < 18:
	print("Sorry, you can't buy tobacco products.")
else:
	print("You are allowed to buy tobacco products.")

## 5.3 Alien Colors #1
## Imagine an alien was just shot down in a game. Create a variable
## called alien_color and assign it a value of green, yellow, or red
## Write an if statement to test whether the alien's color is green.
## If it is, print a message that the player just earned 5 points.

alien_color = 'red'

if alien_color == 'green':
	print("You earn 5 points for shooting a green alien.")

alien_color = 'green'
if alien_color == 'green':
	print("You earn 5 points for shooting a green alien.")

## 5.4 Alien Colors #2

