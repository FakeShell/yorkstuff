########################################
# EECS1015- Fall 2022
# Lab 3
#
# Your name: Bardia Moshiri
# Your section: A
# Your student ID:
# Your email contact: fakeshell@bardia.tech
#######################################

# Please fill out your info for each lab
import os
import random
from fractions import Fraction

command = 'clear'

if os.name in ('nt', 'dos'):
     command = 'cls'
os.system(command)

print("---- Lab 3 ----")
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
print("\n---- Task 1: Simple order ----")

print ("""\033[1;37m**Select menu item**
(1) Coke [$1.00]
(2) Dosa [$2.50]
(3) Pizza [$2.25]
(4) Taco [$1.50]
(5) Tea [$1.00]
""")

coke = 1.00
dosa = 2.50
pizza = 2.25
taco = 1.50
tea = 1.00
none = 0.00

userOrder = int(input("\033[1;32mSelection: "))

if (userOrder < 1 or userOrder > 5):
   print("\033[1;31mInvalid selection - setting amount to $0")
   userOrder = 6

if userOrder == 1:
     meal = coke
elif userOrder == 2:
     meal = dosa
elif userOrder == 3:
     meal = pizza
elif userOrder == 4:
     meal = taco
elif userOrder == 5:
     meal = tea
else:
     meal = none

print (""" \033[1;37m**Discount**
(C) Child [under 18] (50% discount)
(A) Adult [18-64]
(S) Senior [65+] (25% discount)
""")

child = 0.50
senior = 0.25
empty = 1.25

userAge = input("\033[1;32mSelection age: ").upper()

if userAge == "C":
     discount = meal * child
     price = meal - discount
elif userAge == "S":
     discount = meal * senior
     price = meal - discount
elif userAge == "A":
     discount = 0
     price = meal - discount
else:
     print(f"\033[1;31m{userAge} is an invalid selection! Extra charge for you!")
     discount = empty
     price = meal * discount

print (f"""\033[1;37mAmount\t ${meal:5.2f}
Discount ${discount:5.2f}
------------------
Total\t ${price:5.2f}
""")

#
#
#
#
#
#
# Task 2

print("\n---- Task 2: Draw circle ----")

size = int(input("\033[1;32mInput size between 1-10: "))
while (size < 1 or size > 10):
      size = int(input("\033[1;32mInput size between 1-10: "))
      print("")

for y in range(-10,10):
    print("")
    for x in range(-10,10):
       if y >= 5:
          print("\033[1;37m.", end="")
       elif y <= -5:
          print("\033[1;37m.", end="")
       elif x <= -7:
          print("\033[1;37m.", end="")
       elif x >= 7:
          print("\033[1;37m.", end="")
       elif (x**2) * (y**2) <= (size**2):
          print("\033[1;37m*", end="")
       elif (x**2) * (y**2) > (size**2):
          print("\033[1;37m.", end="")
#
#
#
#
#
#
# Task 3
print("\n---- Task 3: Dice pair expected value ----")

while True:
   roll = int(input("\033[1;32mRoll dice how many times? "))

   run = 1
   old_overall = 0
   overall = 0

   for i in range(run, roll+1):
       dice1 = random.randint(1,6)
       dice2 = random.randint(1,6)
       sum = dice1 + dice2

       print (f"\033[1;37m[{dice1}]  [{dice2}] -- {sum}  Roll {i}")

       run = run+1
       old_overall = overall
       overall = old_overall + sum
       if run == roll+1:
          average = overall / roll
          print (f"\033[1;37mAverage dice pair value: {average:5.2f}")
   retry = input("\033[1;32mTry again [Y/N]? ").upper()
   if retry == "N":
      break

#
#
#
#
#
#
# Task 4
print("\n---- Task 4: Compute PI ----")

terms = int(input("\033[1;32mInput number of terms, M: "))

realpi = 3.14159265359
sum = 0

for n in range(0, terms+1):
    termCalculation = (-1)**n / (2*n+1)
    decimal2fractional = str(Fraction(termCalculation).limit_denominator())
    print (f"\033[1;37n={n} . . . adding fraction: {decimal2fractional}")

    sum = sum + termCalculation

    ourpi = 4 * sum

    print (f"\033[1;37our  pi = {ourpi:5.11f}")
    print (f"\033[1;37real pi = {realpi}")

# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")
