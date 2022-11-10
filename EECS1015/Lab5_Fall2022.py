################################
# EECS1015, York University
# Lab 5
# Name: Bardia Moshiri
# Section: A
# Student ID:
# Email: fakeshell@bardia.tech
################################

import random
import os

command = 'clear'

if os.name in ('nt', 'dos'):
     command = 'cls'
os.system(command)

# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Bardia Moshiri")
    print("Section A")
    print("Student id:")
    print("Email: fakeshell@bardia.tech")

def input_list():
    positiveList = []
    x = 0

    while (x >= 0):
        x = int(input("Input positive int: "))

        if x >= 0:
           positiveList.append(x)

    return positiveList

def compute_average(aList):
    N = len(aList)

    if N == 0:
       avg = 0
    else:
       summation = sum(aList[0:N])
       avg = summation / N

    return avg

def random_set():
    aSet = set()
    elementAmount = 0
    number = 0

    while (elementAmount != 5):
        number = random.randint(0,20)
        aSet.add(number)
        elementAmount = len(aSet)

    return aSet

def print_set(aSet, prompt=""):
    myList = list(aSet)
    firstElement = myList[0]
    secondElement = myList[1]
    thirdElement = myList[2]
    forthElement = myList[3]
    fifthElement = myList[4]
    print(f"{prompt} {firstElement} {secondElement} {thirdElement} {forthElement} {fifthElement}")


def task0():
    print_lab_info()

def task1():
    while True:
        myDict = input_list()
        average = compute_average(myDict)
        print(f"List average {average:.2f}")
        yn = input("Do again [Y/N]? ").upper()

        if yn == "Y":
            pass
        else:
            break

def task2():
    myString = input("Input a long string: ").upper()
    myList = list(myString)
    mySet = set(myList)
    myDict = {}
    for i in mySet:
        myDict.update({i:0})

    for i in myList:
        myDict[i] +=1

    for key, value in myDict.items():
        stars2show = '*' * value
        print(f"'{key}' |{stars2show}")


def task3():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']', 'K': '1',
               'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5', 'V': '!',
               'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D', '7': 'E',
               '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ':'_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J', '1': 'K',
               '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U', '!': 'V',
               '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6', 'E': '7',
               '9': '8', ')': '9', ';': '0', ',': '3', '/': '.','_': ' '}

    while True:
        myString = input("Input a message: ").upper()
        action = input("Encode (E) or Decode (D)? ").upper()

        myList = list(myString)

        if action == "E":
            for i in myList:
                 print(encoder.get(i), end="")

        elif action == "D":
            for i in myList:
                 print(decoder.get(i), end="")

        print("")
        yn = input("Encode/decode again [Y/N]? ").upper()

        if yn == "Y":
             pass
        else:
             break

def task4():
    while True:

        while True:
            try:
               firstNum, secondNum, thirdNum, forthNum, fifthNum = input("Enter 5 numbers between 1-20: ").split()
            except ValueError:
               continue
            else:
               break

        firstNum = int(firstNum)
        secondNum = int(secondNum)
        thirdNum = int(thirdNum)
        forthNum = int(forthNum)
        fifthNum = int(fifthNum)
        userSet = set({firstNum, secondNum, thirdNum, forthNum, fifthNum})

        while True:
            if len(userSet) != 5:
               firstNum, secondNum, thirdNum, forthNum, fifthNum = input("Enter 5 numbers between 1-20: ").split()
               firstNum = int(firstNum)
               secondNum = int(secondNum)
               thirdNum = int(thirdNum)
               forthNum = int(forthNum)
               fifthNum = int(fifthNum)
               userSet = set({firstNum, secondNum, thirdNum, forthNum, fifthNum})
            else:
               break

        randomSet = random_set()
        print_set(randomSet, "Computer's numbers:")
        matches = set()
        matches = userSet.intersection(randomSet)

        intersectionLen = len(matches)
        matchString = str(matches).replace("{", "").replace("}", "").replace(",", "")

        if intersectionLen == 5:
           print("YOU WIN!")
        elif intersectionLen == 0:
           print("NO MATCHES")
        else:
           print(f"{intersectionLen} matches found: {matchString}")

        yn = input("Do again [Y/N]? ").upper()

        if yn == "Y":
            pass
        else:
            break

def main():
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()

if __name__ == "__main__":
    main()
