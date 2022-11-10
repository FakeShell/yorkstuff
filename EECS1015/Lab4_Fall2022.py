################################
# EECS1015 York Univresity
# Lab 4
# Name: Bardia Moshiri
# Section A/B A
# Student id:
# Email: fakeshell@bardia.tech
################################
import os
import time
import random

num_of_jumps= 0

command = 'clear'

if os.name in ('nt', 'dos'):
     command = 'cls'
os.system(command)

def print_student_info():
   print("---- Lab 4 ----")
   print("Name: Bardia Moshiri")
   print("Section A")
   print("Student id:")
   print("Email: fakeshell@bardia.tech")


def task1():

   def get_int_input(min_value=2, max_value=20):
       x = int(input(f"Enter a number (select between {min_value} and {max_value}): "))

       while (x < min_value or x > max_value):
           x = int(input(f"Enter a number (select between {min_value} and {max_value}): "))
       return x


   def get_yes():
       boolean = input("Randomize [Y/N]: ").upper()

       accepted_strings = {'Y', 'N'}
       while True:
           if boolean not in accepted_strings:
              boolean = input("Randomize [Y/N]: ").upper()
           else:
              break

       if boolean == "Y":
          return True
       else:
          return False

   def draw_owl(position=0, randomize=False):
       eye1 = '{o,o}'
       eye2 = '{-,o}'
       eye3 = '{o,-}'
       body = '/)_) '
       feet = ' " " '

       space = " "
       spaces = position * space

       if randomize == False:
          print (spaces, eye1)
          print (spaces, body)
          print (spaces, feet)
       elif randomize == True:
          randomEye = random.randint(1, 3)

          if randomEye == 1:
             print(spaces, eye1)
          elif randomEye == 2:
             print(spaces, eye2)
          else:
             print(spaces, eye3)

          print (spaces, body)
          print (spaces, feet)
       else:
          print (spaces, eye1)
          print (spaces, body)
          print (spaces, feet)

   animateAmount = get_int_input(2, 20)
   delay = get_int_input(1, 1000)
   delayMilliSeconds = delay / 1000
   randomize = get_yes()

   for i in range(1, animateAmount):
       draw_owl(i, randomize)
       time.sleep(delayMilliSeconds)


def task2():

   def get_float_input(min_value=1, max_value=10000):
       x = float(input(f"Enter a number (select between {min_value} and {max_value}): "))

       while (x < min_value or x > max_value):
           x = float(input(f"Enter a number (select between {min_value} and {max_value}): "))
       return x

   def get_int_input(min_value=1, max_value=10):
       x = int(input(f"Enter a number (select between {min_value} and {max_value}): "))

       while (x < min_value or x > max_value):
           x = int(input(f"Enter a number (select between {min_value} and {max_value}): "))

       return x
   def get_yes():
       boolean = input("Compute new investment [Y/N]: ").upper()

       accepted_strings = {'Y', 'N'}
       while True:
           if boolean not in accepted_strings:
              boolean = input("Compute new investment [Y/N]: ").upper()
           else:
              break

       if boolean == "Y":
          return True
       else:
          return False

   def compute_return():
       initialAmount = get_float_input(1, 10000)
       returnRate = get_float_input(0, 1)
       year = get_int_input(1, 10)

       newReturnAmount = 0
       returnAmount = initialAmount
       old_returnAmount = 0
       for i in range (1, year+1):
           old_returnAmount = returnAmount
           newReturnAmount = returnAmount * returnRate
           returnAmount = newReturnAmount + old_returnAmount

       if year == 1:
          yearString = "year"
       else:
          yearString = "years"

       print (f"Return in {year} {yearString} is: ${returnAmount:10.2f}")

   compute_return()

   while True:
       rerun = get_yes()

       if rerun == True:
           compute_return()
       else:
           break

def task3():
   def get_int_input(min_value=1, max_value=100):
       x = int(input(f"Enter a number (select between {min_value} and {max_value}): "))

       while (x < min_value or x > max_value):
           x = int(input(f"Enter a number (select between {min_value} and {max_value}): "))
       return x

   def find_largest_odd(*args):
       return max(arg for arg in args if arg & 1)

   result = dict()
   for i in range (1, 6):
       print (f"{i}/5\t", end="")
       result[i] = get_int_input(1, 100)

   while True:
      try:
         largestOdd = find_largest_odd(result[1], result[2], result[3], result[4], result[4], result[5])
      except ValueError:
         largestOdd = 1
         break
      else:
         break

   print(f"Biggest odd number: {largestOdd}.")

   global num_of_jumps
   num_of_jumps = largestOdd

def task4():

    n = 0
    for i in range (1, num_of_jumps+1):
        n = n + 1

        if n == num_of_jumps:
           frame1 = f"  o \t[ {n}]  \n /|\  \n / \  "
           print ("")
           print (frame1)
           break

        frame1 = f"  o \t[ {n}]  \n /|\  \n / \  "
        n = n + 1

        if n == num_of_jumps:
           break

        frame2 = f" \o/ \t[ {n}] \n  |   \n / \  "

        print ("")
        print (frame1)
        print ("")
        print (frame2)

def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")

if __name__ == "__main__":
    main()
