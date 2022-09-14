import math
FromValue = float(input("Enter from value: "))
FromUnit = str(input("Enter from unit (in, ft, yd, mi): "))
if FromUnit != "in" and FromUnit != "ft" and FromUnit != "yd" and FromUnit != "mi":
    print("invalid from unit")
else:
    ToUnit = str(input("Enter to unit (in, ft, yd, mi): "))
    if ToUnit != "in" and ToUnit != "ft" and ToUnit != "yd" and ToUnit != "mi":
        print("invalid to unit")
    elif FromUnit == "in":
        if ToUnit == "in":
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, FromValue, FromUnit))
        elif ToUnit == "ft":
            multiplier = 0.0833333
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "yd":
            multiplier = 0.0277778
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "mi":
            multiplier = 0.0000158
            ToValue = FromValue * multiplier
            print("{:f} {:s} => approx. {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
    elif FromUnit == "ft":
        if ToUnit == "in":
            multiplier = 12
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "ft":
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, FromValue, FromUnit))
        elif ToUnit == "yd":
            multiplier = 0.0001893
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "mi":
            multiplier = 0.0001894
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
    elif FromUnit == "yd":
        if ToUnit == "in":
            multiplier = 36
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "ft":
            multiplier = 3
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "yd":
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, FromValue, ToUnit))
        elif ToUnit == "mi":
            multiplier = 0.0005681
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
    elif FromUnit == "mi":
        if ToUnit == "in":
            multiplier = 66360
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "ft":
            multiplier = 5280
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "yd":
            multiplier = 1760
            ToValue = FromValue * multiplier
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, ToValue, ToUnit))
        elif ToUnit == "mi":
            print("{:f} {:s} => {:f} {:s}".format(FromValue, FromUnit, FromValue, ToUnit))