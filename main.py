from graphics import *
import random
import math 

class App():

    def __init__(self):
        self.window =  GraphWin(title="Simulation ", width=500, height=500)
        self.window.setCoords(-50,-50,50,50)
        self.window.bind("<Motion>", self.getCoordinates)
        self.grid = Grid(self.window)
        self.info = Text(Point(-0,35), 'No info')
        self.info.draw(self.window)
        self.walker = Walker(self.window, self.info)
    
    def getCoordinates(self, event):
        print(event)
        points = self.window.toWorld(event.x, event.y)
        points = [round(p,2) for p in points]
        print(str(points))
        
    def run(self):
        self.walker.update()
        self.window.getMouse()
        self.window.close()
  

class Grid():
    def __init__(self,window):
        print("Creating Grid")
        self.window = window
        self.x_axis = Line(Point(-50,0), Point(50,0))
        self.y_axis = Line(Point(0,-50), Point(0,50))
        self.drawGrid()

    def drawGrid(self):
        self.x_axis.draw(self.window)
        self.y_axis.draw(self.window)
        for i in range(-50,50):
            newLine = Line(Point(-.5, i),Point(.5,i))
            secondLine = Line(Point(i,.5), Point(i, -.5))
            newLine.draw(self.window)
            secondLine.draw(self.window)
class Walker():

    COLORS = ['black','red','blue', 'snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace',
    'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff',
    'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender',
    'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray',
    'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue',
    'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue',  'blue',
    'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue',
    'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise',
    'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen',
    'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen',
    'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen',
    'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow',
    'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown',
    'indianred', 'saddlebrown', 'sandybrown',]
    def __init__(self,window, info=None):
      
        self.window = window
        self.window.bind("<Return>", self.exit)
        self.info = info
        self.angle = 0
        self.x = 0
        self.y = 0
        self.timer = 0
        self.previousLine = Line(Point(0,0), Point(0,0))
        self.path = []
    def exit(self, event):
        print('Exiting!')
        self.window.exit()
    def walk(self):
        self.angle = random.random()*2*math.pi
        print("Walker is turning at angle: "+str(self.angle))
      
        self.x = round(self.x + math.cos(self.angle),0)
        self.y = round(self.y + math.sin(self.angle),0)
        if self.y == 50 :
            self.y = self.y -1
        elif self.y == -50:
            self.y = self.y +1
        elif self.x == 50:
            self.x = self.x -1 
        elif self.x == -50:
            self.x = self.x + 1
        self.previousLine =  Line(self.previousLine.p2, Point(self.x,self.y))
        self.previousLine.setFill(random.sample(Walker.COLORS,1))
        self.previousLine.draw(self.window)
        print("New Location: "+ str(self.x) + ', ' + str(self.y))
        self.info.setText("Walker is moving to new location: "+ str(self.x) + ', '+  str(self.y))
    def update(self):
        while(self.timer != 10000):
            self.timer +=1
            print(str(self.timer))
            self.walk()
        else:
            print('Walker survived for '+ str(self.timer))



app = App().run()
