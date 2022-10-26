#coding by Asa Whitman
NamesFile = open("Exam Two Names.txt")
Girlslist =[]
Boyslist =[]
Names = NamesFile.readline()
while Names != "":
    x = Names.split(',')
    Boyslist.append(x[0])
    Girlslist.append(x[1].strip())
    Names = NamesFile.readline()
NamesFile.close()
UserName = input("Enter a name:")
UserName = UserName.strip()
UserName = UserName.lower()
UserName = UserName.capitalize()
if UserName != 'Q':
    i=0
    if UserName in Boyslist or UserName in Girlslist:
        for i in range (len(Boyslist)):
            if UserName == Boyslist[i]:
                print("Boy's name. Rank: {}".format(i+1))
        for i in range (len(Girlslist)):
            if UserName == Girlslist[i]:
                print("Girl's name. Rank: {}".format(i+1))
    else:
        print("Name not found!")