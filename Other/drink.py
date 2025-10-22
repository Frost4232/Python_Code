money = 25.00
id = 0
drinkCount = 0
adultDrinkCount = 0
done = 0
juiceCount= 0

age = int(input("What is your age? "))

if age <= 10:
    print("Not the right place for you.")
    done = 1

if age >= 80 and age <= 104:
    print("You shouldn't be drinking!")
    done = 1

if age >= 105:
    print("Get out...")
    done = 1

if age >= 21 and age <= 79:
    print("You can buy drinks! ")
    id = 1

while done == 0 and money >= 0:
    drink = input("What drink do you want?: Beer, Alcohol, Water... ")
    drink = drink.lower()

    if drink in {"water", "milk", "juice"}:
        if drink == "water":
            money -= 1.00
        elif drink == "milk":
            money -= 1.50
        elif drink == "juice":
            money -= 1.50
            juiceCount += 1
        drinkCount += 1
        print("Purchase Successful")
        print("Money: " + str(money))

    elif drink.lower() in {"alcohol", "beer", "whiskey"}:
        if id:
            money -= 2.50
            adultDrinkCount += 1
            print("Purchase Successful")
            print("Money: " + str(money))
        else:
            print("Not Old Enough!")

    elif drink.lower() == "done":
        done = 1
    else:
        print("We don't have it.")
print("Remaining Money: " + str(money))
print("Drinks Bought: " + str(drinkCount))
print("Adult Drinks Bought: " + str(adultDrinkCount))