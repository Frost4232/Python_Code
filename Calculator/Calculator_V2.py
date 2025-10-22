import math

print("welcome to Calc V2")
type = input("What Solver is needed?")

if type == "sqrt":
    sqrt_num = input("Type Number")
    ans = math.sqrt(int(sqrt_num))

if type == "sqrd":
    sqrd_num = input("Type Number")
    ans = int(sqrd_num) * int(sqrd_num)



print("Answer: " + str(ans))