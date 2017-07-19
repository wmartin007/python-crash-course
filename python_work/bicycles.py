## Chapter 3 Python Crash Course
## Lists

## python lists are indicated by brackets [] and individual elements
## are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

## lists are ordered collections. Access an element like so:
print(bicycles[0]) ## python index begins at 0

## you can also use string methods on any element in a list
print(bicycles[0].title())

## python has special syntax for accessing last element in a list
## by asking for the item at index -1, python returns the last item
print(bicycles[-1])

## you can use invidivudal values from a list just as you would any other variable
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

## you can also modify elements in a list in a similar manner to accessing
## that element

motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)
motorcyles[0] = 'ducati'
print(motorcyles)

## appending elements to a list - there are several methods to add new data
## to existing lists

motorcyles.append('honda')
print(motorcyles)

## append method makes it easy to create list dynamically

shoes = []
shoes.append('nike')
shoes.append('adidas')
shoes.append('reebok')
print(shoes)

## the insert method allows us to insert a new element at any position in the list
## insert(a,b) opens a space at position a and stores the value b at that location
## this will shift every other value in the position to the right after the insert
shoes.insert(0, 'cole haan')
print(shoes)

## removing elements
## you can remove elements in a list with the del statement
## this works when you know the position of the element to delete
del shoes[0]
print(shoes)

## you can no longer access the values you delete with the del statement
## the pop() method will allow you to work with elements you would like
## to remove from a list
shoes.insert(0, 'cole haan')
print(shoes)

## pop() removes the last element in a list, but will allow
## you to work with that element after you remove it
popped_shoes = shoes.pop()
print(shoes)
print(popped_shoes)

## you can use pop to remove an item in a list at any position by 
## including the index of the item inside the parentheses
recent_bike = bicycles.pop(-1)
print(recent_bike)

## the remove() method is useful if you don't know the position but
## you do know the value of the item you want to remove

motorcyles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcyles)

motorcyles.remove('ducati')
print(motorcyles)
## you can also use the remove() method to work with a value that's
## being removed from a list
motorcyles.append('ducati')
print(motorcyles)

too_expensive = 'ducati'
motorcyles.remove(too_expensive)
print(motorcyles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

## NOTE: the remove() method only deletes the first occurence of the
## value you specify. A loop is needed to deteremine if all values
## have been removed
