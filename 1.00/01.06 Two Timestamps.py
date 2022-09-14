print("First timestamp (use 24hr format)")
HourOne = int(input("Enter hour: "))
MinuteOne = int(input("Enter minute: "))
SecondOne = int(input("Enter second: "))

print("Second timestamp (use 24hr format)")
HourTwo = int(input("Enter hour: "))
MinuteTwo = int(input("Enter minute: "))
SecondTwo = int(input("Enter second: "))

TotalHour = HourTwo - HourOne
TotalMinute = MinuteTwo - MinuteOne
TotalSecond = SecondTwo - SecondOne

HourtoSecond = TotalHour * 3600
MinutetoSecond = TotalMinute * 60
FinalSecond = HourtoSecond + MinutetoSecond + TotalSecond
print(FinalSecond)