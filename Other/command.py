import random
user = "nerd"
GB = random.randint(12,300)
twodnum = 10
threednum = 100
win = 0
cryptoUnfound = 1
timer = 120
words = 1
console = 0
code = 0
version = "Command Line Version 1.1"
#Folders
folders = ["crypto", "photos", "videos", "games", "extra", "other", "admin", "user", "hard drive"]
selected_folders = random.sample(folders, 3)
folderSelection1 = selected_folders[0]
folderSelection2 = selected_folders[1]
folderSelection3 = selected_folders[2]
cdOptions = [folderSelection1, folderSelection2, folderSelection3]

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
while cryptoUnfound and timer > 0:
    print("Macrostrong Doors [Version 9.17.2025]")
    print("Copyright (c) 2025 Macrostrong Corporation. All rights reserved.")
    print("Type \"help\" For The Commands\n")
    print("\"ssd\" Detected\n")
    cdSSD = input("C:/Users/" + user + "> ")
    print(" ")
    if cdSSD == "help":
        print("Command Display: \n")
        print("cd - Used to move into a directory and open it.\n")
        #print("move - Used to move a file from one folder to another. <COMMAND_NOT_ACTIVE>\n")
        print("systeminfo - Used to view information about PC\n")
        print("exit - Used to leave the command line.\n")
        cdSSD = input("C:/Users/" + user + "> ")
    if cdSSD == "`":
        while console:
            console = input("C:/Users/" + user + "/DECRYPT/" + "CONSOLE>")
            if console == "code":
                print(code)
            elif console == "version":
                print(version)
            elif console == "exit":
                console = 0
            elif console == "hi":
                print("Hello!")
            elif console == "help":
                print("find out yourself- Cayd")
            elif console == "skip crypto":
                cryptoUnfound = 0
                print("Crypto Terminal has be skipped!")
            elif console == "DEV":
                print("Place Holder")
            else:
                print("<ERROR>")
    cdSSD = input("C:/Users/" + user + "> ")

    if cdSSD == "exit":
        timer = 0
        cryptoUnfound = 1
        print("Exiting... ")
    if cdSSD == "systeminfo":
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
        cdSSD = input("C:/Users/" + user + "> ")