list = []
length = 0
debugList = ["1", "2", "3", "4"]
run = 1
removeItem = 0
addItem = 0
debugLength = len(debugList)
while run:
    print("To-Do List - V1")
    print("    Options:\n")
    print("1) Add Item")
    print("2) Remove Item")
    print("3) View List")
    print("4) Clear List")
    print("5) Number of Items")
    print("6) Exit")
    #print("23) Debug Tools")
    options = input("Select Options: ")
    if options == "1":
        addItem = input("Add An Item: ")
        list.append(addItem)
        print(addItem + " Successfully Added!\n")
    if options == "2":
        removeItem = input("Remove An Item: ")
        list.remove(removeItem)
        print(removeItem + " Successfully Removed!\n")
    if options == "3":
        print(list)
        #print(list[0])
        #print(list[1])
        #print(list[2])
        #print(list[3])
        print("\nList Succesfully Printed!\n")
    if options == "4":
        list = []
        print("List Succesfully Cleared!\n")
    if options == "5":
        length = len(list)
        print("Items in list: " + length + "\n")
    if options == "6":
        run = 0
    if options == "23":
        print(debugList)