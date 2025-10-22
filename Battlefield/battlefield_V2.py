import random
Class = "assault"
ClassSelect = 1
WeaponSelection = 1
BotSelection = 1
SecondaryWeaponSelection = 1
MapSelection = 1
CharlieCount = 0
Battle = 1
Bots = 999
FactionChance = random.randint(1,2)
faction = "<ERROR>"
Objectives = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
RUPoints = 0
USAPoints = 0
XP = random.randint(156,405)
CaptureChance = random.randint(1,3)
VehicleSelection = 1



#Faction
if FactionChance == 1:
    print("You are in the US army!")
    faction = "us"
else:
    print("You are in the Russian army!")
    faction = "russia"



#Class Selection
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



#Weapon Selection
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
        print("Info:")
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



#Secondary Weapon Selection
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



#Map Selection
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
        VehicleMap = 1
        print("Firestorm Selected!\n")
        print("Info:")
        print("        <Long Range>")
        print("        <Many Vehicles>")
        print("        <Conquest>\n")
    elif Map == "rust":
        MapSelection = 0
        VehicleSelection = 0
        print("Rust Selected!\n")
        print("Info:")
        print("        <Short Range>")
        print("        <No Vehicles>")
        print("        <TDM>\n")
    elif Map == "seige of shanghai":
        MapSelection = 0
        VehicleMap = 1
        print("Seige Of Shanghai Selected!\n")
        print("Info:")
        print("        <Super Long Range>")
        print("        <Many Vehicles>")
        print("        <Conquest>\n")
    elif Map == "shipment":
        VehicleSelection = 0
        MapSelection = 0
        print("Shipment Selected!\n")
        print("Info:")
        print("        <Short Range>")
        print("        <No Vehicles>")
        print("        <TDM>\n")



#Vehicle Selection
while VehicleSelection:
    print("What Vehicle Would You Like To Use?\n")
    print("::::::A-10::::::")
    print("::::::Tank::::::")
    print("::::::Light AA::::::")
    print("::::::Apache::::::\n")
    Vehicle = input(">>> ")
    Vehicle = Vehicle.lower()
    if Vehicle == "a-10":
        VehicleSelection = 0
        print("A-10 Selected!\n")
        print("Info:")
        print("        <Air Transport>")
        print("        <Heavily Armored>")
        print("        <30mm Shells [BRRR]>\n")
    elif Vehicle == "tank":
        VehicleSelection = 0
        print("Tank Selected!\n")
        print("Info:")
        print("        <SGround Transport>")
        print("        <Heavily Armored>")
        print("        <120mm Shells>\n")
    elif Vehicle == "light aa":
        VehicleSelection = 0
        print("Light AA Selected!\n")
        print("Info:")
        print("        <Ground Transport>")
        print("        <Lightly Armored>")
        print("        <40mm Shells>\n")
    elif Vehicle == "apache":
        VehicleSelection = 0
        print("Apache Selected!\n")
        print("Info:")
        print("        <SAir Transport>")
        print("        <Medium Armored>")
        print("        <30mm Shells>\n")



#Bots
while BotSelection:
    print("How many bots would you like?\n")
    print("::::::100::::::")
    print("::::::250::::::")
    print("::::::500::::::")
    print("::::::1000::::::\n")
    BotCount = input(">>> ")
    if BotCount == "100":
        print("100 Bots Selected!")
        print("Info:")
        print("        <Super Short Time Limit>")
        BotSelection = 0
    elif BotCount == "250":
        print("250 Bots Selected!")
        print("Info:")
        print("        <Short Time Limit>")
        BotSelection = 0
    elif BotCount == "500":
        print("500 Bots Selected!")
        print("Info:")
        print("        <Medium Time Limit>")
        BotSelection = 0
    elif BotCount == "1000":
        print("1000 Bots Selected!")
        print("Info:")
        print("        <Long Time Limit>")
        BotSelection = 0




AlphaController = "Nobody"
BravoController = "Nobody"
CharlieController = "Nobody"
DeltaController = "Nobody"
EchoController = "Nobody"
FoxtrotController = "Nobody"


AlphaInfo = "Alpha is controlled by: " + AlphaController
BravoInfo = "Bravo is controlled by: " + BravoController
CharlieInfo = "Charlie is controlled by: " + CharlieController
DeltaInfo = "Delta is controlled by: " + DeltaController
EchoInfo = "Echo is controlled by: " + EchoController
FoxtrotInfo = "Foxtrot is controlled by: " + FoxtrotController


#The Battle
HalvedScore = (int(BotCount)/2)
while Battle:
    if USAPoints >= int(BotCount):
        print("USA Wins!!!")
        print(str(XP) + "XP Gained!")
        Battle = 0
    elif RUPoints >= int(BotCount):
        print("RU Wins!!!")
        print(str(XP) + "XP Gained!")
        Battle = 0

    Objective = random.choice(Objectives)
    CaptureChance = random.randint(1,3)

    if CharlieCount >= 10 and Map == "seige of shanghai":
        print("Charlie Has Callapsed!\n")
        CharlieCount = -100
    if RUPoints >= HalvedScore and VehicleMap == 1:
        print("US Lost Their " + Vehicle)
        HalvedScore = 10000
        USAPoints -= 100
    elif USAPoints >= HalvedScore and VehicleMap == 1:
        print("RU Lost Their " + Vehicle)
        HalvedScore = 10000
        RUPoints -= 100
    if Objective == "Alpha":
        if CaptureChance == 1:
            AlphaController = "US"
            USAPoints += 10
        elif CaptureChance == 2:
            AlphaController = "Nobody"
        elif CaptureChance == 3:
            AlphaController = "RU"
            RUPoints += 10


    elif Objective == "Bravo":
        if CaptureChance == 1:
            BravoController = "US"
            USAPoints += 10
        elif CaptureChance == 2:
            BravoController = "Nobody"
        elif CaptureChance == 3:
            BravoController = "RU"
            RUPoints += 10


    elif Objective == "Charlie":
        if CaptureChance == 1:
            CharlieController = "US"
            USAPoints += 10
        elif CaptureChance == 2:
            CharlieController = "Nobody"
        elif CaptureChance == 3:
            CharlieController = "RU"
            RUPoints += 10
        CharlieCount += 1


    elif Objective == "Delta":
        if CaptureChance == 1:
            DeltaController = "US"
            USAPoints += 10
        elif CaptureChance == 2:
            DeltaController = "Nobody"
        elif CaptureChance == 3:
            DeltaController = "RU"
            RUPoints += 10


    elif Objective == "Echo":
        if CaptureChance == 1:
            EchoController = "US"
            USAPoints += 10
        elif CaptureChance == 2:
            EchoController = "Nobody"
        elif CaptureChance == 3:
            EchoController = "RU"
            RUPoints += 10


    elif Objective == "Foxtrot":
        if CaptureChance == 1:
            FoxtrotController = "US"
            USAPoints += 10
        elif CaptureChance == 2:
            FoxtrotController = "Nobody"
        elif CaptureChance == 3:
            FoxtrotController = "RU"
            RUPoints += 10


    AlphaInfo = "Alpha is controlled by the " + AlphaController
    BravoInfo = "Bravo is controlled by the " + BravoController
    CharlieInfo = "Charlie is controlled by the " + CharlieController
    DeltaInfo = "Delta is controlled by the " + DeltaController
    EchoInfo = "Echo is controlled by the " + EchoController
    FoxtrotInfo = "Foxtrot is controlled by the " + FoxtrotController


    print(AlphaInfo)
    print(BravoInfo)
    print(CharlieInfo)
    print(DeltaInfo)
    print(EchoInfo)
    print(FoxtrotInfo)
    print("RU Points: " + str(RUPoints))
    print("USA Points: " + str(USAPoints))
    print("Points To Win: " + str(BotCount))

    input("\n:::Continue:::")














    #Make Gun, classes, maps, and vehicles affect the gameplay