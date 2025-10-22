table = 1
atomic = 0
proton = 0
mass = 0
electron = 0
neutron = 0
symbol = "N/a"

atomicDisp = 0
protonDisp = 0
massDisp = 0
electronDisp = 0
neutronDisp = 0
symbolDisp = "N/a"

atomicEx = 1
protonEx = 1
massEx = 1.0078
electronEx = 1
neutronEx = 0
symbolEx = "H"


while table:
    print("\nWhat Informatioon Do You Have?")
    print("1) Proton")
    print("2) Neutron")
    print("3) Electron")
    #print("4) Symbol")
    print("5) Mass")
    print("6) Atomic #")
    print("7) Clear")
    choice = input(">>> ")
    choice = choice.lower()
    if choice == "1" or choice == "proton":
        proton = input("What is the amount of protons? ")
        atomic = proton
    elif choice == "2" or choice == "neutron":
        print("WIP")
    elif choice == "3" or choice == "electron":
        print("WIP")
    elif choice == "4" or choice == "symbol":
        print("WIP")
    elif choice == "5" or choice == "mass":
        print("WIP")
    elif choice == "6" or choice == "atomic":
        proton = atomic
    elif choice == "7" or choice == "clear":
        atomic = 0
        proton = 0
        mass = 0
        electron = 0
        neutron = 0
        symbol = "N/a"


    #Displays
    if atomic == 0:
        atomicDisp = "N/a"
    else:
        atomicDisp = atomic
    if proton == 0:
        protonDisp = "N/a"
    else:
        protonDisp = proton
    if mass == 0:
        massDisp = "N/a"
    else:
        massDisp = mass
    if electron == 0:
        electronDisp = "N/a"
    else:
        electronDisp = electron
    if neutron == 0:
        neutronDisp = "N/a"
    else:
        neutronDisp = neutron
    #if symbol == "N/a":
        #symbolDisp = "N/a"
    #else:
        #symbolDisp == symbol

    #Displaying Infromation
    print("Info: ")
    print("Atomic Number: " + str(atomic))
    print("Protons: " + str(proton))
    print("Atomic Mass: " + str(mass))
    print("Electrons: " + str(electron))
    print("Neutrons: " + str(neutron))
    #print("Symbol: " + symbol)















