age = 29
## message = "Happy " + age + "th Birthday!"

##print(message)  will throw an error because age is an int
## you can't concatenate an int with a string

message = "Happy " + str(age) + "th Birthday!"
print(message)
