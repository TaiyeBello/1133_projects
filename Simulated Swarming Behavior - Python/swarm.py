import turtle
from entities import Lights
from entities import Creatures
from configuration import *
import math

class Arena:
    def __init__(self,configuration):
        self.configuration = configuration
        self.arena = turtle.Turtle()
        self.objects = []
        self.lights = []
        self.creatures = []
    def set_lights_creatures(self): #makes lights and creatures
        x = 0 #x and y coord. of the first light
        a = example[0][2].count #all these variables hold information from configuration file
        b = example[0][2].speed
        c = example[0][2].random
        for i in range(a):
            i = Lights(x,x) #creates light object
            i.set_speed(b)
            x += 60 #increases x and y coord. by 60 for the next object
            self.objects.append(i)
            self.lights.append(i)
        y = -300 #x and y coord. of the first creature
        d = example[0][0].count #all these variables hold information from configuration file
        e = example[0][0].space
        f = example[0][0].speed
        for i in range(d):
            i = Creatures(y,y) #creates creature object
            self.objects.append(i)
            self.creatures.append(i)
            y += 60 #increases x and y coord. by 60 for the next object
            i.set_speed(f)
        z = -300 #x and y coord. of the first creature
        h = example[0][1].count #all these variables hold information from configuration file
        j = example[0][1].space
        k = example[0][1].speed
        for i in range(h):
            i = Creatures(z,z) #creates creature object
            self.objects.append(i)
            self.creatures.append(i)
            z += 60 #increases x and y coord. by 60 for the next object
            i.set_speed(k)
        attract1 = example[0][0].attract #wheter creature is attracted or not to light
        attract2 = example[0][1].attract
        while True:
            for el in self.objects: #draws and moves objects and bounces objects off each other
                el.Move(5)
                el.Draw()
                turtle.update()
                self.compare_creatures(j)
                self.compare_lights()
                self.compare_creatures(e)
                self.compare_lights_creatures(10)
            if attract1 or attract2 == True: #attraction funtionality
                for el in self.lights:
                    x = el.return_heading()
                    for el in self.creatures:
                        el.set_heading(x)
            else:
                self.compare_lights_creatures(200)
    def drawArena(self): #draws arena
        self.arena.speed(0)
        self.arena.hideturtle()
        self.arena.pu()
        self.arena.goto(-375,-325)
        self.arena.pd()
        self.arena.color("black","lightblue")
        self.arena.begin_fill()
        self.arena.forward(800)
        self.arena.left(90)
        self.arena.forward(650)
        self.arena.left(90)
        self.arena.forward(800)
        self.arena.left(90)
        self.arena.forward(650)
        self.arena.left(90)
        self.arena.end_fill()
    def compare_creatures(self,space): #bounces creatures off each other
        for i in self.creatures: 
            for j in self.creatures:
                if i == j:
                    pass
                else:
                    
                    distance = (((i.xcor()-j.xcor())**2)+(i.ycor()-j.ycor())**2)**0.5
                    if distance <= space:      
                        i.set_heading(90)
                        j.set_heading(90)
                        
    def compare_lights_creatures(self,space): #function that keeps lights and creatures a certain distance from each other
        for i in self.lights: 
            for j in self.creatures:
                if i == j:
                    pass
                else:
                    
                    distance = (((i.xcor()-j.xcor())**2)+(i.ycor()-j.ycor())**2)**0.5
                    if distance <= space:
                        i.set_heading(45)
                        j.set_heading(45)
    def compare_lights(self): #bounces lights off each other
        for i in self.lights: 
            for j in self.lights:
                if i == j:
                    pass
                else:
                    distance = (((i.xcor()-j.xcor())**2)+(i.ycor()-j.ycor())**2)**0.5
                    if distance <= 60:
                        i.set_heading(30)
                        j.set_heading(30)
        
def main():
    screen = turtle.getscreen()
    screen.setup(700,700)
    draw = Arena(example[0])
    draw.drawArena()
    turtle.speed(10)
    turtle.tracer(0,0)
    draw.set_lights_creatures()

if __name__ == "__main__" :

  main()
