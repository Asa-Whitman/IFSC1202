Kilometers = float(input("Enter length of race in kilometers: "))
Miles = Kilometers / 1.61

Minutes = int(input("enter minutes: "))
Seconds = int(input("enter seconds: "))

MinuteSeconds = float(Seconds / 60)
TotalMinutes = float(MinuteSeconds + Minutes)
Hours = float(TotalMinutes / 60)
MpH = Miles / Hours
print(MpH)