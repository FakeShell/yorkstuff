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

money = 100

def print_student_info():
    print("Name: Bardia Moshiri")
    print("Student ID:")
    print("Section A")
    print("Email: fakeshell@bardia.tech")

def find_mutation(virus1, virus2):
    myString = "                                                  "
    changes = 0
    newString = ""
    endIndex = len(myString)
    for i in range (0, len(virus1) - 1):
        if virus1[i] != virus2[i]:
           newString = myString[:i] + "^" + myString[:endIndex]
           myString = newString
           changes = changes + 1

    myString = myString[0:50]
    return myString, changes

# class for task 2
class virus:
    def __init__(self, DNAInput=""):
        self.DNA = ""
        self.allowedCharacters = "AGTC"
        if DNAInput != "":
            if len(DNAInput) == 50:
                if all(ch in self.allowedCharacters for ch in DNAInput):
                   self.DNA = DNAInput

        if self.DNA == "":
           self.DNA = ''.join(random.choice('AGTC') for _ in range(50))

    def getDNA(self):
        return self.DNA

    def replicate(self):
        self.random = random.randint(1, 100)
        if self.random > 94:
            self.randomMutate = random.randint(0, 49)
            self.randomChar = random.choice(self.allowedCharacters)
            self.newDNA = self.DNA[:self.randomMutate] + self.randomChar + self.DNA[self.randomMutate + 1:]
            x = virus(self.newDNA)
        else:
            x = virus(self.DNA)
        return x

# class for task 1
class lotto_ticket:
    ticket_counter = 1

    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_counter
        lotto_ticket.ticket_counter += 1

        self.numbers = set(random.sample(range(1, 21), 5))

    def print_ticket(self):
        ticketString = f"Ticket #[{self.ticket_id:3d}]"
        for t in self.numbers:
            ticketString += f"  {t:2d}  "
        print(ticketString)

    def print_and_return_win(self, lotto_numbers):
        numbersMatching = 0
        winningString = f"Ticket #[{self.ticket_id:3d}]"
        for t, l in zip(self.numbers, lotto_numbers):
            if (t == l):
                numbersMatching += 1
                winningString += f" *{t:02d}* "
            else:
                winningString += f"  {t:02d}  "

        winningAmount = 0

        if numbersMatching == 3:
            winningAmount = 2
        elif numbersMatching == 4:
            winningAmount = 20
        elif numbersMatching == 5:
            winningAmount = 100

        winningString += f"  [{numbersMatching} matches, ${winningAmount}]"
        print(winningString)

        return winningAmount

def lotto_draw():
    return set(random.sample(range(1, 21), 5))

def task0():
    print_student_info()

def task1():

    global money
    while (True):
        NumberOfTickets = -1

        while ((NumberOfTickets < 0) or (NumberOfTickets * 2 > money)):
            print(f"The amount the user has is ${money}")
            NumberOfTickets = int(input("How many lotto tickets do you want to purchase: "))

        if (NumberOfTickets == 0):
            break
        else:
            money -= NumberOfTickets * 2
            ticketList = list()

            for i in range(NumberOfTickets):
                tickets = lotto_ticket()
                tickets.print_ticket()
                ticketList.append(tickets)

            lotto_numbers = lotto_draw()

            print(f"Lotto Numbers: {lotto_numbers}")

            input("Please press enter to see your winnings.")

            for ticket in ticketList:
                winningAmount = ticket.print_and_return_win(lotto_numbers)
                money += winningAmount
            print(f"The new amount of the user is ${money}")

            if (money < 2):
                break

def task2():

    while True:
        virusName = input("Name of virus: ")
        myVirus = virus()
        originalDNA = myVirus.getDNA()
        print(f"Original DNA sequence: {originalDNA}")
        iterateAmount = int(input("How many times to replicate? "))
        for i in range (0, iterateAmount):
            myVirus = myVirus.replicate()
            newDNA = myVirus.getDNA()
            print(f"Replica [{i:3}] DNA sequence {newDNA}")

        print(f"Comparing latest {virusName} virus to the original {virusName}.")
        mutation, changes = find_mutation(originalDNA, newDNA)
        print(f"{originalDNA}\n{newDNA}\n{mutation}")
        if changes == 0:
            print("No mutations detected.")
        elif changes <= 5:
            print(f"{changes} mutations -- virus is the same.")
        elif changes > 5:
            print(f"{changes} mutations -- a *new* virus has been created.")

        yn = input("Try again [Y/N]? ").upper()

        if yn == "Y":
            pass
        else:
            break

def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
      main()
