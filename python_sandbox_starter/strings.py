# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Jake"
age = 37

#Concatinate
print("hello, im " + name + " and I am " + str(age))



# String Formatting

#Arguments by position
print("My name is {name} and I am {age}". format(name = name, age = age))

#F=Strings
print(f"Hello my name is {name} and i am {age}")

# String Methods

s = "hello world"

#Captialize string
print(s.capitalize()) # OUT---- "Hello world"

# Make all uppercase
print(s.upper()) # OUT---- "HELLO WORLD"

# Make all lower
print(s.lower()) # OUT---- "hello world"

# Swap case
print(s.swapcase()) # OUT---- "HELLO WORLD"

# Get length
print(len(s)) # OUT---- 11

# Replace
print(s.replace('world', 'everyone')) # OUT---- "hello everyone"

# Count
sub = 'h'
print(s.count(sub)) # OUT---- 1

# Starts with
print(s.startswith('hello')) # OUT---- True

# Ends with
print(s.endswith('d')) # OUT---- True

# Split into a list
print(s.split()) # OUT---- ['hello', 'world']

# Find position
print(s.find('r')) # OUT---- 8

# Is all alphanumeric
print(s.isalnum()) # OUT---- False

# Is all alphabetic 
print(s.isalpha()) # OUT---- False

# Is all numeric
print(s.isnumeric()) # OUT---- False
