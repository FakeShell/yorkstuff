########################################
# EECS1015- Fall 2022
# Lab 2
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

print("---- Lab 2 ----")
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
print("\n---- Task 1: Three year investment return ----")

username = input("\033[1;32mName: ").strip().title()

print ("")

while True:
    try:
        initialAmount = float(input("\033[1;32mInitial amount: $"))
        print ("")
    except ValueError:
        print("\033[1;31mI said some amount, which means a number you dumbo. try again")
        print ("")
        continue
    else:
        break

while True:
    try:
        returnRate = float(input("\033[1;32mRate of return: %"))
        print ("")
    except ValueError:
        print("\033[1;31mI said some amount, which means a number you dumbo. try again")
        print ("")
        continue
    else:
        break

returnPercent = returnRate / 100

print(f"\033[1;32mClient: {username}, yearly rate of return multiplier: {returnPercent}")
Year1 = initialAmount + (initialAmount * returnPercent)
Year2 = Year1 + (Year1 * returnPercent)
Year3 = Year2 + (Year2 * returnPercent)

print ("\033[1;37mYear 1\t Starting Amount: $%5.2f \t Ending Amount: $%5.2f" % (initialAmount, Year1))
print ("\033[1;37mYear 2\t Starting Amount: $%5.2f \t Ending Amount: $%5.2f" % (Year1, Year2))
print ("\033[1;37mYear 3\t Starting Amount: $%5.2f \t Ending Amount: $%5.2f" % (Year2, Year3))

#
#
#
#
#
#
# Task 2
print("\n----Task 2 Leetspeak converter ----")

leetspeak = input("\033[1;32mType a long string: ").upper().replace("T", "7").replace("A", "^").replace("E", "3").replace("I", "!").replace("B", "8").replace("O", ".").replace("C", "<").replace("S", "$")

print("\033[1;37m", leetspeak)

#
#
#
#
#
#
# Task 3
print("\n---- Task 3: Substring highlighter ----")

mainString = input("\033[1;32mType a sentence at the prompt below:  ")

subString = input("\033[1;32mEnter substring below to highlight: ")

firstLength = len(mainString)
secondLength = len(subString)

print (f"Sentence has {firstLength} characters, substring has {secondLength} characters.")
startIndex = mainString.find(subString)
endIndex = startIndex + secondLength

highlight = "*" + mainString[startIndex:endIndex].upper() + "*"

mainStringHighlighted = mainString[:startIndex] + highlight + mainString[endIndex:]

print ("\033[1;37m", mainStringHighlighted)

#
#
#
#
#
#
# Task 4
print("\n---- Task 4: Exponent ----")

exponent = input("\033[1;32mInput exponent in the form x^y: ")

firstNumber = int(exponent[0])
secondNumber = int(exponent[2])

print (f"\033[1;37mExtracted numbers: {firstNumber} {secondNumber}")

result = firstNumber ** secondNumber

print (f"\033[1;37m{firstNumber}^{secondNumber} = {result}")

# Pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")
