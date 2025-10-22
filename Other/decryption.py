cryptoUnfound = 0
import random
user = "nerd"

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

                    #Set 3-5 code here------------------------------------------------------------------------------------------


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