########################################
# EECS1015- Fall 2022
# Lab 1
#
# Your name: Bardia Moshiri
# Your section: A
# Your student ID:
# Your email contact: fakeshell@bardia.tech
#######################################

# Please fill out your info for each lab
import os

command = 'clear'

if os.name in ('nt', 'dos'):
     command = 'cls'
os.system(command)

print("---- Lab 1 ----")
print("Name: Bardia Moshiri")
print("Section A")
print("Student id:")
print("Email: fakeshell@bardia.tech")

#
#
#
#
#
#
# Task 1
print('\n---- Task 1: Currency converter ----')

while True:
    try:
        userCurrency = float(input("\033[1;32mEnter some amount (CAD) here: "))
        print ("")
    except ValueError:
        print("\033[1;31mI said some amount, which means a number you dumbo. try again")
        print ("")
        continue
    else:
        break

USD = userCurrency * 0.76
EUR = userCurrency * 0.75
NGN = userCurrency * 322.24
CNY = userCurrency * 5.25
INR = userCurrency * 97.14

print ("\033[1;37mUSD: ", USD)
print ("\033[1;37mEUR: ", EUR)
print ("\033[1;37mNGN: ", NGN)
print ("\033[1;37mCNY: ", CNY)
print ("\033[1;37mINR: ", INR)

#
#
#
#
#
#
# Task 2
print('\n---- Task 2: String math ----')

userString1 = input("\033[1;32mEnter your first string: ")
userString2 = input("\033[1;32mEnter your second string: ")
userString3 = input("\033[1;32mEnter your third string: ")
print ("")

firstResult = userString1 + userString2 + userString3
secondResult = userString3 + userString2 + userString1
thirdResult = userString2 + userString1 + userString3
forthResult = userString2 + userString3

print ("\033[1;37m", firstResult)
print ("\033[1;37m", secondResult)
print ("\033[1;37m", thirdResult)

print ("")

while True:
    try:
        userInteger = int(input("\033[1;32mEnter some number here: "))
        print ("")
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        continue
        print ("")
    else:
        break

for i in range (userInteger):
     print ("\033[1;37m", userString1, end="")

print ("")

for i in range (userInteger):
     print ("\033[1;37m", forthResult, end="")

print ("")

#
#
#
#
#
#
# Task 3
print("\n---- Task 3: Math operators ----")

while True:
    try:
        userNum1 = int(input("\033[1;32mEnter your first number (integer) here: "))
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        print ("")
        continue
    else:
        break

while True:
    try:
        userNum2 = int(input("\033[1;32mEnter your second number (integer) here: "))
        print ("")
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        print ("")
        continue
    else:
        break

firstResult = userNum1 / userNum2
secondResult = userNum1 // userNum2
thirdResult = userNum1 % userNum2
forthResult = userNum1**userNum2

print ("\033[1;37mFirst number / Second number: ", firstResult)
print ("\033[1;37mFirst number // Second number: ", secondResult)
print ("\033[1;37mFirst number % Second number: ", thirdResult)
print ("\033[1;37mFirst number^Second number: ", forthResult)

print ("")

while True:
    try:
        userNum1 = float(input("\033[1;32mEnter your first number (float) here: "))
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        print ("")
        continue
    else:
        break

while True:
    try:
        userNum2 = float(input("\033[1;32mEnter your second number (float) here: "))
        print ("")
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        print ("")
        continue
    else:
        break

firstResult = userNum1 / userNum2
secondResult = userNum1 // userNum2
thirdResult = userNum1 % userNum2
forthResult = userNum1**userNum2

print ("\033[1;37mFirst number / Second number: ", firstResult)
print ("\033[1;37mFirst number // Second number: ", secondResult)
print ("\033[1;37mFirst number % Second number: ", thirdResult)
print ("\033[1;37mFirst number^Second number: ", forthResult)

#
#
#
#
#
#
# Task 4
print('\n---- Task 4: Simple cylinder computation ----')

while True:
    try:
        radius = float(input("\033[1;32mEnter the radius here: "))
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        print ("")
        continue
    else:
        break

while True:
    try:
        height = float(input("\033[1;32mEnter the height here: "))
        print ("")
    except ValueError:
        print("\033[1;31mI said some number you dumbo. try again")
        print ("")
        continue
    else:
        break

pi = 355 / 113
SurfaceArea = 2 * pi * radius * height + 2 * pi * radius**2
volume = pi * radius**2 * height

print ("\033[1;37mCylinder surface area: ", SurfaceArea)
print ("\033[1;37mCylinder volume: ", volume)

## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\033[1;32m\n---- FINISHED ----")
input("Press enter to end.")
