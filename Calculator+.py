# Picking A Calculator
print("1 For Addition.")
print("2 For Multiplication.")
print("3 For Division.")
print("4 For Subtraction.")
calc = input("What Calculator Do You Need?")
# Addition Calculator
if calc == str("1"):
    A1 = input("First:")
    A2 = input("Second:")
    Sum = (float(A1) + float(A2))
    print("sum: " + str(Sum))
# Multiplication Calculator
elif calc == str("2"):
    X1 = input("First:")
    X2 = input("Second:")
    product = (float(X1) * float(X2))
    print("Product:" + str(product))
# Division Calculator
elif calc == str("3"):
    D1 = input("First:")
    D2 = input("Second:")
    quotient = float(D1) / float(D2)
    print("Quotient:" + str(quotient))
# Subtraction Calculator
elif calc == str("4"):
    S1 = input("First:")
    S2 = input("Second:")
    difference = float(S1) - float(S2)
    print("Difference:" + str(difference))
print("DONE")
