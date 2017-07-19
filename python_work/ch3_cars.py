
## lists are often unordered initially
cars = ['bwm', 'audi', 'toyota', 'subaru']

## the sort() method permanently alters the order of your list
cars.sort()
print(cars)

## you can sort in reverse by adding the argument reverse = True
## to the sort method
cars.sort(reverse = True)
print(cars)

## To maintain the original order of a list but present in a
## sorted order, use the sorted() function

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

## NOTE: sorting a list alphabetically gets more complicated
## when all values aren't in lower case

## Printing a list in reverse order
## This won't sort backwards alphabetically 
## It will alter the list permanently
cars.reverse()
print(cars)

## The len() function gives you the length of a list
print(len(cars))

##pg 48
