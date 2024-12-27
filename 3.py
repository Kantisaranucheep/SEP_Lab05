import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40, color="blue"):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.color = color

    def showdisk(self):
        t.penup()
        t.goto(self.dxpos - self.dwidth / 2, self.dypos)  # Position to start drawing
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        for _ in range(2):
            t.forward(self.dwidth)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)
        t.end_fill()
        t.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        t.color("white")
        self.showdisk()
        t.color("black")


class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100, color="brown"):
        self.pname = name
        self.stack = [] 
        self.toppos = ypos
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        self.color = color

    def showpole(self):
        t.penup()
        t.goto(self.pxpos - self.pthick / 2, self.pypos)  
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        for _ in range(2):
            t.forward(self.pthick)
            t.left(90)
            t.forward(self.plength)
            t.left(90)
        t.end_fill()
        t.penup()

    def pushdisk(self, disk):
        if self.stack:
            disk.newpos(self.pxpos, self.toppos + 20)
            self.toppos += disk.dheight  
        else:
            disk.newpos(self.pxpos, self.pypos + 20)
            self.toppos = self.pypos + disk.dheight
        self.stack.append(disk)  
        disk.showdisk() 

    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            disk.cleardisk()  
            if self.stack:
                self.toppos -= disk.dheight
            else:
                self.toppos = self.pypos
            return disk
        return None  


class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0, color="darkgreen")
        self.workspacep = Pole(workspace, 150, 0, color="darkred")
        self.destinationp = Pole(destination, 300, 0, color="darkblue")

        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        for i in range(n):
            disk_color = colors[i % len(colors)]
            disk = Disk(f"d{i+1}", 0, i * 20, 20, (n-i) * 30, color=disk_color)
            self.startp.pushdisk(disk)

    def move_disk(self, start, destination):
        disk = start.popdisk()
        if disk:
            destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)


t.speed(0) 
t.bgcolor("white")

h = Hanoi()
h.solve()

t.done()
