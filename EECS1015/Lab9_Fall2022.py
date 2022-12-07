########################################
# EECS1015- Fall 2022
# Lab 8
#
# Your name: Bardia Moshiri
# Your section: A
# Your student ID:
# Your email contact: fakeshell@bardia.tech
#######################################
import random
import os

command = 'clear'

if os.name in ('nt', 'dos'):
     command = 'cls'
os.system(command)

def student_info():
    print("Name: Bardia Moshiri")
    print("Student ID:")
    print("Email: fakeshell@bardia.tech")
    print("Section: A")
    print("Lab: A")

def task0():
    student_info()

def task1():
   while True:
      mainString = input("Type in a long sentence: ")
      subString = input("Remove words containing: ")
      stringList = mainString.split()
      with_substring = []
      without_substring = []

      for word in stringList:
          if subString in word:
              without_substring.append(word)
          else:
              with_substring.append(word)

      wss = " ".join(without_substring)
      ws = " ".join(with_substring)
      print (f"With substring '{wss}'\nW/o substring: '{ws}'")
      yn = input("Try again? [Y/N] ").upper()

      if yn == "Y":
          pass
      else:
          break

# write randomlist and reshape for task2 below
def randomlist(N):
    randomList = []
    for i in range(0, N):
        randomNum = random.randint(0, 9)
        randomList.append(randomNum)
    return randomList

def reshape(a_list, rows, cols):
    reshapeList = []
    newList = []
    for i in a_list:
        if len(newList) == cols:
            reshapeList.append(newList)
            newList = []
            newList.append(i)
        else:
            newList.append(i)

    reshapeList.append(newList)
    return reshapeList

def task2():
    while True:
       length = int(input("List length: "))
       myList = randomlist(length)
       print(myList)

       rows = int(input("Rows: "))
       cols = int(input("Cols: "))

       if rows * cols != length:
           print(f"Error: {rows}*{cols} != {length}")
       else:
           newList = reshape(myList, rows, cols)
           print(f"Reshaped list\n{newList}")

       yn = input("Try again? [Y/N] ").upper()

       if yn == "Y":
           pass
       else:
           break

# write function find_duplicates() for task 3 below
def find_duplicates(a_dict):
    testDict = {}
    for key, value in a_dict.items():
        if value not in testDict:
            testDict[value] = [key]
        elif value in testDict:
            testDict[value].append(key)

    newDict = testDict.copy()
    for key, value in testDict.items():
        if len(value) == 1:
           del newDict[key]

    return newDict

def task3():
    while True:
       i = 1
       myDict = {}
       while True:
          word = input(f"[Input {i}] Word: ")
          if word == "":
              break
          else:
              myDict[i] = word
              i = i + 1

       print(f"Dictionary\n{myDict}")

       duplicateDict = find_duplicates(myDict)
       print(f"Duplicates\n{duplicateDict}")
       yn = input("Try again? ").upper()
       if yn == "Y":
           pass
       else:
           break

# write class rangeChecker for task4 below
class rangeChecker:
    range_counter = 1

    def __init__(self, name, min, max):
        assert max > min, f"Max ({max}) must be greater than min ({min})"
        self.id = rangeChecker.range_counter
        rangeChecker.range_counter = rangeChecker.range_counter + 1
        self.min_value = min
        self.max_value = max
        self.name = name

    def within_range(self, number):
        if self.min_value <= number <= self.max_value:
            return True
        else:
            return False

    def outside_range(self, number):
        if number < self.min_value or number > self.max_value:
            return True
        else:
            return False

    def print(self):
        print(f"rangeChecker [{self.id:2}]   '{self.name:10}'  - {self.min_value:8.2f} <= num <= {self.max_value:8.2f}")

def task4():
    while True:
        firstRange = input("Range 0 Name, Min, Max: ").replace(" ", "")
        firstList = []
        firstList = firstRange.split(",")
        firstClass = rangeChecker(firstList[0], float(firstList[1]), float(firstList[2]))

        secondRange = input("Range 1 Name, Min, Max: ").replace(" ", "")
        secondList = []
        secondList = secondRange.split(",")
        secondClass = rangeChecker(secondList[0], float(secondList[1]), float(secondList[2]))

        thirdRange = input("Range 2 Name, Min, Max: ").replace(" ", "")
        thirdList = []
        thirdList = thirdRange.split(",")
        thirdClass = rangeChecker(thirdList[0], float(thirdList[1]), float(thirdList[2]))

        numberString = input("Input list of numbers x1, x2,..,xn: ").replace(" ", "")
        numberList = numberString.split(",")

        firstClass.print()
        for i in range(0, len(numberList)):
            tf = firstClass.within_range(float(numberList[i]))
            print(f"Inside range [{float(numberList[i]):8.2f}]: {tf}")

        secondClass.print()
        for i in range(0, len(numberList)):
            tf = secondClass.within_range(float(numberList[i]))
            print(f"Inside range [{float(numberList[i]):8.2f}]: {tf}")

        thirdClass.print()
        for i in range(0, len(numberList)):
            tf = thirdClass.within_range(float(numberList[i]))
            print(f"Inside range [{float(numberList[i]):8.2f}]: {tf}")

        firstClass.print()
        for i in range(0, len(numberList)):
            tf = firstClass.outside_range(float(numberList[i]))
            print(f"Outside range [{float(numberList[i]):8.2f}]: {tf}")

        secondClass.print()
        for i in range(0, len(numberList)):
            tf = secondClass.outside_range(float(numberList[i]))
            print(f"Outside range [{float(numberList[i]):8.2f}]: {tf}")

        thirdClass.print()
        for i in range(0, len(numberList)):
            tf = thirdClass.outside_range(float(numberList[i]))
            print(f"Outside range [{float(numberList[i]):8.2f}] {tf}")

        yn = input("Try again? ").upper()
        if yn == "Y":
            pass
        else:
            break

def main():
    task0()
    print("--- Task 1 ---")
    task1()
#    print("\n--- Task 2 ---")
#    task2()
#    print("\n--- Task 3 ---")
#    task3()
#    print("\n--- Task 4 ---")
#    task4()

if __name__ == "__main__":
    main()

