# Language: Python
# Source packages used: Turtle

import turtle as graphics

count_a = 0
count_b = 0

wn = graphics.Screen()
wn.title("Pong by mja")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A

paddle_a = graphics.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = graphics.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = graphics.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen

pen = graphics.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Functions

def movePaddle(paddleC, dir):
    y = paddleC.ycor()
    if dir == "up":
        y += 20
    elif dir == "down":
        y -= 20
    paddleC.sety(y)

# Functions without parameters

def paddle_a_up():
    movePaddle(paddle_a,"up")

def paddle_a_down():
    movePaddle(paddle_a,"down")

def paddle_b_up():
    movePaddle(paddle_b,"up")

def paddle_b_down():
    movePaddle(paddle_b,"down")


# Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop here

while True: 
    wn.update()

    # Moving Ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        count_a =+ 1
        pen.write("Player A: " + str(count_a) + " Player B: " + str(count_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= - 1

    if ball.xcor() < -390:
        count_b =+ 1
        pen.write("Player A: " + str(count_a) + " Player B: " + str(count_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= - 1

    # Paddle and Ball collisions

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < (paddle_b.ycor() + 40) and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= - 1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < (paddle_a.ycor() + 40) and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= - 1