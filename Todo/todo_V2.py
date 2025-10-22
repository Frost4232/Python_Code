list1 = []
length = 0
debugList = ["1", "2", "3", "4"]
version = "Command Line Version 1.1-TODO"
run = 1
user = "Admin"
console = 0
removeItem = 0
addItem = 0
name = "To-Do List - V2"
debugLength = len(debugList)
while run:
    print(name)
    print("    Options:\n")
    print("1) Add Item")
    print("2) Remove Item")
    print("3) View List")
    print("4) Clear List")
    print("5) Number of Items")
    print("6) Exit")
    print("7) Rename List")
    #print("console) Debug Tools")
    options = input("Select Options: ")
    if options == "1":
        addItem = input("Add An Item: ")
        list1.append(addItem)
        print(addItem + " Successfully Added!\n")
        print("--------------------------------------------------")
    if options == "2":
        removeItem = input("Remove An Item: ")
        list1.remove(removeItem)
        print(removeItem + " Successfully Removed!\n")
        print("--------------------------------------------------")
    if options == "3":
        print("List: \n")
        for word in list1:
            print(word)
        print("\nList Succesfully Printed!\n")
        print("--------------------------------------------------")
    if options == "4":
        list = []
        print("List Succesfully Cleared!\n")
        print("--------------------------------------------------")
    if options == "5":
        length = len(list1)
        print("Items in list: " + str(length) + "\n")
        print("--------------------------------------------------")
    if options == "6":
        run = 0
    if options == "7":
        name = input("Name Change: ")
        print("Successfully Changed Name To ", name + "\n")
        print("--------------------------------------------------")
    if options == "console":
        console = 1
        while console:
            console = input("C:/Users/" + user + "/DECRYPT/" + "CONSOLE>")
            if console == "debugList":
                print(debugList)
            elif console == "version":
                print(version)
            elif console == "exit":
                console = 0
            elif console == "hi":
                print("Hello!")
            elif console == "help":
                print("Commands: \ndebugList\nversion\nexit\nDEV\nend\nchangeUser\n")
            elif console == "DEV":
                print("Place Holder")
            elif console == "end":
                run = 0
                console = 0
            elif console == "changeUser":
                user = input("New User: ")
            else:
                print("<ERROR>")