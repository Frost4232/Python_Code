import random

health = 100
enemyHealth = 100
enemyFire = 0
enemyAir = 0
enemyEarth = 0
enemyIce = 0
frostChance = 0
boulderChance = 0
attackType = 0
attack = 0
element = input("Pick an element: 1 = Fire Based, 2 = Ice Based, 3 = Earth Based, 4 = Air Based? ")
print(" ")
element = int(element)

# Elemental Enemies
print("Enemy found!")
print(" ")
enemyElement = random.randint(1,4)
if enemyElement == 1:
    print("Fire Enemy Type! ")
    enemyFire = random.randint(1,4)
elif enemyElement == 2:
    print("Ice Enemy Type!")
    enemyIce = random.randint(1,4)
    frostChance = random.randint(1,10)
    if frostChance == 10:
        enemyIce = 5
elif enemyElement == 3:
    print("Earth Enemy Type!")
    enemyEarth = random.randint(1,4)
    boulderChance = random.randint(1,10)
    if boulderChance == 10:
        enemyEarth = 5
elif enemyElement == 4:
    print("Air Enemy Type!")
    enemyAir = random.randint(1,4)

# Enemy Names
if enemyAir == 1:
    print("Cloudy Appeared!")
elif enemyAir == 2:
    print("Windy Appeared!")
elif enemyAir == 3:
    print("Airud Appeared!")
elif enemyAir == 4:
    print("Atmos Appeared!")

if enemyFire == 1:
    print("Firestorm Appeared!")
elif enemyFire == 2:
    print("Magmus Appeared!")
elif enemyFire == 3:
    print("Lavus Appeared!")
elif enemyFire == 4:
    print("Hellstorm Appeared!")

if enemyEarth == 1:
    print("Rocky Appeared!")
elif enemyEarth == 2:
    print("Stony Appeared!")
elif enemyEarth == 3:
    print("Earthguy Appeared!")
elif enemyEarth == 4:
    print("Grassy Appeared!")
elif enemyEarth == 5:
    print("The Boulder Appeared! MYTHICAL!!!")
    enemyHealth = 200

if enemyIce == 1:
    print("Icer Appeared!")
elif enemyIce == 2:
    print("Icicler Appeared!")
elif enemyIce == 3:
    print("Frozening Appeared!")
elif enemyIce == 4:
    print("Snowy Appeared!")
elif enemyIce == 5:
    print("Frost4232 Appeared! MYTHICAL!!!")
    enemyHealth = 200
print(" ")

# Loop Starting
while enemyHealth > 0:
    if element == 1:
        attackType = 1
    if element == 2:
        attackType = 2
    if element == 3:
        attackType = 3
    if element == 4:
        attackType = 4


    #attack = input("Attacks: 1 = Fire, 2 = Ice, 3 = Earth, 4 = Air? ")
    dmg = random.randint(12,45)

# Attacks - Enemy and Friendly
    if attackType == 1:
        print("Fire Attacks! ")
        attack = input("Attacks: 1 = Fireball, 2 = Volcanic Eruption, 3 = Helldiver, 4 = Heat Wave? ")
        attack = int(attack)
        if attack == 1:
            print("Fireball! ")
        elif attack == 2:
            print("Volcanic Eruption! ")
        elif attack == 3:
            print("Helldiver! ")
        elif attack == 4:
            print("Heatwave! ")

    elif attackType == 2:
        print("Ice Attacks! ")
        attack = input("Attacks: 1 = Snow Throw, 2 = Frost Blast, 3 = Ice Slice, 4 = Chilly? ")
        attack = int(attack)
        if attack == 1:
            print("Snow Throw! ")
        elif attack == 2:
            print("Frost Blast! ")
        elif attack == 3:
            print("Ice Slice! ")
        elif attack == 4:
            print("Chilly! ")

    elif attackType == 3:
        print("Earth Attacks! ")
        attack = input("Attacks: 1 = Tectonic Throw, 2 = Ground Slam, 3 = Earth Throw, 4 = Earthquake? ")
        attack = int(attack)
        if attack == 1:
            print("Tectonic Throw! ")
        elif attack == 2:
            print("Ground Slam! ")
        elif attack == 3:
            print("Earth Throw! ")
        elif attack == 4:
            print("Earthquake! ")

    elif attackType == 4:
        print("Air Attacks! ")
        attack = input("Attacks: 1 = Wind(ow) Throw, 2 = Tornado, 3 = Air Slice, 4 = Sonic Boom? ")
        attack = int(attack)
        if attack == 1:
            print("Wind(ow) Throw! ")
        elif attack == 2:
            print("Tornado! ")
        elif attack == 3:
            print("Air Slice! ")
        elif attack == 4:
            print("Sonic Boom! ")

    attack = int(attack)


    if enemyElement == attackType:
        print("Little Damage!")
        enemyHealth = enemyHealth - (dmg - 12)
        print("Enemy Health: " + str(enemyHealth))
        print(" ")
    elif enemyElement == 1 and attackType == 2:
        print("EXTREME Damage!")
        enemyHealth = enemyHealth - (dmg + 25)
        print("Enemy Health: " + str(enemyHealth))
        print(" ")
    elif enemyElement == 2 and attackType == 1:
        print("EXTREME Damage!")
        enemyHealth = enemyHealth - (dmg + 25)
        print("Enemy Health: " + str(enemyHealth))
        print(" ")
    else:
        enemyHealth = enemyHealth - dmg
        print("Enemy Health: " + str(enemyHealth))
        print(" ")

#--------------Needs Fixing------------------------
    enemyAttack = random.randint(1,4)
    dmg = random.randint(12,45)

    if enemyAttack == 1:
        print("Fireball! ")
    elif enemyAttack == 2:
        print("Frost Blast! ")
    elif enemyAttack == 3:
        print("Earth Throw! ")
    elif enemyAttack == 4:
        print("Sonic Boom! ")
    if element == enemyAttack:
        print("Little Damage!")
        health = health - (dmg - 12)
        print("Health: " + str(health))
        print(" ")
    elif element == 1 and enemyAttack == 2:
        print("EXTREME Damage!")
        enemyHealth = enemyHealth - (dmg + 25)
        print("Health: " + str(health))
        print(" ")
    elif element == 2 and enemyAttack == 1:
        print("EXTREME Damage!")
        health = health - (dmg + 25)
        print("Health: " + str(health))
        print(" ")
    else:
        health = health - dmg
        print("Health: " + str(health))
        print(" ")


# Ending
if health > enemyHealth or enemyHealth == 0:
    print("You Win!")
    if frostChance == 10:
        print("MYTHICAL CAPTURED!!!")
elif health < enemyHealth or health == 0:
    print("You Lose!")