userList = ["frost4232", "guest","Thecoolman3000", "Luretex", "007man", "DirtLord3817", "Jellybean"]
pswd = "1234"
superPSWD = "71613"
unlogged = 1
user = "guest"
creating = 1
createNew = " "
age = 12
email = "error@gmail.com"
name = "guest"


while unlogged:
    print("To Proceed To Cadmium Shell, Please Log In: \n")
    userLog = input("Login: ")
    userLog = userLog.lower()
    if userLog in userList:
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
            unlogged = 0
        pswdLog = input("Password: ")
        pswdLog = pswdLog.lower()
        if pswdLog == pswd or pswdLog == superPSWD:
            print("Logged In!")
            user = userLog
            user = userLog
            age = ageLog
            email = emailLog
            name = nameLog
            unlogged = 0
        else:
            print("Incorrect Password, Try Again.")
    else:
        print("User Not Found")
        createNew = input("Would You Like To Make A Temporary Account? ")
        createNew = createNew.lower()
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