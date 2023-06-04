from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos) -> None:
        super().__init__()
        self.pos = pos
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.goto(pos)
        
    def moveL(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def moveR(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
        