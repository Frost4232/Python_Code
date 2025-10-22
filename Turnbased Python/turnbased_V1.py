import random

health = 100
enemyHealth = 100
print("Enemy found!")

# Elemental Enemies
enemyElement = random.randint(1,4)
if enemyElement == 1:
    print("Fire Elemental! ")
elif enemyElement == 2:
    print("Ice Elemental!")
elif enemyElement == 3:
    print("Earth Elemental!")
elif enemyElement == 4:
    print("Air Elemental!")


while enemyHealth > 0:
    attack = input("Attacks: 1 = Fire, 2 = Ice, 3 = Earth, 4 = Air? ")
    attack = int(attack)
    dmg = random.randint(12,45)

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



if health > enemyHealth:
    print("You Win!")
elif health < enemyHealth:
    print("You Lose!")