import random

health = 100
enemyHealth = 100
enemyFire = 0
enemyAir = 0
enemyEarth = 0
enemyIce = 0
element = input("Pick an element: 1 = Fire, 2 = Ice, 3 = Earth, 4 = Air? ")


# Elemental Enemies
print("Enemy found!")
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

# Loop Starting
while enemyHealth > 0:
    attack = input("Attacks: 1 = Fire, 2 = Ice, 3 = Earth, 4 = Air? ")
    attack = int(attack)
    dmg = random.randint(12,45)

# Attacks - Enemy and Friendly
    if attack == 1:
        print("Fireball! ")
    elif attack == 2:
        print("Frost Blast! ")
    elif attack == 3:
        print("Earth Throw! ")
    elif attack == 4:
        print("Sonic Boom! ")
    if enemyElement == attack:
        print("Little Damage!")
        enemyHealth = enemyHealth - (dmg - 12)
        print("Enemy Health: " + str(enemyHealth))
    elif enemyElement == 1 and attack == 2:
        print("EXTREME Damage!")
        enemyHealth = enemyHealth - (dmg + 25)
        print("Enemy Health: " + str(enemyHealth))
    elif enemyElement == 2 and attack == 1:
        print("EXTREME Damage!")
        enemyHealth = enemyHealth - (dmg + 25)
        print("Enemy Health: " + str(enemyHealth))
    else:
        enemyHealth = enemyHealth - dmg
        print("Enemy Health: " + str(enemyHealth))
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
    elif element == 1 and enemyAttack == 2:
        print("EXTREME Damage!")
        enemyHealth = enemyHealth - (dmg + 25)
        print("Health: " + str(enemyHealth))
    elif element == 2 and enemyAttack == 1:
        print("EXTREME Damage!")
        health = health - (dmg + 25)
        print("Health: " + str(health))
    else:
        health = health - dmg
        print("Health: " + str(health))


# Ending
if health > enemyHealth:
    print("You Win!")
    if frostChance == 10:
        print("MYTHICAL CAPTURED!!!")
elif health < enemyHealth:
    print("You Lose!")