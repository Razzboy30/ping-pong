from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(800,600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.moveL, "w")
screen.onkey(l_paddle.moveR, "s")
screen.onkey(r_paddle.moveL, "Up")
screen.onkey(r_paddle.moveR, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # if r player miss ball
    if ball.xcor() > 380:
        ball.start_over()
        score.l_scoree()
        
    # l player
    if ball.xcor() < -380:
        ball.start_over()
        score.r_scoree()



screen.exitonclick()

