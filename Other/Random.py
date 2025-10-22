import math
import random

money = 500
print("You have "+ str(money) + "$")
bet = input("Bet? ")
bet = int(bet)
guess = input("Black or red? (b/r) ")
#r = 1, b = 0
color = random.randint(0,1)
if guess == "r":
    gcolor = 1
else:
    gcolor = 0
if gcolor == color:
    print("You win!")
    income = bet * 2
    money += income
else:
    print("You lose!")
    income = bet - (bet * 2)
    money += int(income)
print(money)