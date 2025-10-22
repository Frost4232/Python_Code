import random
unlogged = 1
pswdLimit = 3
setOne = random.randint(10,99)
setTwo = random.randint(10,99)
setThree = random.randint(10,99)
setFour = random.randint(10,99)
setFive = random.randint(10,99)
money = random.randint(1200,100000)
type = ["Bitcoin", "DogeCoin", "Other"]
cryptoType = random.choice(type)
decryptsLeft = 18
decrypt = 1
code = str(setOne) + str(setTwo) + str(setThree) + str(setFour) + str(setFive)
code = int(code)
fail = 0
codeEntered = 0
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

userList = ["user1234", "frosty", "007man", "dqrk3ning", "guest"]
user = random.choice(userList)

pswdList = ["1234", "snowy", "nerd", "abcd", "notnerd"]
pswd = random.choice(pswdList)

while unlogged and pswdLimit > 0:
    userLog = input("Login: ")
    userLog = userLog.lower()
    if userLog == user:
        pswdLog = input("Password: ")
        pswdLog = pswdLog.lower()
        if pswdLog == pswd:
            print("Logged In!")
            unlogged = 0
        else:
            print("Incorrect Password, Try Again.")
            pswdLimit -= 1
    else:
        print("User Not Found")
if unlogged == 0:
    print("Terminal Starting... \n")

    #Terminal Setup
    print("Macrostrong Doors [Version 9.17.2025]")
    print("Copyright (c) 2025 Macrostrong Corporation. All rights reserved.")
    #print("Type \"help\" For The Commands")
    print(" ")
    cdSSD = input("C:/Users/" + user + "> ")
    print(" ")
    #if cdSSD == "help":
    #add commands - cd, move, etc

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
                        print("\nMoving on to decryption process...")
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
                        print("\nMoving on to decryption process...")
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
                        print("\nMoving on to decryption process...")
                    elif cdItems in cdItemsOptionsList and cdItems != "cd crypto":
                        print("ERROR: NOT CRYPTO")
                        print(" ")
                    else:
                        print("Failed: Not Found \n")

    if cryptoUnfound == 0:
        while codeEntered == 0 and fail == 0:
            print("\n10 Digit Code Is Required To Decrypt\n")
            print("Choose A Set\n")
            print("-set one-    -set two-")
            print("-set one-    -set two-")
            print("      -set five-      ")
            print("\n-----ENTER--CODE-----")
            setChoice = input("\nC:/Users/" + user + "/DECRYPT> ")

            if setChoice == "set one":
                while decrypt != setOne and decryptsLeft > 0:
                    decrypt = input("C:/Users/" + user + "/DECRYPT/" + "10-99_SETONE>")
                    decrypt = int(decrypt)
                    if decrypt > setOne:
                        print("ERROR")
                        print("DECRYPT_LOWER")
                    if decrypt < setOne:
                        print("ERROR")
                        print("DECRYPT_HIGHER")
                        decryptsLeft -= 1
                        print("DECRYPTS_LEFT: " + str(decryptsLeft))
                        print(" ")
                    if decryptsLeft > 0 and decrypt == setOne:
                        print("DECRYPT SUCCESSFUL")
                        print("CODE_" + str(setOne))
                    if decryptsLeft < 0:
                        print("ERROR - CURRUPTED")
                        print(" ")
                        fail = 1
            if setChoice == "set two":
                while decrypt != setTwo and decryptsLeft > 0:
                    decrypt = input("C:/Users/" + user + "/DECRYPT/" + "10-99_SETTWO>")
                    decrypt = int(decrypt)
                    if decrypt > setTwo:
                        print("ERROR")
                        print("DECRYPT_LOWER")
                    if decrypt < setTwo:
                        print("ERROR")
                        print("DECRYPT_HIGHER")
                        decryptsLeft -= 1
                        print("DECRYPTS_LEFT: " + str(decryptsLeft))
                        print(" ")
                    if decryptsLeft > 0 and decrypt == setTwo:
                        print("DECRYPT SUCCESSFUL")
                        print("CODE_" + str(setTwo))
                    if decryptsLeft < 0:
                        print("ERROR - CURRUPTED")
                        print(" ")
                        fail = 1
            if setChoice == "set three":
                while decrypt != setThree and decryptsLeft > 0:
                    decrypt = input("C:/Users/" + user + "/DECRYPT/" + "10-99_SETTHREE>")
                    decrypt = int(decrypt)
                    if decrypt > setThree:
                        print("ERROR")
                        print("DECRYPT_LOWER")
                    if decrypt < setThree:
                        print("ERROR")
                        print("DECRYPT_HIGHER")
                        decryptsLeft -= 1
                        print("DECRYPTS_LEFT: " + str(decryptsLeft))
                        print(" ")
                    if decryptsLeft > 0 and decrypt == setThree:
                        print("DECRYPT SUCCESSFUL")
                        print("CODE_" + str(setThree))
                    if decryptsLeft < 0:
                        print("ERROR - CURRUPTED")
                        print(" ")
                        fail = 1
            if setChoice == "set four":
                while decrypt != setFour and decryptsLeft > 0:
                    decrypt = input("C:/Users/" + user + "/DECRYPT/" + "10-99_SETFOUR>")
                    decrypt = int(decrypt)
                    if decrypt > setFour :
                        print("ERROR")
                        print("DECRYPT_LOWER")
                    if decrypt < setFour :
                        print("ERROR")
                        print("DECRYPT_HIGHER")
                        decryptsLeft -= 1
                        print("DECRYPTS_LEFT: " + str(decryptsLeft))
                        print(" ")
                    if decryptsLeft > 0 and decrypt == setFour :
                        print("DECRYPT SUCCESSFUL")
                        print("CODE_" + str(setFour))
                    if decryptsLeft < 0:
                        print("ERROR - CURRUPTED")
                        print(" ")
                        fail = 1
            if setChoice == "set five":
                while decrypt != setFive and decryptsLeft > 0:
                    decrypt = input("C:/Users/" + user + "/DECRYPT/" + "10-99_SETFIVE>")
                    decrypt = int(decrypt)
                    if decrypt > setFive :
                        print("ERROR")
                        print("DECRYPT_LOWER")
                    if decrypt < setFive :
                        print("ERROR")
                        print("DECRYPT_HIGHER")
                        decryptsLeft -= 1
                        print("DECRYPTS_LEFT: " + str(decryptsLeft))
                        print(" ")
                    if decryptsLeft > 0 and decrypt == setFive :
                        print("DECRYPT SUCCESSFUL")
                        print("CODE_" + str(setFive))
                    if decryptsLeft < 0:
                        print("ERROR - CURRUPTED")
                        print(" ")
                        fail = 1


            if setChoice == "enter code":
                codeEnter = input("C:/Users/" + user + "/DECRYPT/" + "CODE>")
                if codeEnter == code:
                    print("\nCrypto Collected!")
                    print("\nCrypto Type: " + cryptoType)
                    print("\nMoney Collected: " + money)
                elif codeEnter != code:
                    print("CODE REJECTED!")
                    fail = 1
                else:
                    print("ERROR")