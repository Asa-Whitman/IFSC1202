Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Num3 = int(input("Enter third number: "))

if Num1 == Num2 and Num2 == Num3:
    print(3)
elif Num1 == Num2 or Num2 == Num3:
    print(2)
else:
    print(0)
