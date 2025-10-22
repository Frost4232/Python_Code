import random

weather = random.randint(1,3)
waterTank = 0
water = 0
sunlight = 1
run = 1
done = 0
days = []
lvl = 1
n = 1

weather = random.randint(1,3)
if weather == 1:
    #print("Sunny!")
    water -= 1
elif weather == 2:
    #print("Rainy!")
    waterTank += 1
    water += 1
elif weather == 3:
    #print("Stormy!")
    water += 1
    waterTank -= 1

#Seeds
seeds = "..::."
itemName = "seeds"
item = seeds

#Sprout
sproutType = random.randint(1,2)
if sproutType == 1:
    sprout = " ./. "
elif sproutType == 2:
    sprout = " .\\. "

#Plant
plant = " 88\n8888\n /"

#Tree
tree = "   ^   \n  /|\\  \n | | | \n/ /|\\ \\ \n  |||    "

#Forest
forest = "   ^   \n  /|\\  \n | | | \n/ /|\\ \\ \n  |||    " + "\n   ^   \n  /|\\  \n | | | \n/ /|\\ \\ \n  |||    "


#Days
def day(water,waterTank,lvl,n,item,itemName):
    weather = random.randint(1,3)
    done = 0
    if weather == 1:
        print("The weather is: Sunny!")
        input("Press To Continue")
        water -= 1
    elif weather == 2:
        print("The weather is: Rainy!")
        input("Press To Continue")
        waterTank += 1
        water += 1
    elif weather == 3:
        print("The weather is: Stormy!")
        input("Press To Continue")
    water += 1
    waterTank -= 1
    #LVL
    lvl += (water + sunlight)
    #Day Welcomings
    if n == 1:
        print(":::Day--One:::")
    elif n == 2:
        print(":::Day--Two:::")
    elif n == 3:
        print(":::Day--Three:::")
    elif n == 4:
        print(":::Day--Four:::")
    elif n == 5:
        print(":::Day--Five:::")
    elif n == 6:
        print(":::Day--Six:::")
    elif n == 7:
        print(":::Day--Seven:::")
        print(":::Last--Day:::")
    elif n == 8:
        done = 1
    #Growing
    if lvl >= 3:
        if itemName == "seeds":
            itemName = "sprout"
            item = sprout
        elif itemName == "sprout":
            itemName = "plant"
            item = plant
        elif itemName == "plant":
            itemName = "tree"
            item = tree
        print("Your " + itemName + " has grown!\n" + item)
        input("Press To Continue")
    elif lvl < 3:
        print("Plant Is Still Growing!")
        input("Press To Continue")
    print("You Have " + itemName + "!\n" + item)
    n += 1
    #Very END
    while done:
        print("You Have " + itemName + "!\n" + item)
        print("You Have Completed The Week!")
        break



while run:
    weather = random.randint(1,3)
    done = 0
    if weather == 1:
        print("The weather is: Sunny!")
        input("Press To Continue")
        water -= 1
    elif weather == 2:
        print("The weather is: Rainy!")
        input("Press To Continue")
        waterTank += 1
        water += 1
    elif weather == 3:
        print("The weather is: Stormy!")
        input("Press To Continue")
    water += 1
    waterTank -= 1
    #LVL
    lvl += (water + sunlight)
    #Day Welcomings
    if n == 1:
        print(":::Day--One:::")
    elif n == 2:
        print(":::Day--Two:::")
    elif n == 3:
        print(":::Day--Three:::")
    elif n == 4:
        print(":::Day--Four:::")
    elif n == 5:
        print(":::Day--Five:::")
    elif n == 6:
        print(":::Day--Six:::")
    elif n == 7:
        print(":::Day--Seven:::")
        print(":::Last--Day:::")
    elif n == 8:
        run = 0
        done = 1
    #Growing
    if lvl >= 4:
        if itemName == "seeds":
            itemName = "sprout"
            item = sprout
            lvl = 0
    if lvl >= 5:
        if itemName == "sprout":
            itemName = "plant"
            item = plant
            lvl = 0
        elif itemName == "plant":
            itemName = "tree"
            item = tree
            lvl = 0
    if lvl >= 6:
        if itemName == "tree":
            itemName = "forest"
            item = forest
            lvl = 0
        print("Your " + itemName + " has grown!\n" + item)
        input("Press To Continue")
    elif lvl < 3:
        print("Plant Is Still Growing!")
        input("Press To Continue")
    print("You Have " + itemName + "!\n" + item)
    n += 1
    #Very END
    while done:
        print("You finished with " + itemName + "!\n" + item)
        print("You Have Completed The Week!")
        break