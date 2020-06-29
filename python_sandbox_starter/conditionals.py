# If/ Else conditions are used to decide to do something based on something being true or false

x = 13
y = 132

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#if statement
if x > y:
    print(f"{x} > {y}")

#if/else statement
if x > y:
    print(f"{x} > {y}")
else: print(f"{y} > {x}")

#else/if statement
if x > y:
    print(f"{x} > {y}")
elif x == y:
    print(f"{x} = {y}")
else:
    print(f"{y} > {x}")


#Nested if
if x > 2:
    if x <= 10:
        print(f"{x} > 2 and <= 10")


# Logical operators (and, or, not) - Used to combine conditional statements
#And
if x > 2 and x <= 10:
    print(f"{x} > 2 and <= 10")

#Or
if x > 2 or x <= 10:
    print(f"{x} > 2 and <= 10")

#Not
if not(x == y):
    print(f"{x} != {y}")



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#In
if x in numbers:
    print(x in numbers)

#Not in
if x not in numbers:
    print(x not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


#Is
if x is y:
    print(x is y)

#Is Not
if x is not y:
    print(x is not y)