import random
user = "nerd"
GB = random.randint(12,300)
twodnum = 10
threednum = 100
win = 0
cryptoUnfound = 1
timer = 120
words = 1

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

#Terminal Setup
print("Macrostrong Doors [Version 9.17.2025]")
print("Copyright (c) 2025 Macrostrong Corporation. All rights reserved.")
print(" ")
cdSSD = input("C:/Users/" + user + "> ")
print(" ")

#CD Options
GB2 = random.randint(12,300)
GB3 = random.randint(12,300)

while cryptoUnfound and timer > 0:
    if cdSSD == "cd ssd":
        print("Folder Selection: ")
        print(" ")
        print(folderSelection1 + "     " + str(GB) + "GB Free")
        print(" ")
        print(folderSelection2 + "     " + str(GB2) + "GB Free")
        print(" ")
        print(folderSelection3 + "     " + str(GB3) + "GB Free")
        print(" ")
        cdFolder = input("C:/Users/" + user + "/ssd" + "> ")
        folderName = cdFolder.split()
        folder_name = str(folderName[1])
        print(" ")
        if folder_name in cdOptions:
            if folder_name == str(folderSelection1):
                print("Opened " + folderSelection1)
                print(" ")
                print("Item Selection: ")
                print(" ")
                GB4 = random.randint(2,48)
                print(itemSelection1 + "     " + str(GB4) + "GB")
                print(" ")
                GB5 = random.randint(2,48)
                print(itemSelection2 + "     " + str(GB5) + "GB")
                print(" ")
                GB6 = random.randint(2,48)
                print(itemSelection3 + "     " + str(GB6) + "GB")
                print(" ")
                GB7 = random.randint(2,48)
                print(itemSelection4 + "     " + str(GB7) + "GB")
                print(" ")
                GB8 = random.randint(2,48)
                print(itemSelection5 + "     " + str(GB8) + "GB")
                print(" ")

                cdItems = input("C:/Users/" + user + "/ssd" + "/" + folderSelection1 + "> ")
                if cdItems in cdItemsOptionsList and cdItems == "cd crypto":
                    print("Crypto Found!!!")
                    cryptoUnfound = 0
                    print("\nYou Win!")
                elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                    print("ERROR: NOT CRYPTO")
                    print(" ")
                else:
                    print("Failed: Not Found \n")

            elif folder_name == str(folderSelection2):
                print("Opened " + folderSelection2)
                print(" ")
                print("Item Selection: ")
                print(" ")
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
                    print("\nYou Win!")
                elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                    print("ERROR: NOT CRYPTO")
                    print(" ")
                else:
                    print("Failed: Not Found \n")

            elif folder_name == str(folderSelection3):
                print("Opened " + folderSelection3)
                print(" ")
                print("Item Selection: ")
                print(" ")
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
                    print("\nYou Win!")
                elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                    print("ERROR: NOT CRYPTO")
                    print(" ")
                else:
                    print("Failed: Not Found \n")