Class = "assault"
ClassSelect = 1
WeaponSelection = 1
BotWeapons = []
WeaponCount = 0
SecondaryWeaponSelection = 1
MapSelection = 1
Bots = 999

while ClassSelect:
    print("What Class Would You Like To Be?\n")
    print("::::::Assault::::::")
    print("::::::Support::::::")
    print("::::::Engineer::::::")
    print("::::::Recon::::::\n")
    Class = input(">>> ")
    Class = Class.lower()
    if Class == "assault":
        print("Assault Class Selected!\n")
        ClassSelect = 0
        print("Perks:")
        print("        <Faster Sprint Speed>")
        print("        <Adrenaline Injector>")
        print("        <Better Assault Rifles>\n")
    elif Class == "support":
        print("Support Class Selected!\n")
        ClassSelect = 0
        print("Perks:")
        print("        <Better SMGs>")
        print("        <Defibrillator>")
        print("        <Ammo Crate>\n")
    elif Class == "engineer":
        print("Engineer Class Selected!\n")
        ClassSelect = 0
        print("Perks:")
        print("        <Better LMGs>")
        print("        <Repair Torch>")
        print("        <Reduced Explosion Damage>\n")
    elif Class == "recon":
        print("Recon Class Selected!\n")
        ClassSelect = 0
        print("Perks:")
        print("        <Better Snipers>")
        print("        <Trophy System>")
        print("        <Spawn Beacon>\n")
    #elif Class == "console":
        #print("Console Opening...\n")
        #while console:
    else:
        print("<ERROR>")



while WeaponSelection:
    print("What Weapon Would You Like To Have?\n")
    print("::::::HK416::::::")
    print("::::::MP5::::::")
    print("::::::M249::::::")
    print("::::::Barrett::::::\n")
    Weapon = input(">>> ")
    Weapon = Weapon.lower()
    if Weapon == "hk416":
        WeaponSelection = 0
        print("HK416 Weapon Selected!\n")
        print("v:")
        print("        <Full Auto>")
        print("        <Medium Damage>")
        print("        <Medium Ammo Count>\n")
    elif Weapon == "mp5":
        WeaponSelection = 0
        print("MP5 Weapon Selected!\n")
        print("Info:")
        print("        <Full Auto>")
        print("        <Low Damage>")
        print("        <Low Ammo Count>\n")
    elif Weapon == "m249":
        WeaponSelection = 0
        print("M249 Weapon Selected!\n")
        print("Info:")
        print("        <Full Auto>")
        print("        <Medium Damage>")
        print("        <High Ammo Count>\n")
    elif Weapon == "barrett":
        WeaponSelection = 0
        print("Barrett Weapon Selected!\n")
        print("Info:")
        print("        <Semi-Auto>")
        print("        <High Damage>")
        print("        <Low Ammo Count>\n")



while SecondaryWeaponSelection:
    print("What Weapon Would You Like To Have?\n")
    print("::::::M1911A1::::::")
    print("::::::G18::::::")
    print("::::::2011XC::::::")
    print("::::::P320::::::\n")
    SecondaryWeapon = input(">>> ")
    SecondaryWeapon = SecondaryWeapon.lower()
    if SecondaryWeapon == "m1911a1":
        SecondaryWeaponSelection = 0
        print("M1911A1 Weapon Selected!\n")
        print("info:")
        print("        <Semi-Auto>")
        print("        <High Damage>")
        print("        <Low Ammo Count>\n")
    elif SecondaryWeapon == "g18":
        SecondaryWeaponSelection = 0
        print("G18 Weapon Selected!\n")
        print("Info:")
        print("        <Full-Auto>")
        print("        <Low Damage>")
        print("        <High Ammo Count>\n")
    elif SecondaryWeapon == "2011xc":
        SecondaryWeaponSelection = 0
        print("2011XC Weapon Selected!\n")
        print("Info:")
        print("        <Semi-Auto>")
        print("        <High Damage>")
        print("        <Medium Ammo Count>\n")
    elif SecondaryWeapon == "p320":
        SecondaryWeaponSelection = 0
        print("P320 Weapon Selected!\n")
        print("Info:")
        print("        <Semi-Auto>")
        print("        <Medium Damage>")
        print("        <Medium Ammo Count>\n")



while MapSelection:
    print("What Map Would You Like To Play?\n")
    print("::::::Firestorm::::::")
    print("::::::Rust::::::")
    print("::::::Seige Of Shanghai::::::")
    print("::::::Shipment::::::\n")
    Map = input(">>> ")
    Map = Map.lower()
    if Map == "firestorm":
        MapSelection = 0
        print("Firestorm Selected!\n")
        print("Info:")
        print("        <Long Range>")
        print("        <Many Vehicles>")
        print("        <Conquest>\n")
    elif Map == "rust":
        MapSelection = 0
        print("Rust Selected!\n")
        print("Info:")
        print("        <Short Range>")
        print("        <No Vehicles>")
        print("        <TDM>\n")
    elif Map == "seige of shanghai":
        MapSelection = 0
        print("Seige Of Shanghai Selected!\n")
        print("Info:")
        print("        <Super Long Range>")
        print("        <Many Vehicles>")
        print("        <Conquest>\n")
    elif Map == "shipment":
        MapSelection = 0
        print("Shipment Selected!\n")
        print("Info:")
        print("        <Short Range>")
        print("        <No Vehicles>")
        print("        <TDM>\n")

#add 999 bots with their own weapons and classes. add vehicle selection.
#make battles simulated like oregon trail. EX: You Have Taken Charlie! #Victory
#the bots over threw the enemy





















