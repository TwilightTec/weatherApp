from turtle import *
mickey = Turtle()
mickey.shape("turtle")
mickey.color("pink")
mickey.forward(100)
mickey.left(90)
mickey.forward(100)
mickey.left(90)
mickey.forward(100)
mickey.left(90)
mickey.forward(100)
mickey.left(90)
#loop
for a in range(4):
    mickey.forward(100)
    mickey.left(90)
def square():
    mickey.begin_fill()
    for a in range(4):
        mickey.forward(100)
        mickey.left(90)
    mickey.end_fill()
square()
colorOne = "cadetblue"
colorTwo = "chartreuse"
colorThree = "cyan"
colorFour = "firebrick"
colorFive = "paleturquoise"
colorSix = "limegreen"
size = 200
for a in range(6) :
    if a == 0:
        square(size, colorOne)
    if a == 1:
        square(size,colorTwo)
    if a == 2:
        square(size,colorThree)
    if a == 3:
        square(size, colorFour)
    if a == 4:
        square(size, colorFive)
    if a == 5:
        square(size, colorSix)
    
    
    #try to th e next colors on your own
    #write code for the next three colors
    


