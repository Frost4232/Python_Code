import math

C = 0
favNum = input("What is your favorite number? ")
print(" ")

#Question 1
A = input("What is " + favNum + " squared? ")
A = int(A)
correctAns1 = int(favNum) * int(favNum)
if A == correctAns1:
    print("Correct! ")
    C += 1
else:
    print("Incorrect! ")
print(" ")

#Question 2
B = input("What is the square root of " + favNum + "? ")
B = float(B)
CorrectAns2 = math.sqrt(float(favNum))
if B == CorrectAns2:
    print("Correct! ")
    C += 1
else:
    print("Incorrect! ")
print(" ")

#Question Count + End
print("Questions correct: " + str(C))