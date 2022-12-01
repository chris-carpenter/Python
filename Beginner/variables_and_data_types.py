#Title:  Data Types
#Author: Chris Carpenter
#Date:   12/01/2022

#Data Types can be classified as numeric.
#Floats allow decimal places.
bankAccount = 1299.49
print(type(bankAccount))

#Integers are whole numbers
age = 30
print(type(age))

#Data Types can also be Sequence Types which contain one or more objects in a list.
#String is a sequence of characters.
name = 'Chris'
print(type(name))

#Lists hold an array of different values
months = ['Jan', 'Feb', 'March', 'April', 'May']
print(type(months))
print(months[4])
print(len(months)) #Although the index of the last item is 4, the length is still # of items.

#Dictionaries hold data pairs
nameAndAge = {'Chris': 30, 'Sally': 34, 'Jenifer': 28}
print(nameAndAge['Chris'])
print(type(nameAndAge['Chris'])) #values stored in a dictionary are still whatever value assigned

#Tuple data cannot be changed once assigned
citiesVisited = ('Orlando', 'San Diego', 'Seattle', 'New York')
print(type(citiesVisited))

#Set
thisIsASet = {1, 'b', 22, 'a'}
print(type(thisIsASet))