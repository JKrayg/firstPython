# Python has functions for creating, reading, updating, and deleting files.

#Open a file

myFile = open("myFile.txt", "w")

#Get info from file
print("name: ", myFile.name)
print("is closed: ", myFile.closed)
print("opening mode: ", myFile.mode)

#Write to file
myFile.write("i love python")
myFile.write(" and Javascript")
myFile.close()

#Append to file
myFile = open("myFile.txt", "a")
myFile.write(" i also hate php")

#Read from file
myFile = open("myFile.txt", "r+")
text = myFile.read(100)
print(text)