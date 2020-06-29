# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create tuple
fruits = ("apples", "oranges", "grapes")
#fruits2 = tuple(("apples", "oranges", "grapes"))

#Singles value needs trailing comma
fruits2 = ("apples",)

#Get value
print(fruits[1])

#Cant change value
fruits[0] = "pears"

#Delete tuple
del fruits2

#Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

#Create a set
fruitsSet = {"apples", "bananas", "pineapple"}

#Check if in set
print("apples" in fruitsSet)

#Addto set
fruitsSet.add("grape")
print(fruitsSet)

#remove from set
fruitsSet.remove("grape")

#Add duplicate -- wont add, duplicates not allowed
fruitsSet.add("apples")

#Clear set
fruitsSet.clear()

#Delete set
del fruitsSet
print(fruitsSet)
