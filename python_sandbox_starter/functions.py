# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#Create a function
#With param
def sayHello(name):
    print(f"Hello my name is {name}")

sayHello("Jake")

#Default param
def sayHello(name = "Jake"):
    print(f"Hello my name is {name}")


#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total
num = getSum(2, 4)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

#Create lambda function
getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 3))
