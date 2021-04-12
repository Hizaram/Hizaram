#REGISTER
#FIRSTNAME,LASTNAME, PASSWORD AND EMAIL
#GENERATE USER ACCOUNT


#LOGIN
#ACCOUNT NUMBER AND PASSWORD


#BANK OPERATIONS

#INITIALISING THE SYSTEM
import random

#CREATING A DATABASE FOR OUR USER CREDENTIALS
database = {}


def init():

    isOptionSelectedValid = False
    print("Welcome to bank CSB")

    while isOptionSelectedValid == False:

        haveAccount = int(input("Do you have an account with us? 1(yes) or 2(no) \n"))

        if(haveAccount == 1):
            isOptionSelectedValid = True
            login()
        elif(haveAccount == 2):
            isOptionSelectedValid = True
            print(register())
        else:
            print("You have selected a wrong option, please try again")

def login():
    print("********* Login *********")

    isLoginSuccessful = False

    while isLoginSuccessful == False:

        accountNumberFromUser = int(input("What is your account number? \n"))
        password = (input("What is your password? \n"))

        for accountNumber, userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == password:
                    isLoginSuccessful = True

            else:
                print("Invalid account number or password") 
    

    bankOperations(userDetails)

def register():

    print("****** Register ******")
    
    email = input("What is your email address? \n")
    firstName = input("What is your  first name? \n")
    lastName = input("What is your  last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password]

    print("Your account has been created")
    print('== ======= ========= ===== ==')
    print("Your account number is: %d" % accountNumber)
    print('== ======= ========= ===== ==')
    print('Make sure you keep it safe')
    print('== ======= ========= ===== ==')

    login()

def bankOperations(user):
    print("Welcome %s %s" % ( user[0], user[1] ))

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)



### ACTUAL BANKING SYSTEM ###

init()