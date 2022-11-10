################################
# EECS1015, York University
# Lab 6
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

def print_student_info():
    print("---- Lab 6 ----")
    print("Name: Bardia Moshiri")
    print("ID:")
    print("Section A")
    print("Email: fakeshell@bardia.tech")

def task0():
    print_student_info()

def average_num(*nums):
    amount = 0
    sum = 0
    for i in nums:
        sum = sum + i
        amount = amount + 1
    average = sum / amount
    return average

def task1():
    while True:
       iterations = int(input("Input 4 or 5 numbers? "))
       if iterations == 4:
          firstNum, secondNum, thirdNum, forthNum = input("Input 4 numbers [x1, x2, x3, x4] : ").replace(' ', '').split(",")
          firstNum = int(firstNum)
          secondNum = int(secondNum)
          thirdNum = int(thirdNum)
          forthNum = int(forthNum)
          average = average_num(firstNum, secondNum, thirdNum, forthNum)
          print(f"Average is {average}")

       elif iterations == 5:
          firstNum, secondNum, thirdNum, forthNum, fifthNum = input("Input 5 numbers [x1, x2, x3, x4, x5] : ").replace(' ', '').split(",")
          firstNum = int(firstNum)
          secondNum = int(secondNum)
          thirdNum = int(thirdNum)
          forthNum = int(forthNum)
          fifthNum = int(fifthNum)
          average = average_num(firstNum, secondNum, thirdNum, forthNum, fifthNum)
          print(f"Average is {average}")

          yn = input("Try again? ").upper()

          if yn == "Y":
              pass
          else:
              break

def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-"*31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}")
        stock_dict[k][1]
    print()

def string_to_stock_dict():
    astring = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    myList = astring.replace(' ', ':').split(":")
    stock_dict = {}
    symbol = dict()
    count = 0

    for i in myList:
        if i.isupper() == True and len(i) <= 4:
           stock_dict.update({i : ''})
           symbol[count] = i
           count = count + 1

    count = 0
    name = dict()
    for i in myList:
        if i.istitle() == True:
           name[count] = i
           count = count + 1

    count = 0
    for i in myList:
       try:
          var2float = float(i)
          stock_dict.update({symbol[count] : [name[count] , var2float]})
          count = count + 1
       except:
          pass

    print_stock_dict(stock_dict)

def task2():
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)
    string_to_stock_dict()

def create_rand_list():
    num_of_elements = random.randint(5, 15)
    min_value = random.randint(5, 10)
    max_value = random.randint(20, 50)
    myList = []
    for i in range (0, num_of_elements):
        number = random.randint(min_value, max_value)
        myList.append(number)
    return myList

def print_list(a_list):
    print("---list---")
    if len(a_list) == 0:
        myString = "(empty)"
    else:
        list2string = str(a_list).replace("[", "").replace("]", "").replace(",", ")->(").replace(" ", "")
        myString = f"({list2string})->(end)"

    return myString

def delete_item_from_list(a_list, item):
    if item in a_list:
        index = a_list.index(item)
        del a_list[index]
        return index
    else:
        return -1

def task3():
    myList = create_rand_list()

    while True:
        myString = print_list(myList)
        print(myString)
        item2delete = int(input("Item to delete: "))
        index = delete_item_from_list(myList, item2delete)

        if index != -1:
            print(f"Item {item2delete} deleted at position {index}")
        else:
            print(f"Item {item2delete} could not be deleted.")

        yn = input("Delete item [Y/N]? ").upper()

        if yn == "Y":
            pass
        else:
            break

def print_image(image):
   print("")

def uncompress_rle_image(rle_image):
    for i in range (0, len(rle_image)):
        print("")
        iterate = len(rle_image[i])
        for j in range(0, iterate):
            try:
               picture = rle_image[i][j][0] * rle_image[i][j][1]
               print(picture, end='')
            except IndexError:
               i = i + 1

def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')], [(9, ' '), (3, '8'), (1, 'l')],
     [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
     [(6, ' '), (1, '.'), (8, '8'), (1, '.')], [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
     [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')], [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
     [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
     [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'), (1, "'")],
     [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'), (1, '-'),
      (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
     [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '), (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')], [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')], [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'), (3, ' '), (2, '|'), (17, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'), (7, '.'), (7, ' '), (3, '.')], [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'), (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'), (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')], [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'), (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')], [(52, '.')]]
    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    print_image(image1)
    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)
    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)

def main():
    task0()
    print("\n--- Task 1: Average numbers ---")
    task1()
    print("\n--- Task 2: Text to dictionary---")
    task2()
    print("\n--- Task 3: Deleting from list---")
    task3()
    print("\n--- Task 4: RLE decoding  ---")
    task4()
    input("Press enter to end lab 6.")

if __name__ == '__main__':
    main()
