import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.teleport(self.dxpos, self.dypos)
        t.speed(1)
        t.forward(self.dwidth/2)
        t.backward(self.dwidth)
        t.left(90)
        t.forward(self.dheight)
        t.right(90)
        t.forward(self.dwidth)
        t.right(90)
        t.forward(self.dheight)
        t.teleport(self.dxpos, self.dypos)
        t.left(90)

    def newpos(self, xpos, ypos):
        t.teleport(xpos, ypos)

    def cleardisk(self):
        t.color("white")
        self.showdisk()
        t.color("black")

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0,thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        pass

    def pushdisk(self, disk):
        pass

    def popdisk(self):
        pass

d= Disk()
d.showdisk()
d.cleardisk()
t.done()