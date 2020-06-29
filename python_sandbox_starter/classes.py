# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create a class
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def hasBirthday(self):
        self.age += 1


#Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"



#Initialize user object
jake = User("Jake Krayger", "jake@jake.com", 23)


#Initialize customer
Jane = Customer("Jane Doe", "Jane@jane.com", 34)

Jane.setBalance(500)
print(Jane.greeting())

jake.hasBirthday()
print(jake.greeting())