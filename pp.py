import time
import os

clear = lambda: os.system('clear')
DataBase = {"marmar":"marmar"}


def printIntroPage():
    print("\tPanda Protection")
    print("1) Create Account")
    print("2) Login")
    print("3) Exit")

def printMainPage():
    print("\tMain Menu")
    print("1) Open Webcam")
    print("2) Settings")
    print("3) Exit")

def printSettingsPage():
    print("\tUser Settings")
    print("1) Change Username")
    print("2) Change Password")
    print("3) Add New User")
    print("4) Return to Main Menu")

def introMenu():
    clear()
    printIntroPage()

    userChoice = int(input("Enter Choice: "))

    if(userChoice == 1):
        createAccount()
    elif(userChoice == 2):
        login()
    elif(userChoice == 3):
        exit()


def createAccount():
    clear()
    print("\tCreate Account")

    username = input("Enter Username: ")
    password = input("Enter password: ")

    checkVal = checkUserInfo(username)

    if(checkVal):
        DataBase[username] = password
        print("1) Submit")
        print("2) Exit")

        userChoice = int(input("Enter Choice: "))
        if(userChoice == 1):
            introMenu()
        else:
            exit()

    else:
        print("Username must be above 6 characters. Try Again")
        time.sleep(2)
        createAccount()

def login():
    clear()
    print("\tLogin")
    
    print(DataBase)

    username = input("Enter Username: ")
    password = input("Enter password: ")
    loginVal = verifyPassword(username, password)

    if(login):
        home()
    else:
        print("Incorrect Username or Password\n")
        time.sleep(2)

        print("1) Try again")
        print("2) Back to Main Menu")
        userChoice = int(input("Enter Choice: "))

        if(userChoice == 1):
            login()
        else:
            introMenu()

def checkUserInfo(username):
    if(len(username) < 6):
        return False
    else:
        return True


def verifyPassword(username, password):
    checkUsername = DataBase.get(username)
    if(checkUsername == None):
        return False
    else:
        if(checkUsername == password):
            print("Verified")
            return True
        else:
            return False

def home():
    clear()
    printMainPage()

    userChoice = int(input("Enter Choice: "))

    if userChoice == 1:
        openCamera()
    elif userChoice == 2:
        userSettings()
    elif userChoice == 3:
        exit()

def openCamera():
    print("Camera is open...")

def userSettings():
    print("This is settings")

def userSettings():
    clear()
    printSettingsPage()

    userChoice = int(input("Enter Choice: "))

    if userChoice == 1:
        clear()
        print("\tChange Username")
        temp = input("Enter your old username: ")

        if temp in DataBase:
            tempNew = input("Enter new username: ")
            DataBase[tempNew] = DataBase.pop(temp)
            print("Username has been changed to: ", tempNew)
            time.sleep(2)
            userSettings()
        else:
            print("Username not found...")
            time.sleep(2)
            userSettings()

    if userChoice == 2:
        clear()
        print("\tChange Password")
        temp = input("Enter Username: ")

        if temp in DataBase:
            tempNew = input("Enter new password: ")
            DataBase[temp] = tempNew
            print(DataBase)
            print("Password has been changed to: ", tempNew)
            time.sleep(2)
            userSettings()
        else:
            print("Username not found...")
            time.sleep(2)
            userSettings()

    if userChoice == 3:
        clear()
        print("\tAdd New User")

        username = input("Enter username: ")
        password = input("Enter password: ")

        DataBase[username] = password
        print("New user has been added...")
        print(DataBase)
        time.sleep(2)
        userSettings()

    if userChoice == 4:
        home()


            


    


    

introMenu()
