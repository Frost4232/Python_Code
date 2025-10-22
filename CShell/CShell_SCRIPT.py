import random
run = 0
PCHP = 10

#------------------------------Login--------------------------------------------
userList = ["frost4232", "guest","Thecoolman3000", "Luretex", "007man", "DirtLord3817", "Jellybean"]
pswd = "1234"
superPSWD = "71613"
unlogged = 1
user = "guest"
creating = 1
nameLog = "na"
createNew = "na"
age = 12
ageLog = 0
emailLog = "na"
email = "error@gmail.com"
userLog = "error"
name = "guest"
#-------------------------------------------------------------------------------

console = 0
GB1 = random.randint(12,300)
GB2 = random.randint(12,300)
GB3 = random.randint(12,300)
GB4 = random.randint(12,300)
GB11 = random.randint(12,300)
GB22 = random.randint(12,300)
GB33 = random.randint(12,300)
GB44 = random.randint(12,300)
GB55 = random.randint(12,300)
GB66 = random.randint(12,300)
GB77 = random.randint(12,300)
GB88 = random.randint(12,300)
version = "CadmiumShell Version 1.5"
listVersion = "Version Five CSE"
Guess = 0
GuessesLeft = 10
GuessVersion = "Version 1.3 GUESS-CSE "
SecretNum = random.randint(1,100)
system = "videoPC"
directory = "root"
safemode = 0
DEVM = 0
win = 0
crypto = 0
lrun = 1
list1 = []
length = 0
debugList = ["1", "2", "3", "4"]
removeItem = 0
addItem = 0
Lname = "To-Do List - V2"
debugLength = len(debugList)
MAINconsole = 1

#Folders
folders = ["crypto", "photos", "videos", "games", "extra", "other", "admin", "user", "hard drive"]
selected_folders = random.sample(folders, 3)
folderSelection1 = selected_folders[0]
folderSelection2 = selected_folders[1]
folderSelection3 = selected_folders[2]
cdOptions = [folderSelection1, folderSelection2, folderSelection3]

#Errors
error1 = random.randint(1,3)
error2 = random.randint(1,3)
error3 = random.randint(1,3)
error4 = random.randint(1,3)
error5 = random.randint(1,3)

#dmg
dmg1 = random.randint(1,3)
dmg2 = random.randint(1,3)
dmg3 = random.randint(1,3)
dmg4 = random.randint(1,3)
dmg5 = random.randint(1,3)

#Items/Folder
twodnum = random.randint(10,99)
threednum = random.randint(100,999)
pTypeList = [".png", ".jpg"]
pType = random.choice(pTypeList)
items = ["crypto", "photo" + str(twodnum) + pType, "video" + str(threednum) + ".mp4", "notes.txt", "audio.mp3", "steam.exe", "clash_vid.mp4", "music.mp3", "game.8xp", "battlefield.exe", "google.exe", "terminal.py", "login.py", "drink.py", "Zoom.mp3", "google-classroom.exe", "specs.txt", "discord.exe"]
selected_items = random.sample(items, 16)
itemSelection1 = selected_items[1]
itemSelection2 = selected_items[2]
itemSelection3 = selected_items[3]
itemSelection4 = selected_items[4]
itemSelection5 = selected_items[5]
itemSelection6 = selected_items[6]
itemSelection7 = selected_items[7]
itemSelection8 = selected_items[8]
itemSelection9 = selected_items[9]
itemSelection10 = selected_items[10]
itemSelection11 = selected_items[11]
itemSelection12 = selected_items[12]
itemSelection13 = selected_items[13]
itemSelection14 = selected_items[14]
itemSelection15 = selected_items[15]
folderItems1 = [itemSelection1, itemSelection2, itemSelection3, itemSelection4, itemSelection5]
folderItems2 = [itemSelection6, itemSelection7, itemSelection8, itemSelection9, itemSelection10]
folderItems3 = [itemSelection11, itemSelection12, itemSelection13, itemSelection14, itemSelection15]
cdItemsOptionsList = ["cd crypto", "cd photo" + str(twodnum) + pType, "cd video" + str(threednum) + ".mp4", "cd notes.txt", "cd audio.mp3", "cd steam.exe", "cd clash_vid.mp4", "cd music.mp3", "cd game.8xp", "cd battlefield.exe", "cd google.exe", "cd terminal.py", "cd login.py", "cd drink.py", "cd zoom.mp3", "cd google-classroom.exe", "cd specs.txt", "cd discord.exe"]
itemCdOptions1 = [itemSelection1, itemSelection2, itemSelection3, itemSelection4, itemSelection5]
itemCdOptions2 = [itemSelection6, itemSelection7, itemSelection8, itemSelection9, itemSelection10]
itemCdOptions3 = [itemSelection11, itemSelection12, itemSelection13, itemSelection14, itemSelection15]

from builtins import input

while unlogged:
    print("To Proceed To Cadmium Shell, type \"help\" for users, Please Log In: \n")
    userLog = input("Login: ")
    if userLog == "help":
        print(":::User:::List:::")
        for userL in userList:
            print(f"User: {userL}")
        print(" ")
    elif userLog in userList:
        if userLog == "frost4232":
            pswd = "2319"
            nameLog = "Snow"
            ageLog = 14
            emailLog = "frost4232.1@gmail.com"
        elif userLog == "Luretex":
            pswd = "ghostmatt2010"
            emailLog = "ghostmatt2010@gmail.com"
            ageLog = 14
            nameLog = "Matthew lovell"
        elif userLog == "Thecoolman3000":
            ageLog = 14
            nameLog = "Austin Bonilla"
            emailLog = "thecoolman3000@gmail.com"
            pswd = "thisprogramneedsahero"
        elif userLog == "007man":
            ageLog = 14
            nameLog = "O`Ryan Riggs"
            emailLog = "youmom@gmail.com"
            pswd = "tinpen123"
        elif userLog == "DirtLord3817":
            ageLog = 15
            nameLog = "Rainelle Ruiz"
            emailLog = "DirtLord3817@gmail.com"
            pswd = "Ikickbabies1779"
        elif userLog == "Jellybean":
            ageLog = 12
            nameLog = "Cylas Farmer"
            emailLog = "Jellybean57@gmail.com"
            pswd = "314159"
        elif userLog == "guest":
            user = "guest"
            print("Skip Password")
            unlogged = 0
        pswdLog = input("Password: ")
        pswdLog = pswdLog.lower()
        if pswdLog == pswd or pswdLog == superPSWD:
            print("Logged In!")
            user = userLog
            age = ageLog
            email = emailLog
            name = nameLog
            unlogged = 0
        else:
            print("Incorrect Password, Try Again.")
    else:
        print("User Not Found")
        createNew = str(input("Would You Like To Make A Temporary Account? ")).lower()
        if createNew == "yes":
            createNew = " "
            while creating:
                userLog = input("Username: ")
                ageLog = input("Age: ")
                emailLog = input("Email: ")
                nameLog = input("Name: ")
                print("Does this information look correct?")
                print("Age: " + str(ageLog))
                print("Email: " + str(emailLog))
                print("Name: " + str(nameLog))
                print("User: " + str(userLog))
                infoCorrect = input(">>> ")
                infoCorrect = infoCorrect.lower()
                if infoCorrect == "yes":
                    user = userLog
                    age = ageLog
                    email = emailLog
                    name = nameLog
                    creating = 0
                    unlogged = 0
                elif infoCorrect == "no":
                    print("Returning...")
                else:
                    print("<ERROR>")
        elif createNew == "no":
            print("Back To Login Process...")
if unlogged == 0:
    print("Terminal Starting... \n")
    run = 1
else:
    print("<ERROR>")

if run:
    print("Chromindium - Cobalt Co [Version 9.17.2025]")
    print("Copyright (c) 2025 Chromindium Corporation. All rights reserved.")
    print("Type \"help\" For The Commands\n")


while run and PCHP > 0:

    if DEVM == 1:
        print("--DEV MODE ENABLED--")
    commandInput = input("C:/Users/" + user + "> ")
    print(" ")

#--------------------------HELP-------------------------------------------------
    if commandInput == "help":
        print("Command Display: \n")
        print("cd - Used to move into a directory and open it.\n")
        print("move - Used to move to a different system\n")
        print("systeminfo - Used to view information about PC\n")
        print("exit - Used to leave the command line.\n")
        print("chck - Checks the current system for errors.\n")
        print("safe - Boots into safemode which stops most errors.\n")
        print("direct - Shows the availible directories to cd into.\n")
        print("list - Opens the built in list app.\n")
        print("version - Shows the command line version.\n")
        print("drive options - Shows the availible drives to cd into.\n")
        print("virus - Downloads a virus...\n")
        print("games - Shows a list of games built into CS.\n")

#---------------------DIRECTORIES-----------------------------------------------
    elif commandInput == "direct":
        print("curseforge - " + str(GB1) + "GB")
        print("app_data - " + str(GB2) + "GB")
        print("root - " + str(GB3) + "GB")
        print("twodrove - " + str(GB4) + "GB")
#---------------------GAMES-----------------------------------------------------
    elif commandInput == "games":
        print("guess - Plays the built in guessing game.\n")
        print("cd ssd - If you cd ssd it plays a minigame.\n")
#---------------------MAKE VIRUS------------------------------------------------
    elif commandInput == "virus":
        print("VIRUS FOUND - USE \"chck\" COMMAND TO REMOVE!")
        if system == "videoPC":
            error1 = 1
        elif system == "bpaPC":
            error2 = 1
        elif system == "customPC":
            error3 = 1
        elif system == "codingPC":
            error4 = 1

#---------------------CHCK VIRUS------------------------------------------------
    elif commandInput == "chck":
        if system == "videoPC":
            if error1 != 1:
                print("PC Clean!")
            elif error1 == 1:
                print("ERROR FOUND!!!")
                if dmg1 == 2:
                    if safemode:
                        PCHP -=3
                        print("66% Currupted")
                    else:
                        PCHP -= 5
                        print("50% CURRUPTED")
                else:
                    print("SAFE")
                if safemode:
                    print("3 Crypto Collected")
                    crypto += 3
                else:
                    print("5 Crypto Collected")
                    crypto += 5

        elif system == "bpaPC":
            if error2 != 1:
                print("PC Clean!")
            elif error2 == 1:
                print("ERROR FOUND!!!")
                if dmg2 == 2:
                    if safemode:
                        PCHP -=3
                        print("66% Currupted")
                    else:
                        PCHP -= 5
                        print("50% CURRUPTED")
                else:
                    print("SAFE")
                if safemode:
                    print("3 Crypto Collected")
                    crypto += 3
                else:
                    print("5 Crypto Collected")
                    crypto += 5

        elif system == "customPC":
            if error3 != 1:
                print("PC Clean!")
            elif error3 == 1:
                print("ERROR FOUND!!!")
                if dmg3 == 2:
                    if safemode:
                        PCHP -=3
                        print("66% Currupted")
                    else:
                        PCHP -= 5
                        print("50% CURRUPTED")
                else:
                    print("SAFE")
                if safemode:
                    print("3 Crypto Collected")
                    crypto += 3
                else:
                    print("5 Crypto Collected")
                    crypto += 5

        elif system == "codingPC":
            if error4 != 1:
                print("PC Clean!")
            elif error4 == 1:
                print("ERROR FOUND!!!")
                if dmg4 == 2:
                    if safemode:
                        PCHP -=3
                        print("66% Currupted")
                    else:
                        PCHP -= 5
                        print("50% CURRUPTED")
                else:
                    print("SAFE")
                if safemode:
                    print("3 Crypto Collected")
                    crypto += 3
                else:
                    print("5 Crypto Collected")
                    crypto += 5
        elif system == "macroPC":
            if error5 != 1:
                print("PC Clean!")
            elif error5 == 1:
                print("ERROR FOUND!!!")
                if dmg5 == 2:
                    if safemode:
                        PCHP -=3
                        print("66% Currupted")
                    else:
                        PCHP -= 5
                        print("50% CURRUPTED")
                else:
                    print("SAFE")
                if safemode:
                    print("3 Crypto Collected")
                    crypto += 3
                else:
                    print("5 Crypto Collected")
                    crypto += 5

#---------------------------CD COMMANDS-----------------------------------------
    elif commandInput == "cd root":
        if directory == "root":
            print("Already There!")
        else:
            print("cd to root...")
            directory = "root"

    elif commandInput == "cd two_drove":
        if directory == "two_drove":
            print("Already There!")
        else:
            print("-ERROR: CANNOT CD INTO CLOUD STORAGE-")

    elif commandInput == "cd app_data":
        if directory == "app_data":
            print("Already There!")
        else:
            print("cd to app_data...")
            directory = "app_data"

    elif commandInput == "cd curseforge":
        if directory == "curseforge":
            print("Already There!")
        else:
            print("cd to curseforge...")
            directory = "curseforge"

    elif commandInput == "drive options":
        print("ssd")
        print("hard drive")

    elif commandInput == "cd hard drive":
        print("-Connection Failed-")
#-----------------------------VERSION-------------------------------------------
    elif commandInput == "version":
        print(version)
#------------------------------EXIT---------------------------------------------
    elif commandInput == "exit":
        print("Exiting...")
        run = 0
#---------------------------CD SSD----------------------------------------------
    elif commandInput == "cd ssd":
            print("Folder Selection: ")
            print(" ")
            print(folderSelection1 + "     " + str(GB11) + "GB Free")
            print(" ")
            print(folderSelection2 + "     " + str(GB22) + "GB Free")
            print(" ")
            print(folderSelection3 + "     " + str(GB33) + "GB Free")
            print(" ")
            cdFolder = input("C:/Users/" + user + "/ssd" + "> ")
            folderName = cdFolder.split()
            folder_name = str(folderName[1])
            print(" ")
            if folder_name in cdOptions:
                if folder_name == str(folderSelection1):
                    print("Opened " + folderSelection1)
                    print(" ")
                    print("Item Selection: \n")
                    GB4 = random.randint(2,48)
                    print(itemSelection1 + "     " + str(GB44) + "GB")
                    print(" ")
                    GB5 = random.randint(2,48)
                    print(itemSelection2 + "     " + str(GB55) + "GB")
                    print(" ")
                    GB6 = random.randint(2,48)
                    print(itemSelection3 + "     " + str(GB66) + "GB")
                    print(" ")
                    GB7 = random.randint(2,48)
                    print(itemSelection4 + "     " + str(GB77) + "GB")
                    print(" ")
                    GB8 = random.randint(2,48)
                    print(itemSelection5 + "     " + str(GB88) + "GB")
                    print(" ")

                    cdItems = input("C:/Users/" + user + "/ssd" + "/" + folderSelection1 + "> ")
                    if cdItems in cdItemsOptionsList and cdItems == "cd crypto":
                        print("Crypto Found!!!")
                        cryptoUnfound = 0
                        print("\nMoving on to decryption process...")
                    elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                        print("ERROR: NOT CRYPTO")
                        print(" ")
                    else:
                        print("Failed: Not Found \n")

                elif folder_name == str(folderSelection2):
                    print("Opened " + folderSelection2)
                    print(" ")
                    print("Item Selection: \n")
                    GB9 = random.randint(2,48)
                    print(itemSelection6 + "     " + str(GB9) + "GB")
                    print(" ")
                    GB10 = random.randint(2,48)
                    print(itemSelection7 + "     " + str(GB10) + "GB")
                    print(" ")
                    GB11 = random.randint(2,48)
                    print(itemSelection8 + "     " + str(GB11) + "GB")
                    print(" ")
                    GB12 = random.randint(2,48)
                    print(itemSelection9 + "     " + str(GB12) + "GB")
                    print(" ")
                    GB13 = random.randint(2,48)
                    print(itemSelection10 + "     " + str(GB13) + "GB")
                    print(" ")

                    cdItems = input("C:/Users/" + user + "/ssd" + "/" + folderSelection2 + "> ")
                    if cdItems in cdItemsOptionsList and cdItems == "cd crypto":
                        print("Crypto Found!!!")
                        cryptoUnfound = 0
                        print("\nMoving on to decryption process...")
                    elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                        print("ERROR: NOT CRYPTO")
                        print(" ")
                    else:
                        print("Failed: Not Found \n")

                elif folder_name == str(folderSelection3):
                    print("Opened " + folderSelection3)
                    print(" ")
                    print("Item Selection: \n")
                    GB14 = random.randint(2,48)
                    print(itemSelection11 + "     " + str(GB14) + "GB")
                    print(" ")
                    GB15 = random.randint(2,48)
                    print(itemSelection12 + "     " + str(GB15) + "GB")
                    print(" ")
                    GB16 = random.randint(2,48)
                    print(itemSelection13 + "     " + str(GB16) + "GB")
                    print(" ")
                    GB17 = random.randint(2,48)
                    print(itemSelection14 + "     " + str(GB17) + "GB")
                    print(" ")
                    GB18 = random.randint(2,48)
                    print(itemSelection15 + "     " + str(GB18) + "GB")
                    print(" ")

                    cdItems = input("C:/Users/" + user + "/ssd" + "/" + folderSelection3 + "> ")
                    if cdItems in cdItemsOptionsList and cdItems == "cd crypto":
                        print("Crypto Found!!!")
                        cryptoUnfound = 0
                        print("\nMoving on to decryption process... ERROR")
                    elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                        print("ERROR: NOT CRYPTO]n")
                    else:
                        print("Failed: Not Found \n")
#---------------------------MOVE COMMANDS---------------------------------------
    elif commandInput == "move":
        if system == "videoPC":
            print("Moving To BPA System PC\n")
            system = "bpaPC"
        elif system == "bpaPC":
            print("Moving To Off Site System PC\n")
            system = "customPC"
        elif system == "customPC":
            print("Moving To Coding System PC\n")
            system = "codingPC"
        elif system == "codingPC":
            print("Moving To Macrostrong System PC\n")
            system = "macroPC"
        elif system == "macroPC":
            print("Moving To Video System PC\n")
            system = "videoPC"
#---------------------------LIST------------------------------------------------
    elif commandInput == "list":
        while lrun:
            print(name)
            print("    Options:\n")
            print("1) Add Item")
            print("2) Remove Item")
            print("3) View List")
            print("4) Clear List")
            print("5) Number of Items")
            print("6) Exit")
            print("7) Rename List")
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
                List = []
                print("List Succesfully Cleared!\n")
                print("--------------------------------------------------")
            if options == "5":
                length = len(list1)
                print("Items in list: " + str(length) + "\n")
                print("--------------------------------------------------")
            if options == "6":
                lrun = 0
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
                        print(listVersion)
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

#---------------------------CONSOLE COMMANDS------------------------------------
    elif commandInput == "`":
        while MAINconsole:
            console = input("C:/Users/" + user + "CONSOLE>")
            if console == "version":
                print(version)
            elif console == "exit":
                MAINconsole = 0
                run = 0
            elif console == "info":
                print("CShell - CadmiumShell")
                print("Chromindium - Chromium + Indium")
                print("CSE - CadmiumShell Edition")
                print("DEV - <ERROR>")
            elif console == "help":
                print("DEV - Dev mode")
                print("log - Log & changelog")
                print("user - Change user")
                print("exit - <ENDS CSHELL>")
                print("info - Gives information")
                print("version - Prints version")
            elif console == "DEV":
                DEVM = 1
            elif console == "user":
                if DEVM == 1:
                    print("ERROR DEV MODE ENABLED")
                elif DEVM != 1:
                    user = input("Change User To: ")
            elif console == "log":
                print("LOG:\n")
                print("ADD FIREWALL, LITERALLY []")
                print("ADD TURNBASE TO CSHELL []")
                print("CHANGE SAFEMODE AND PCHP TO BE SYSTEM DEPENDANT []")
                print("ADD PROFILE MODE WITH LOGIN AND AGE ETC []")
                print("ADD SMOKE (STEAM ALT) TO RUN NON TERMINAL GAMES LIKE")
                print("GUESSING GAME AND BAR []")
                print("ADD BAR TO FANTASY LAND []")
                print("ADD A USER LIST AND HELP MENU TO THE CONSOLE AND LOGIN []")
                print("-------------------------------------------------------")
                print("Changelog - (CAPs for Log items)\n")
                print("Changed Company Name From Macrostrong To Chromiodine")
                print("Changed OS Name From Doors To Cobalt Co")
                print("Changed Company Name To Chromindium")
                print("Changed Shell Name To Cadmium Shell - CS")
                print("ADDED A SAFE MODE THAT REDUCES DMG AND CRYPTO")
                print("ADDED DEATH OF PC DUE TO ERRORS/VIRUS")
                print("ADDED SYSTEMINFO FOR BPA PC")
                print("Added Virus Catcher")
                print("ADDED SYSTEMINFO FOR PROGRAMMING PC")
                print("-------------------------------------------------------")
            else:
                print("<ERROR>")

#---------------------------SYSTEM INFO-----------------------------------------
    elif commandInput == "systeminfo" and system == "videoPC":
        print("System Information: \n")
        print("Host Name:                       LAB501-1020346")
        print("OS Name:                         Microsoft Windows 11 Pro")
        print("OS Version:                      10.0.22631 N/A Build 22631")
        print("OS Manufacturer:                 Microsoft Corporation")
        print("OS configuration:                Member Workstation")
        print("OS Build Type:                   Multiprocessor Free")
        print("Registered Owner:                cmsadm")
        print("Registered Organization:         N/A")
        print("Project ID:                      00355-60797-34414-AAOEM")
        print("Original Install Date:           2/14/2024, 7:59:27 AM")
        print("System Boot Time:                10/1/2025, 8:49:35 AM")
        print("System Manufacturer:             ASUSTeK COMPUTER INC.")
        print("System Model:                    ROG STRIX G15CF_G15CF")
        print("System Type:                     x64-based PC")
        print("Processor(s):                    1 Processor(s) Installed")
        print("                                 [01]: Intel64 Family 6 Model 151 Stepping 2 GenuineIntel ~2100 Mhz")
        print("BIOS Version:                    American Megatrends Inc. G15CF.301, 1/24/2022")
        print("Doors Directory:                 C:\\WINDOWS")
        print("System Directory                 C:\\WINDOWS\\system32")
        print("Boot Device:                     \\Device\\HarddiskVolume1")
        print("System Locale:                   en-us;English (United States)")
        print("Input Locale:                    en-us;English (United States)")
        print("Time Zone:                       (UTC-07:00) Mountain Time (US & Canada)")
        print("Total Physical Memory:           32,509 MB")
        print("Available Physical Memory:       23,409 MB")
        print("Virtual Memory: Max Size:        34,557 MB")
        print("Virtual Memory: Available:       24,784 MB")
        print("Virtual Memory: In Use:          9,773 MB")
        print("Page File Location(s):           C:\\pagefile.sys")
        print("Domain:                          carlsbad.k12.nm.us")
        print("Logon Server:                    \\\\CMS-DC02")
        print("Hotfix(s):                       4 Hotfix(s) Installed.")
        print("                     [01]: KB5042099")
        print("                     [02]: KB5027397")
        print("                     [03]: KB5043076")
        print("                     [04]: KB5043937")
        print("Network Card(s):                 4 NIC(s) Installed.")
        print("                     [01]: Realtek Gaming 2.5GbE Family Controller")
        print("                         Connection Name: Ethernet")
        print("                         DHCP Enabled:    Yes")
        print("                         DHCP Server:     10.30.1.1")
        print("                         IP address(es)")
        print("                         [01]: 10.200.114.10")
        print("                         [02]: fe80::9238:6651:4a72:b674")
        print("                     [02]: MediaTek Wi-Fi 6 MT7921 Wireless LAN Card")
        print("                         Connection Name: Wi-Fi")
        print("                         Status:          Media disconnected")
        print("                     [03]: Bluetooth Device (Personal Area Network)")
        print("                         Connection Name: Bluetooth Network Connection")
        print("                         Status:          Media disconnected")
        print("                     [04]: Cisco AnyConnect Virtual Miniport Adapter for Windows x64")
        print("                         Connection Name: Ethernet 2")
        print("                         Status:          Hardware not present")
        print("Hyper-V Requirements:            A hypervisor has been detected.")
        print("Features required for Hyper-V will not be displayed.")

    elif commandInput == "systeminfo" and system == "customPC":
        print("System Information: \n")
        print("Host Name:                       COBALT-PROTOTYPE")
        print("OS Name:                         Chromindium Cobalt Ti3")
        print("OS Version:                      9.17.2025 -- Build Ti3")
        print("OS Manufacturer:                 Cobalt Corporation")
        print("OS configuration:                Member Workstation")
        print("OS Build Type:                   Multiprocessor Free")
        print("Registered Owner:                CSCO")
        print("Registered Organization:         N/A")
        print("Project ID:                      23190-71613-12345-AAACO")
        print("Original Install Date:           10/15/2025, 9:36:15 AM")
        print("System Boot Time:                10/16/2025, 8:49:35 AM")
        print("System Manufacturer:             CHROMINDIUM INC.")
        print("System Model:                    COBALT Titanium Prototype-Three")
        print("System Type:                     x64-based PC")
        print("Processor(s):                    1 Processor(s) Installed")
        print("                                 [01]: SUPEZ-64  ~52100 Mhz")
        print("BIOS Version:                    <CLASSIFIED>")
        print("Doors Directory:                 C:\\COBALT")
        print("System Directory                 C:\\COBALT\\system32")
        print("Boot Device:                     \\Device\\HarddiskVolume0")
        print("System Locale:                   en-us;English (United States)")
        print("Input Locale:                    en-us;English (United States)")
        print("Time Zone:                       (UTC-07:00) Mountain Time (US & Canada)")
        print("Total Physical Memory:           32,509 MB")
        print("Available Physical Memory:       23,409 MB")
        print("Virtual Memory: Max Size:        34,557 MB")
        print("Virtual Memory: Available:       24,784 MB")
        print("Virtual Memory: In Use:          9,773 MB")
        print("Page File Location(s):           C:\\pagefile.sys")
        print("Domain:                          N/A")
        print("Logon Server:                    \\\\CBC-AC32")
        print("Hotfix(s):                       0 Hotfix(s) Installed.")

    elif commandInput == "systeminfo" and system == "bpaPC":
        print("System Information: \n")
        print("Host Name:                       LAB7-D-1020572")
        print("OS Name:                         Microsoft Windows 11 Pro")
        print("OS Version:                      10.0.22621 N/A Build 22621")
        print("OS Manufacturer:                 Microsoft Corporation")
        print("OS configuration:                Member Workstation")
        print("OS Build Type:                   Multiprocessor Free")
        print("Registered Owner:                cmsadm")
        print("Registered Organization:         N/A")
        print("Project ID:                      00355-60797-34384-AAOEM")
        print("Original Install Date:           2/10/2023, 10:17:25 AM")
        print("System Boot Time:                10/10/2025, 11:36:00 AM")
        print("System Manufacturer:             ASUSTeK COMPUTER INC.")
        print("System Model:                    ROG STRIX G15CF_G15CF")
        print("System Type:                     x64-based PC")
        print("Processor(s):                    1 Processor(s) Installed")
        print("                                 [01]: Intel64 Family 6 Model 151 Stepping 2 GenuineIntel ~2100 Mhz")
        print("BIOS Version:                    American Megatrends Inc. G15CF.301, 1/24/2022")
        print("Doors Directory:                 C:\\WINDOWS")
        print("System Directory                 C:\\WINDOWS\\system32")
        print("Boot Device:                     \\Device\\HarddiskVolume1")
        print("System Locale:                   en-us;English (United States)")
        print("Input Locale:                    en-us;English (United States)")
        print("Time Zone:                       (UTC-07:00) Mountain Time (US & Canada)")
        print("Total Physical Memory:           32,509 MB")
        print("Available Physical Memory:       25,146 MB")
        print("Virtual Memory: Max Size:        34,557 MB")
        print("Virtual Memory: Available:       25,353 MB")
        print("Virtual Memory: In Use:          9,204 MB")
        print("Page File Location(s):           C:\\pagefile.sys")
        print("Domain:                          carlsbad.k12.nm.us")
        print("Logon Server:                    \\\\LAB7-D-1020572")
        print("Hotfix(s):                       4 Hotfix(s) Installed.")
        print("                     [01]: KB5020880")
        print("                     [02]: KB5012170")
        print("                     [03]: KB5022303")
        print("                     [04]: KB5020487")
        print("Network Card(s):                 2 NIC(s) Installed.")
        print("                     [01]: Realtek Gaming 2.5GbE Family Controller")
        print("                         Connection Name: Ethernet")
        print("                         DHCP Enabled:    Yes")
        print("                         DHCP Server:     10.30.1.1")
        print("                         IP address(es)")
        print("                         [01]: 10.200.114.101")
        print("                         [02]: fe80::6bc3:fe87:5a4d:9dea")
        print("                   [02]: MediaTek Wi-Fi 6 MT7921 Wireless LAN Card")
        print("                         Connection Name: Wi-Fi")
        print("                         Status:          Media disconnected")
        print("Hyper-V Requirements:            A hypervisor has been detected.")
        print("Features required for Hyper-V will not be displayed.")

    elif commandInput == "systeminfo" and system == "codingPC":
        print("System Information: \n")
        print("Host Name:                       PLTW-SL-1027522")
        print("OS Name:                         Microsoft Windows 11 Pro")
        print("OS Version:                      10.0.22631 N/A Build 22631")
        print("OS Manufacturer:                 Microsoft Corporation")
        print("OS configuration:                Member Workstation")
        print("OS Build Type:                   Multiprocessor Free")
        print("Registered Owner:                CMSADM")
        print("Registered Organization:         HP Inc.")
        print("Project ID:                      00355-60997-54423-AAOEM")
        print("Original Install Date:           1/10/2024, 8:22:42 AM")
        print("System Boot Time:                8/28/2025, 7:45:32 AM")
        print("System Manufacturer:             HP")
        print("System Model:                    HP ProBook 450 15.6 inch G10 Notebook PC")
        print("System Type:                     x64-based PC")
        print("Processor(s):                    1 Processor(s) Installed")
        print("                                 [01]: Intel64 Family 6 Model 186 Stepping 3 GenuineIntel ~1700 Mhz")
        print("BIOS Version:                    HP V72 Ver. 01.07.01, 12/9/2024")
        print("Doors Directory:                 C:\\WINDOWS")
        print("System Directory                 C:\\WINDOWS\\system32")
        print("Boot Device:                     \\Device\\HarddiskVolume1")
        print("System Locale:                   en-us;English (United States)")
        print("Input Locale:                    en-us;English (United States)")
        print("Time Zone:                       (UTC-07:00) Mountain Time (US & Canada)")
        print("Total Physical Memory:           16,016 MB")
        print("Available Physical Memory:       5,596 MB")
        print("Virtual Memory: Max Size:        17,040 MB")
        print("Virtual Memory: Available:       3,715 MB")
        print("Virtual Memory: In Use:          13,325 MB")
        print("Page File Location(s):           C:\\pagefile.sys")
        print("Domain:                          carlsbad.k12.nm.us")
        print("Logon Server:                    \\\\CMS-DCECHS")
        print("Hotfix(s):                       7 Hotfix(s) Installed.")
        print("                     [01]: KB5050578")
        print("                     [02]: KB5012170")
        print("                     [03]: KB5027397")
        print("                     [04]: KB5031274")
        print("                     [05]: KB5036212")
        print("                     [06]: KB5052094")
        print("                     [07]: KB5052107")
        print("Network Card(s):                 4 NIC(s) Installed.")
        print("                     [01]: Realtek PCIe GbE Family Controller")
        print("                         Connection Name: Ethernet")
        print("                         Status:          Media disconnected")
        print("                     [02]: Intel(R) Wi-Fi 6E AX211 160MHz")
        print("                         Connection Name: Wi-Fi")
        print("                         DHCP Enabled:    Yes")
        print("                         DHCP Server:     10.30.1.1")
        print("                         IP address(es)")
        print("                         [01]: 172.19.163.200")
        print("                         [02]: fe80::b72d:be33:bc9b:3c8")
        print("                     [03]: Bluetooth Device (Personal Area Network)")
        print("                         Connection Name: Bluetooth Network Connection")
        print("                         Status:          Media disconnected")
        print("                     [04]: Cisco AnyConnect Virtual Miniport Adapter for Windows x64")
        print("                         Connection Name: Ethernet 2")
        print("                         Status:          Hardware not present")
        print("Hyper-V Requirements:            A hypervisor has been detected.")
        print("Features required for Hyper-V will not be displayed.")

    elif commandInput == "systeminfo" and system == "macroPC":
        print("System Information: \n")
        print("OS Name:                         Macrostrong Doors 22")
        print("OS Version:                      9.17.2025 BUILD 279841")
        print("OS Manufacturer:                 Macrostrong Corporation")
        print("OS configuration:                Standolone Workstation")
        print("OS Build Type:                   Multiprocessor Free")
        print("Registered Owner:                Macrostrong Organization")
        print("Project ID:                                              ")
        print("Original Install Date:           9/18/2025, 18:57:58")
        print("System Boot Time:                12/16/2025, 22:46:18")
        print("System Manufacturer:             To Be Filled By O.E.M")
        print("System Model:                    To Be Filled By O.E.M")
        print("System Type:                     x64-based PC")
        print("Processor(s):                    1 Processor(s) Installed")
        print("                                 [01]: 12th Gen Intel(R) Core(TM) i5-1235U (12 threads, 4.400GHz)")
        print("BIOS Version:                    <ERROR> BIOS VERSION NOT FOUND")
        print("Doors Directory:                 C:/DOORS")
        print("Boot Device:                     C:/DOORS/system32")
        print("System Locale:                   en-us;English (United States)")
        print("Input Locale:                    en-us;English (United States)")
        print("Time Zone:                       (UTC-6:00) MDT")
        print("Total Physical Memory:           8,192 MB")
        print("Available Physical Memory:       1,362 MB")
        print("Virtual Memory: Max Size:        8,192 MB")
        print("Virtual Memory: Available:       1,362 MB")
        print("Virtual Memory: In Use:          6,830 MB")
        print("Page File Location(s):           C:/pagefile.sys")
        print("Domain:                          WORKGROUP")
        print("Logon Server:                             ")
        print("Hotfix(s):                       0 Hotfix(s) Installed\n")

#---------------------------GUESSING GAME--------------------------------------
    elif commandInput == "guess":
        RangeNumOne = input("Insert Number One: ")
        RangeNumTwo = input("Insert Number Two: ")
        RangeNumOne = int(RangeNumOne)
        RangeNumTwo = int(RangeNumTwo)
        SecretNum = random.randint(RangeNumOne,RangeNumTwo)
        print("The Range Is " + str(RangeNumOne) + "-" + str(RangeNumTwo))
        while Guess != SecretNum and GuessesLeft > 0:
            Guess = input("Insert A Number: ")
            Guess = int(Guess)
            if Guess > SecretNum:
                print("Wrong")
                print("Guess Lower")
            if Guess < SecretNum:
                print("Wrong")
                print("Guess Higher")
            GuessesLeft -= 1
            print("Guesses Left: " + str(GuessesLeft))
            print(" ")
            if Guess == "console":
                console = 1
                while console:
                    console = input("C:/Users/" + user + "/DECRYPT/" + "CONSOLE>")
                    if console == "secretNum":
                        print(SecretNum)
                    elif console == "version":
                        print(GuessVersion)
                    elif console == "exit":
                        console = 0
                    elif console == "hi":
                        print("Hello!")
                    elif console == "help":
                        print("Commands: \nsecretNum\nversion\nexit\nDEV\nend\nchangeUser\n")
                    elif console == "DEV":
                        print("Place Holder")
                    elif console == "end":
                        Guess = SecretNum
                        console = 0
                    elif console == "changeUser":
                        user = input("New User: ")
                    else:
                        print("<ERROR>")

        if GuessesLeft > 0 and Guess == SecretNum:
            print("Correct!")

        elif GuessesLeft < 0:
          print("Out Of Guesses! Game Over!")
          print(" ")
        print("The Secret Number Was " + str(SecretNum) + "!")
#---------------------PC HEALTH-------------------------------------------------
if PCHP <= 0:
    print("CRITICAL FAILIURE!!!")