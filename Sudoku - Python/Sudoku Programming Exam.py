import turtle
turtle.hideturtle()
grid1 = [[3,4,1,2],[0,0,0,0],[0,0,0,0],[4,2,3,1]] #numbers that go into puzzle
class Sudoku:
    def __init__(self,name):
        self.name = name
    def grid(self): #draw puzzle
        turtle.pu()
        turtle.goto(-200,-200)
        turtle.pd()
        turtle.speed(10)
        turtle.pensize(5)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
        turtle.pensize(1)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(400)
    grid("grid1")
    def labels(self): #draws labels so user can identify where they'd like their value to go 
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(75)
        turtle.right(90)
        turtle.pu()
        turtle.forward(25)
        turtle.pd()
        turtle.write("A", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.left(90)
        turtle.forward(100)
        turtle.pd()
        turtle.write("B", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.forward(100)
        turtle.pd()
        turtle.write("C", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.forward(100)
        turtle.pd()
        turtle.write("D", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(75)
        turtle.pd()
        turtle.write("1", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.forward(100)
        turtle.pd()
        turtle.write("2", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.forward(100)
        turtle.pd()
        turtle.write("3", move=False, align="center", font=("Arial", 28, "normal"))
        turtle.pu()
        turtle.forward(100)
        turtle.pd()
        turtle.write("4", move=False, align="center", font=("Arial", 28, "normal"))
    labels("grid1")
    def numbers(self): #function to put numbers in grid
        turtle.pu()
        turtle.goto(-150,125)
        for i in grid1:# for each element in grid1(a list)
            if i != grid1[0]:#if element is not the first element in grid1(a list)
                turtle.pu()
                turtle.left(180)
                turtle.forward(400)
                turtle.left(90)
                turtle.forward(100)
                turtle.left(90)
            for j in i:# for each element in element in grid1(a list)
                turtle.write(j, move=False, align="center", font=("Arial", 28, "normal"))#write j which is the element in element in grid1(a list)
                turtle.forward(100) #write j then move forward 100       
    numbers("grid1")
    def correct(): #function that checks if puzzle is correct
        rowa = set(grid1[0])# make element 1 in grid1(a list) a set
        rowb = set(grid1[1])# make element 2 in grid1(a list) a set
        rowc = set(grid1[2])# make element 3 in grid1(a list) a set
        rowd = set(grid1[3])# make element 4 in grid1(a list) a set
        return rowa == rowb == rowc == rowd # returns true or false 
    def youwin():# function that tells user they won
        turtle.speed(10)
        turtle.pu()
        turtle.goto(0,300)
        turtle.pd()
        turtle.write("Good Job! You Solved The Puzzle", move = False, align = "center",font = ("Arial",30,"normal"))
    submit = True #should be false but couldn't get it to work. Making it true doesn't allow user to enter submit and check for correctness, but it does let them know that they won if puzzle is correct after they input the last value.
    def user(self):#function that asks user for location and value and changes what is in the puzzle
        x = turtle.textinput("Sudoku Directions","To enter a value in each box enter the row name and column name and value (i.e. 'A1,2' or 'a1,2'), be sure to type it in exactly like the given exmaple. If you fill all the boxes and your answer are correct then I'll let you know you won. If you fill all the boxes and your answers are incorrect I'll keep asking for a location z")
        y = x #y is equal to x so x doesn't change
        y = list(y)#makes y a list
        isthereacomma = False #isthereacomma is equal to false originally so for loop can work
        for i in y: # for each element in y(a list)
            if i == ",": # if a element in y is a comma
                isthereacomma = True # then isthereacomma becomes true           
        if isthereacomma == True: 
            x = x.split(",") #split x(user input) at the comma
            x[1] = int(x[1])#make the second element in x an integer
        if x == "Submit" or x == "submit": # if user inputs the word submit, submit is true
            submit = True
        if x == "": #if user enters nothing then x is fish and it will go through the program and ask a input again
            x = ["fish"]
        if x[0] == "A1" or x[0] == "a1": #if the first element in x is a1 
            turtle.pu()
            turtle.goto(-150,125)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))#write the value given by user which is the second element in x
            grid1[0][0] = x[1] # changes list based on the value given by the user
        elif x[0] == "A2" or x[0] == "a2":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.forward(100)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[0][1] = x[1]
        elif x[0] == "A3" or x[0] == "a3":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.forward(200)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[0][2] = x[1]
        elif x[0] == "A4" or x[0] == "a4":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.forward(300)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[0][3] = x[1]
        elif x[0] == "B1" or x[0] == "b1":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[1][0] = x[1]
        elif x[0] == "B2" or x[0] == "b2":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[1][1] = x[1]
        elif x[0] == "B3" or x[0] == "b3":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(200)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[1][2] = x[1]
        elif x[0] == "B4" or x[0] == "b4":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(300)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[1][3] = x[1]
        elif x[0] == "C1" or x[0] == "c1":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[2][0] = x[1]
        elif x[0] == "C2" or x[0] == "c2":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(100)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[2][1] = x[1]
        elif x[0] == "C3" or x[0] == "c3":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(200)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[2][2] = x[1]
        elif x[0] == "C4" or x[0] == "c4":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(200)
            turtle.left(90)
            turtle.forward(300)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[2][3] = x[1]
        elif x[0] == "D1" or x[0] == "d1":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[3][0] = x[1]
        elif x[0] == "D2" or x[0] == "d2":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(100)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[3][1] = x[1]
        elif x[0] == "D3" or x[0] == "d3":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(200)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[3][2] = x[1]
        elif x[0] == "D4" or x[0] == "d4":
            turtle.pu()
            turtle.goto(-150,125)
            turtle.right(90)
            turtle.forward(300)
            turtle.left(90)
            turtle.forward(300)
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.color("white")
            turtle.circle(30, steps = 4)
            turtle.end_fill()
            turtle.pencolor()
            turtle.color("black")
            turtle.write(x[1], move=False, align="center", font=("Arial", 28, "normal"))
            grid1[3][3] = x[1]
    correctness = False #corretness is equal to false originally so while loop can work
    while correctness == False:# while correctness is false run the funciton user
        user("grid1")
        if submit == True: #if user enters submit
            correctness = correct() #check if the puzzle is right 
        if correctness == True:# if it is right user is notified, if it's wrong another input will be asked for
            youwin()
grid1 = Sudoku("grid1")