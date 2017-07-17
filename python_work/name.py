name = "ada lovelace"
print(name.title()) ## title() displays each word in titlecase; Ada Lovelace
print(name.upper()) ## upper() and lower() are different string methods
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name ## python uses + to concatenate strings

print("Hello, " + full_name.title() + "!")

print("Python")
print("\tPython") ## \t adds a tab to text

print("Languages:\nPython\nC\nJavaScript") ## \n adds a newline
print("Languages:\n\tPython\n\tC\n\tJavaScript") ## you can combine \n and \t

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip()) ## rstrip strips the white space at the right end
## remember that the above doesn't change the variable; favorite_language still
## will return 'python '

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
