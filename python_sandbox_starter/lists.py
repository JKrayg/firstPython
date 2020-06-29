# A List is a collection which is ordered and changeable. Allows duplicate members.


#Create a List
numbers = [1, 2, 3, 4, 5, 6]
fruits = ["apples", "oranges", "grapes", "bananas"]

#Constructor
numbers2 = list((1, 2, 3, 4, 5, 6))

print(numbers, numbers2)

#Get Value
print(fruits[1])

#Get Length of List
print(len(fruits))

#Append to List
fruits.append("Mangos")


#Remove from List
fruits.remove("grapes")

#Insert into position
fruits.insert(3, "pineapple")

#Change value
fruits[0] = "Blueberries"

#Remove with pop
fruits.pop(2)

#Reverse List
fruits.reverse()

#Sort List
fruits.sort()

#Reverse Sort
fruits.sort(reverse = True)
print(fruits)