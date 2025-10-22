import random
unlogged = 1
pswdLimit = 3

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