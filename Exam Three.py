#Coding by Asa Whitman
from math import pi
from math import sqrt
from math import acos
class Triangle():
    def __init__(self, side1, side2, side3):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
    def perimiter(self):
        return self.s1 + self.s2 + self.s3
    def Type(self):
        if self.s1 == self.s2 and self.s1 == self.s3:
            return("Equilateral")
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return("Isoceles")
        else:
            return("Scalene")
    def area(self):
        s = (self.s1 + self.s2 +self.s3)/2
        area=sqrt(s*(s-self.s1)*(s-self.s2)*(s-self.s3))
        return(area)
    def angles(self):
        angle1 = acos((self.s2 ** 2 + self.s3 ** 2 + self.s1 ** 2) / (2 * self.s2 * self.s3)) * (180 / pi)
        angle2 = acos((self.s3 ** 2 + self.s1 ** 2 + self.sb ** 2) / (2 * self.s3 * self.s1)) * (180 / pi)
        angle3 = acos((self.s1 ** 2 + self.s2 ** 2 + self.s3 ** 2) / (2 * self.s1 * self.s2)) * (180 / pi)
        anglelist = []
        anglelist.append(angle1)
        anglelist.append(angle2)
        anglelist.append(angle3)
        return anglelist
trianglelist = []
tridata = open("Exam Three Triangles.txt")
x = tridata.readline()
while x != "":
    sides = x.split(",")
    triangle = Triangle(float(sides[0]), float(sides[1]), float(sides[2]))
    trianglelist.append(triangle)
    x = tridata.readline()
for i in range(len(trianglelist)):
    print(trianglelist[i].Type(), trianglelist[i].s1, trianglelist[i].s2, trianglelist[i].s3, trianglelist[i].perimiter(), trianglelist[i].area(), trianglelist[i].angles)