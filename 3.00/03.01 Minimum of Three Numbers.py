one = float(input("Enter first number: "))
two = float(input("Enter second number: "))
three = float(input("Enter third number: "))
if one < two:
    if one < three:
        print(one)
    elif one > three:
        print(three)
else:
    if two < three:
        print(two)
    else:
        print(three)