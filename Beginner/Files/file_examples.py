#Title: File System to Save Users Email and Phone Numbers
#Author: Chris Carpenter 
#Date: 12/1/2022

def getInfo():
    name = input("Hello. What is your name?")
    phone = input("And your phone number? ")
    email = input("And your email please? ")

    line_to_store = "Name: " + name + " Phone: " + phone + " Email: " + email
    return line_to_store

def storeInfo(userInfo):
    with open("users.txt", "a") as file:
        file.write(userInfo + "\n")


while True:
    currentUser = getInfo()
    storeInfo(currentUser)
    if (input("Would you like to continue? (y for yes) ") == 'y'):
        continue
    else:
        break
