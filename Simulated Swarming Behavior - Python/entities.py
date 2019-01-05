import turtle
import math
import random

class Creatures: #creates creatures
    def __init__(self,x,y):
        self.radius = 10
        self.x = x
        self.y = y
        self.heading = random.randint(0,100)#using random so creatures go in different dicrections
        self.creature = turtle.Turtle()
        self.creature.hideturtle()
        self.speed = 1 #determines speed of creature
    def xcor(self):
        return int(self.x)
    def ycor(self):
        return int(self.y)
    def Draw(self): #draws creatures
        self.creature.clear()
        self.creature.hideturtle()
        self.creature.penup()
        self.creature.goto(self.x,self.y) 
        self.creature.dot(self.radius*2) #creates body of creature
        deltaX = self.radius*math.cos(self.heading)
        deltaY = self.radius*math.sin(self.heading)
        self.creature.goto(self.x+deltaX,self.y+deltaY)#goes to the point where heading with be drawn
        self.creature.dot(self.radius*.75) #draws the heading of the creature
    def Move(self,dist): #moves creature 
        distance = dist*self.speed #how fast the creature will move
        deltaX = distance*math.cos(self.heading)
        deltaY = distance*math.sin(self.heading)
        self.x += deltaX #changes the position of the creature
        self.y += deltaY
        if self.x <= -375 or self.x >= 425 or self.y <= -325 or self.y >= 325: #used so creatures and lights can bounce off the wall
            self.heading += 90
    def set_heading(self,x):
        self.heading += x
    def set_speed(self,x):
        self.speed = x
    def return_heading(self):
        return self.heading
class Lights(Creatures):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.color = "yellow"
        self.lights = turtle.Turtle()
    def Draw(self): #draws a light
        self.lights.clear()
        self.lights.hideturtle()
        self.lights.penup()
        self.lights.goto(self.x,self.y)
        self.lights.dot(self.radius*2,self.color)
        deltaX = self.radius*math.cos(self.heading)
        deltaY = self.radius*math.sin(self.heading)
        self.lights.goto(self.x+deltaX,self.y+deltaY)

