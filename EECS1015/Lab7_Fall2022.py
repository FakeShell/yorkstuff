########################################
# EECS1015- Fall 2022
# Lab 7
#
# Your name: Bardia Moshiri
# Your section: A
# Your student ID:
# Your email contact: fakeshell@bardia.tech
#######################################

import os

command = 'clear'

if os.name in ('nt', 'dos'):
     command = 'cls'
os.system(command)

x = 0

# Print info
def print_student_info():
    print("---- Lab 7 ----")
    print("Name: Bardia Moshiri")
    print("Section A")
    print("Student id:")
    print("Email: fakeshell@bardia.tech")

def task0():
    print_student_info()

def is_sorted(a_list):
    testList = a_list[:]
    testList.sort()
    if (testList == a_list):
       return True
    else:
       return False

def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    firstResult = is_sorted(x1)
    secondResult = is_sorted(x2)
    thirdResult = is_sorted(x3)
    print(f"{firstResult} {secondResult} {thirdResult}")

def merge_dict(firstDict, secondDict):
    for key in firstDict:
        secondDict[key] = firstDict[key]
    print(f"dict2 merged into dict1\n{secondDict}")

def task2():
    dict1 = {8:"Exercise", 9:"Breakfast", 12:"Lunch", 3:"Study", 6:"Netflix"}
    dict2 = {8:"Sleep", 10:"Lab", 12:"Class", 4:"Call Mom"}
    print(f"dict1\n{dict1}")
    print(f"dict2\n{dict2}")
    merge_dict(dict1, dict2)

def invert_dict(a_dict):
    invertedDict = dict()
    for key in a_dict:
        value = a_dict[key]
        invertedDict[value] = key
    return invertedDict

def task3():
    a_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
    print(a_dict)
    invertedDict = invert_dict(a_dict)
    print(invertedDict)

def list_to_dict(my_list):
    myDict = dict()
    i = 0
    for value in my_list:
        myDict[i] = value
        i = i + 1
    return myDict

def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1:"1", 2:"2"}]
    myDict = list_to_dict(my_list)
    print(f"{my_list}\n{myDict}")

x = 0
def str_list_to_num_list(a_list):
    newList = []
    global x
    for value in a_list:
        intValue = int(value)
        newList.append(intValue)
    print(newList)

def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(x)
    str_list_to_num_list(x)

def merge_lists(list1, list2):
    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    index1 = 0
    index2 = 0
    while index1 < len1 and index2 < len2:
        if list1[index1] <= list2[index2]:
            new_list.append(list1[index1])
            index1+=1
        else:
            new_list.append(list2[index2])
            index2+=1

    if index1 < len1:
         new_list.extend(list1[index1:])
    if index2 < len2:
         new_list.extend(list2[index2:])
    return new_list

def task6():
    while True:
        firstList = input("Input 1st sorted list of numbers [x1 x2 ...]: ").split()
        secondList = input("Input 2nd sorted list of numbers [y1 y2 ...]: ").split()
        assert is_sorted(firstList) == True, "List 1 is not sorted!"
        assert is_sorted(secondList) == True, "List 2 is not sorted"
        newList = merge_lists(firstList, secondList)
        print(f"Merged list\n{newList}")

        yn = input("Try again [Y/N]? ").upper()

        if yn == "Y":
            pass
        else:
            break

def main():
    task0()
    print("\n---- Task 1: Check if list is sorted ----")
    task1()
    print("\n---- Task 2: Merge dictionaries ----")
    task2()
    print("\n---- Task 3: Invert dictionaries ----")
    task3()
    print("\n---- Task 4: List to dictionary ----")
    task4()
    print("\n---- Task 5: String list to num list ----")
    task5()
    print("\n---- Task 6: Merge list with assert ----")
    task6()

if __name__ == "__main__":
    main()
