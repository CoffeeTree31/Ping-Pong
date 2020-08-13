import turtle, random

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor('black')
window.tracer(3)


border = turtle.Turtle()
border.color('green')
border.speed(0)
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.right(90)
for i in range(25):
    border.forward(24)
    if border.isvisible():
        border.hideturtle()
        border.up()
    else:
        border.showturtle()
        border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.speed(0)
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_len=1, stretch_wid=4)
rocket_a.up()
rocket_a.goto(-450, 0)

rocket_b = turtle.Turtle()
rocket_b.speed(0)
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_len=1, stretch_wid=4)
rocket_b.up()
rocket_b.goto(450, 0)

def move_up_a():
    y = rocket_a.ycor() + 10
    if y > 260:
        y = 260
    rocket_a.sety(y)
def move_down_a():
    y = rocket_a.ycor() - 10
    if y < -260:
        y = -260
    rocket_a.sety(y)
def move_up_b():
    yb = rocket_b.ycor() + 10
    if yb > 260:
        yb = 260
    rocket_b.sety(yb)
def move_down_b():
    yb = rocket_b.ycor() - 10
    if yb < -260:
        yb = -260
    rocket_b.sety(yb)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()
ball.dx = -0.7
ball.dy = -0.7
ball.speed(0)
ball.sety(random.randint(-150, 150))


window.update()

speed = [0.6, 0.7, 0.75, -0.6, -0.7, -0.75]

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 290 or ball.ycor()<= -290:
        ball.dy = -ball.dy
    if ball.xcor() >= 490 or ball.xcor() <= -490:
        ball.goto(0, 0)
        rocket_a.sety(0)
        rocket_b.sety(0)
        ball.dx = random.choice(speed)
        ball.dy = random.choice(speed)
    if ball.ycor() >= rocket_a.ycor() - 50 and ball.ycor() <= rocket_a.ycor() + 50 and ball.xcor() >= rocket_a.xcor() - 5 and ball.xcor() <= rocket_a.xcor() + 5:
        ball.dx = -ball.dx
    if ball.ycor() >= rocket_b.ycor() - 50 and ball.ycor() <= rocket_b.ycor() + 50 and ball.xcor() >= rocket_b.xcor() - 5 and ball.xcor() <= rocket_b.xcor() + 5:
        ball.dx = -ball.dx
    window.listen()
    window.onkeypress(move_down_a, "s")
    window.onkeypress(move_up_a, "w")
    window.onkeypress(move_down_b, "Down")
    window.onkeypress(move_up_b, 'Up')
    window.onkey(move_down_a, "s")
    window.onkey(move_up_a, "w")
    window.onkey(move_down_b, "Down")
    window.onkey(move_up_b, 'Up')



