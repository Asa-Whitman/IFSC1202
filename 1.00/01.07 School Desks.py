A = int(input("Enter Classroom A: "))
B = int(input("Enter Classroom B: "))
C = int(input("Enter Classroom C: "))

AFullDesks = A // 2
APartialDesks = A % 2
ATotalDesks = AFullDesks + APartialDesks

BFullDesks = B // 2
BPartialDesks = B % 2
BTotalDesks = BFullDesks + BPartialDesks

CFullDesks = C // 2
CPartialDesks = C % 2
CTotalDesks = CFullDesks + CPartialDesks

TotalDesks = ATotalDesks + BTotalDesks + CTotalDesks
print(TotalDesks)