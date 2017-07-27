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
