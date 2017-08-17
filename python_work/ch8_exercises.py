## 8.1 Message
# Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    print("I'm learning about functions in chapter 8.")

display_message()

## 8.2 Favorite Book
# Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    print("One of my favorite books is " + title.title())

favorite_book("harry potter and the sorcererss stone")

## 8.3 T-Shirt
# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, text):
    print("\nYou've ordered a " + size + " shirt that says " + text)

make_shirt('large', '"Suck it Trebek"')
make_shirt(size = 'smedium', text = '"I need a bigger shirt"')

## 8.4 Large Shirts
# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size = 'medium', text = '"I love Python"'):
    print("\nYou've ordered a " + size + " shirt that says " + text)

make_shirt('large')
make_shirt()
make_shirt('small','"I am a big brother"')

## 8.5 Cities
# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city, country = 'united states'):
    print("\n" + city.title() + " is in " + country.title())

describe_city('Atlanta')
describe_city('las vegas')
describe_city('paris','france')


## 8.6 City Names
# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like
# this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.
def city_country(city, country):
    return(city.title() + ", " + country.title())

print(city_country('santiago', 'chile'))
print(city_country('berlin', 'germany'))
print(city_country('paris', 'france'))

## 8.7 Album
# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.
def make_album(artist, title, num_tracks = ''):
    album = {'artist': artist, 'title': title}
    if num_tracks:
        album['# of tracks'] = num_tracks
    return album

garth = make_album('garth brooks',"garth's greatest hits")
print(garth)

kenny = make_album('kenny chesney', 'road and the radio', 12)
print(kenny)

## 8.8 User Albums
# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while loop.

while True:
    print("\nEnter the album information:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist's name: ")
    if artist == 'q':
        break

    album = input("Album title: ")
    if album == 'q':
        break

    tracks = input("Number of tracks on album (leave blank if unknown): ")
    if tracks == 'q':
        break

    print(make_album(artist, album, tracks))


