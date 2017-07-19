## 3.8
## Create a list of places you'd like to visit and print it

locations =  ['lake tahoe', 'paris', 'maldives', 'peru']
print(locations)

## Print a temporary sorted list
print(sorted(locations))

## Show list is still in original order by printing it
print(locations)

## Use reverse to change the order of the list
locations.reverse()
print(locations)

## Use reverse again to put list in original order
locations.reverse()
print(locations)

## Use sort() to change list so that it's in alpha order
## Print to show it's permanently changed
locations.sort()
print(locations)

## Use sort to change list so it's stored in reverse alpha order
locations.sort(reverse = True)
print(locations)

## 3.9 Using len
print('You have ' + str(len(locations)) + ' on your list to visit.')

## 3.10

## 3.11
print(locations[4]) 
## This will throw an error due to only having 4 locations [0:3]
print(locations[-1] 
## This is usually a good way to get the last value in a list
## However, it will throw an error on an empty list


