# A variable is a container for a value, which can be of various types
"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

#------------------------------------------------------------------------------------
#====================================================================================
#------------------------------------------------------------------------------------

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

# a hashtag is how you comment
#------------------------------

x = 1           #int
y = 2.5         #float    #---------------------------------
name = "jake"   #string                                    |
is_cool = True  #boolean                                   |
                                                          #|---- Affectively the same thing
                                                          #|
x, y, name, is_cool = (1, 2.5, "jake", True)  #-------------

#Basic math
a = x * y

#Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
