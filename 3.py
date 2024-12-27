class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dexpos = xpos
        self.dypos = ypos
        self.dheigt = height
        self.dwidth = width

    def showdisk(self):
        pass

    def newpos(self, xpos, ypos):
        pass

    def cleardisk(self):
        pass

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
    