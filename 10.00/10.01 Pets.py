#coding by Asa Whitman
Petsfile = open("10.00/10.01 Pets.txt")
Petnamelist =[]
Pettypelist =[]
Petagelist =[]
Pets = Petsfile.readline()
while Pets != "":
    x = Pets.split(',')
    Petnamelist.append(x[0])
    Pettypelist.append(x[1].strip())
    Petagelist.append(x[2].strip())
Petsfile.close()
class Pets ():
    def __init__(self, Petname, Pettype, Petage):
        self.Petname = Petnamelist
        self.Pettype = Pettypelist
        self.Petage = Petagelist
