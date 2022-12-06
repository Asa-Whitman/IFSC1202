#coding by Asa Whitman
class Sketch():
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = "U"
        self.pen = "U"
        self.canvas = []
        for i in range(self.size):
            self.canvas.append([' '] * self.size)
        return
    
    

    def printsketch(self):
        print("+" + ("-" * self.size) + "+")
        for i in range(self.size - 1, -1, -1):
            print("|", sep="", end="")
            # print a row of the canvas
            for j in range(self.size):
                print(self.canvas[i][j], sep="", end="")
            print("|", sep="", end="")
            print()
        print("+" + ("-" * self.size) + "+")
        print("X =", self.xpos, " Y =", self.ypos, " Direction =", self.direction)

    def penup(self):
        self.pen = "U"

    def pendown(self):
        self.pen = "D"
    
    def turnright(self):
        if self.direction == "U":
            self.direction = "R"    #up to right
        elif self.direction =="L":
            self.direction = "U"    #left to up
        elif self.direction == "D":
            self.direction = "L"    #down to left
        elif self.direction == "R":
            self.direction = "D"
    def turnleft(self):
        if self.direction == "U":
            self.direction = "L"
        elif self.direction =="R":
            self.direction = "U"
        elif self.direction == "D":
            self.direction = "R"
        elif self.direction == "L":
            self.direction = "D"
        
    
    def move(self, distance):
        #UP
        if self.direction == "U":
            newpos = self.xpos + distance
            if newpos >= self.size:
                newpos = self.size - 1
            if self.pen == "D":
                for i in range(self.xpos, newpos):
                    self.canvas[i][self.ypos] = "*"
            self.xpos = newpos
        #DOWN
        elif self.direction == "D":
            newpos = self.xpos - distance
            if newpos < 0:
                    newpos = 0
            if self.pen == "D":
                for i in range(self.xpos, newpos - 1, -1):
                    self.canvas[i][self.ypos] = "*"
            self.xpos = newpos
        #RIGHT
        elif self.direction == "R":
            newpos = self.ypos + distance
            if newpos >= self.size:
                newpos = self.size - 1
            if self.pen == "D":
                for i in range(self.ypos, newpos + 1):
                    self.canvas[self.xpos][i] = "*"
            self.ypos = newpos
        #LEFT
        elif self.direction == "L":
            newpos = self.ypos - distance
            if newpos < 0:
                newpos = 0
            if self.pen == "D":
                for i in range(newpos, self.ypos):
                    self.canvas[self.xpos][i] = "*"
            self.ypos = newpos
                    
Cshape = open("Cshape.txt")
command = Cshape.readline()
mysketch = Sketch(int(command))
command = Cshape.readline()
while command != "":
    commandvalues=command.split(",")
    command1 = commandvalues[0].strip()
    if command1 == "1":
        mysketch.penup()
    if command1 == "2":
        mysketch.pendown()
    if command1 == "3":
        mysketch.turnright()
    if command1 == "4":
        mysketch.turnleft()
    if command1 == "5":
        mysketch.move(int(commandvalues[1]))
    if command1 == "6":
        mysketch.printsketch()
    command = Cshape.readline()
Cshape.close()

#mysketch = Sketch(20)
#mysketch.penup()
#mysketch.move(15)   #UP
#mysketch.turnright()
#mysketch.move(5)    #RIGHT
#mysketch.pendown()
#mysketch.move(10)   #RIGHT
#mysketch.turnright()
#mysketch.move(2)    #DOWN
#mysketch.turnright()
#mysketch.move(7)    #LEFT
#mysketch.turnleft()
#mysketch.move(7)    #DOWN
#mysketch.turnleft()
#mysketch.move(7)    #RIGHT
#mysketch.turnright()
#mysketch.move(2)    #DOWN
#mysketch.turnright()
#mysketch.move(10)   #LEFT
#mysketch.turnright()
#mysketch.move(12)
#mysketch.printsketch()