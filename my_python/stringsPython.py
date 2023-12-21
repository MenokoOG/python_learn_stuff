# strings, can use single or double quotes as mentioned before in datatype lesson.
text = 'Hello World!'
print(text)
text = "Hello World!"
print(text)
# if string contains double quotes use single quotes.
text = 'He said "I Love Python!"'
print(text)
# if string contains  single quotes, use double quotes.
text = "Let's have fun learning Python!"
print(text)
# multi line strings, to create multiline string, surround string with triple single quotes or triple double quotes.
text = '''Python is fun to learn,
for sure you are having fun
learning python too.'''
print(text)
text = """Python is fun to learn,
for sure you are having fun
learning python too."""
print(text)
# concatenating strings, simply is combining or adding strings together.
a = "Hello"
b = " World!"  # Jace (working under Menoko OG) put a space before world here to create print out space.
text = a + b
print(text)
# can concatenate as many strings as we want
a = "this is sparta"
b = "motha fucka"
c = "so step off"
d = "get happy!"
print(a + " " + b + " " + c + " " + d)
# escaping characters in a string, it helps make sure our strings are recognized as text and not pert of the code.
text = 'Let\'s learn pyhton'  # here the backslash is used to because of single quote inside single quotes.
print(text)
# indexing parts of a string, [] is used to index starting at 0 like most indexing.
text = "Hello There"
print(text[0])
print(text[4])
print(text[-1])  # starts from end of string
print(text[-5])
print(text[1:5])  # here the numbers specify a range.  also called slicing a string.

# string methods
# capitalize string, capitalize() function returns the string with first letter capitalized.
text = "lorem ipsum dolor sit amet."
x = text.capitalize()
print(x)
print(text)  # not capitalized.
# convert to upper case, upper() returns a copy of the string but in all upper case
text = "Lorem ipsum dolor sit amet."
x = text.upper()
print(x)
print(text)  # not upper
# convert to lower case. lower() function returns string but all lower case
text = "Lorem Ipsum Dolor SIT AMET"
x = text.lower()
print(x)
print(text)  # not lower
# get length of a string, len() returns the length of string
text = "Hello"
print(len(text))
# replacing parts of a string, replace() function replaces the occurences of a specified substring within another
# substring. syntax is string.replace(old, new) remember that the old substring is case-sensitive, has to match.
text = "Hello World!"
x = text.replace("world", "Fuckers!")
print(x)  # was not match for "World" so no change .replace() did nto work
text = "Hello World!"
x = text.replace("World", "Fuckers!")
print(x)
# replace() can replace all occurrences of the old substring with new.
text = "Hello World! I love World! World is Awesome!"
x = text.replace("World", "you fuckers")
print(x)
# you can also specify how many occurrences you would like to be replaced
text = "Hello World! I love World! World is Awesome!"
x = text.replace("World", "you fuckers", 2)
print(x)
# to check if a substring is present within a string use the in keyword, it returns True statement if True
text = "This is fun to learn today."
x = "learn" in text
print(x)
# alternately you can use the not in keyword, it also returns True if True
text = "This is fun to learn today."
x = "learn" not in text
print(x)
text = "This is fun to learn today."
x = "fuckers" not in text
print(x)
