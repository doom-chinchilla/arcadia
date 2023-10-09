import turtle

WN = turtle.Screen()
WN.title("Pong!")
WN.bgcolor("black")
WN.setup(width=800, height=600)
WN.tracer(0)

# init variables to keep track of the score
SCORE_PA = 0
SCORE_PB = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# ball logic
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# todo: allow player's to write their names
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

# move the paddle functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 
    paddle_a.sety(y)

# keyboard binding
WN.listen()
WN.onkeypress(paddle_a_up,"w")
WN.onkeypress(paddle_a_down,"s")
WN.onkeypress(paddle_b_up,"Up")
WN.onkeypress(paddle_b_down,"DoWN")

# start main game loop
while True:
    WN.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        SCORE_PA += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}"\
                  .format(SCORE_PA, SCORE_PB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        SCORE_PB += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}"\
                  .format(SCORE_PA, SCORE_PB), align="center", font=("Courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
        (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) \
        and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
