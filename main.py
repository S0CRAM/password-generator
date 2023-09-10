# Password Generator 
# By S0CR4M


#---Imports
import string
import random

#---Arrays for available options
alpha = list(string.ascii_letters)
numbers = list(string.digits)
punct = list(string.punctuation)

#---Loop check
check = True

while(check):
    password = ""
    ask = input("Choose an Option\n1. Use alphabetic and numbers\n2. Use alphabetic, numbers, and punctuation\nInput: ")
    lencheck = True

    while(lencheck):
        length = input("Input a range between 16 and 32 for length of password: ")
        if(int(length) < 16 or int(length) > 32):
            print("You did not input a valid range. Try again.\n")
        else: 
            lencheck = False

    if(ask == "1"):
        while(len(password) < int(length)):
            choice = random.randint(0,1)
            if(choice == 0):
                password += alpha[random.randrange(len(alpha))]
            else:
                password += numbers[random.randrange(len(numbers))]

    if(ask == "2"):
        while(len(password) < int(length)):
            choice = random.randint(0,2)
            if(choice == 0):
                password += alpha[random.randrange(len(alpha))]
            elif(choice == 1):
                password += numbers[random.randrange(len(numbers))]
            else:
                password += punct[random.randrange(len(punct))]

    print(password)
    checkSecond = input("\nGenerate a new password? Y/N: ")
    if(checkSecond == 'y' or checkSecond == 'Y'): pass
    elif(checkSecond == 'n' or checkSecond == 'N'): check = False
    else: print("Invalid Input... Exiting...\n")

