# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create dictionary
person = {
    "firstName": "Jake",
    "lastName": "Doe",
    "age": 23
}

#Use constructor
person2 = dict(firstname = "Joe", lastName = "Bro")

#Get value
print(person["firstName"])
print(person.get("lastName"))

#Add keyvalue
person["phone"] = "345235235"
print(person)

#Get dictionary keys
print(person.keys())

#Get dictionary items
print(person.items())

#Copy dictionary
person3 = person.copy()
person3["city"] = "philly"

#Remove item
del(person["age"])
person.pop("phone")

#Clear
person.clear()

#Get Length
print(len(person3))

#List of dictionaries
people = [
    {
        "name": "Ben",
        "age": 30,
    },
    {
        "name": "steve",
        "age": 60
    }
]
print(people)