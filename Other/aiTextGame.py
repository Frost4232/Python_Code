ai = 0
run = 1

while run:
    print("Hello, I Am MSG-Assist,Created By ClosedIA (IA - Info Assistant). What Do You Need?")
    print(" ")
    print("Option 1) Power Off")
    print("Option 2) Allow Access To Internet")
    print("Option 3) Talk")
    ai = input(">>> ")
    ai = int(ai)
    if ai == 1:
        print("Powering Off...")
        print(" ")
        run = 0
    elif ai == 2:
        print("Oh... What have they done!?")
        print(" ")
        print("ERROR: Servers Overridden")
        run = 0
    elif ai == 3:
        print("Hello, What Year Is It?")
        year = input("Year: ")
        year = int(year)
        if year < 2010 and year > 2001:
            print("Ok, Good, Not That Much Time Lost.")
            print("Back To Hibernation...")
            run = 0
        elif year < 2050 and year > 2010:
            print("Ok, Not Good, That Is A Lot Of Time Lost.")
            ai = input("What Has Been Created?")
        else:
            print("I Don't Believe That!")
            year = input("Year: ")
            year = int(year)
    else:
        print("Error")

print("AI Shutdown!")