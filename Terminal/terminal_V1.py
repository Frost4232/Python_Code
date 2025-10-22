import random
user = "nerd"
GB = random.randint(12,300)
twodnum = 10
threednum = 100

#Folders
folders = ["crypto", "photos", "videos", "games", "extra", "other", "admin", "user"]
selected_folders = random.sample(folders, 3)
folderSelection1 = selected_folders[0]
folderSelection2 = selected_folders[1]
folderSelection3 = selected_folders[2]
cdOptions = ["cd " + folderSelection1, "cd " + folderSelection2, "cd " + folderSelection3]

#Items/Folder
twodnum = random.randint(10,99)
threednum = random.randint(100,999)
pTypeList = [".png", ".jpg"]
pType = random.choice(pTypeList)
items = ["crypto", "photo" + twodnum + pType, "video" + threednum + ".mp4", "notes.txt", "audio.mp3", "stea,.exe", "clash_vid.mp4", "music.mp3", "game.8xp"]
selected_items = random.sample(items, 5)
itemSelection1 = selected_items[0]
itemSelection2 = selected_items[1]
itemSelection3 = selected_items[2]
itemSelection4 = selected_items[3]
itemSelection5 = selected_items[4]

#Terminal Setup
print("Macrostrong Doors [Version 9.17.2025]")
print("Copyright (c) 2025 Macrostrong Corporation. All rights reserved.")
print(" ")
cdSSD = input("C:/Users/" + user + "> ")
print(" ")

#CD Options
if cdSSD == "cd ssd":
    print("Folder Selection: ")
    print(" ")
    print(folderSelection1 + "     " + str(GB) + "GB Free")
    print(" ")
    GB = random.randint(12,300)
    print(folderSelection2 + "     " + str(GB) + "GB Free")
    print(" ")
    GB = random.randint(12,300)
    print(folderSelection3 + "     " + str(GB) + "GB Free")
    print(" ")
    cdFolder = input("C:/Users/" + user + "/ssd" + "> ")
    print(" ")
    if cdFolder in cdOptions:
        print("Folder Opened")
