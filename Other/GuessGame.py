import random

Guess = 0
GuessesLeft = 10
GuessVersion = "Command Line Version 1.1-GUESS"
user = "Admin"
SecretNum = random.randint(1,100)
RangeNumOne = input("Insert Number One: ")
RangeNumTwo = input("Insert Number Two: ")
RangeNumOne = int(RangeNumOne)
RangeNumTwo = int(RangeNumTwo)
SecretNum = random.randint(RangeNumOne,RangeNumTwo)
print("The Range Is " + str(RangeNumOne) + "-" + str(RangeNumTwo))

while Guess != SecretNum and GuessesLeft > 0:
    Guess = input("Insert A Number: ")
    Guess = int(Guess)
    if Guess > SecretNum:
        print("Wrong")
        print("Guess Lower")
    if Guess < SecretNum:
        print("Wrong")
        print("Guess Higher")
    GuessesLeft -= 1
    print("Guesses Left: " + str(GuessesLeft))
    print(" ")
    if Guess == "console":
        console = 1
        while console:
            console = input("C:/Users/" + user + "/DECRYPT/" + "CONSOLE>")
            if console == "secretNum":
                print(SecretNum)
            elif console == "version":
                print(GuessVersion)
            elif console == "exit":
                console = 0
            elif console == "hi":
                print("Hello!")
            elif console == "help":
                print("Commands: \nsecretNum\nversion\nexit\nDEV\nend\nchangeUser\n")
            elif console == "DEV":
                print("Place Holder")
            elif console == "end":
                Guess = SecretNum
                console = 0
            elif console == "changeUser":
                user = input("New User: ")
            else:
                print("<ERROR>")

if GuessesLeft > 0 and Guess == SecretNum:
    print("Correct!")

if GuessesLeft < 0:
    print("Out Of Guesses! Game Over!")
    print(" ")
print("The Secret Number Was " + str(SecretNum) + "!")