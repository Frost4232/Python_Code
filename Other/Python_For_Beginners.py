# Tuples
Number = (1, 2, 3, 3, 3, 3)
Number.count(3)
# Range
numbers = range(5, 10, 2)
for number in numbers:
    print(number)
# Lists
Names = ["Snow", "Dax", "Jonathan"]
print(Names[0])
print(len(Names))
# 1-Infinite
i = 1
while i <= 5:
    print(i)
    i = i + 1
# Weight (K And L)
weight = float(input("Weight:"))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

# Temp
Temp = input("What Is The Temperature?")
if int(Temp) > 80:
    print("It Is A Hot Day")
    print("Drink Lots Of Water")
elif int(Temp) > 60:
    print("It Is A Nice Day")
elif int(Temp) > 30:
    print("It Is A Bit Cold")
else:
    print("It Is Cold")
print("Done")

#Python For Beginners
course = "Python for Beginners"
print(course.upper())
print(course)
print(course.replace("for", "4"))
# Name And Age
name = input("What is your name?")
print("Hello " + name)
birth_year = input("Enter your birth year:")
age = 2024 - int(birth_year)
print("You Are")
print(age)
#Calculator
N1 = input("First:")
N2 = input("Second:")
sum = (float(N1) + float(N2))
print("sum: " + str(sum))