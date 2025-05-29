# Picking A Calculator
calc = input("What Calculator Do You Need?"
             " 1 For +"
             " 2 For *"
             " 3 For /"
             " 4 For -")
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