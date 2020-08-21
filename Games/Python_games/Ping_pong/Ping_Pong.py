import turtle



wn = turtle.Screen()
wn.title("Pong By @Roboleo")
wn.bgcolor("black")
wn.setup(width=900, height=600)
wn.tracer(0)


# Score

score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("gray")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {0}  Player B: {1}".format(score_a, score_b), align= "center", font= ("Courier", 24, "normal"))

# Pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(440, 270)
pen2.write("Velocidade: {}".format(ball.dx), align= "right", font= ("Courier", 12, "normal"))

#Special_indicator
    # Spec A Title
spec_a_title = turtle.Turtle()
spec_a_title.speed(0)
spec_a_title.penup()
spec_a_title.color("white")
spec_a_title.hideturtle()
spec_a_title.goto(-440, -270)
spec_a_title.write("Special: Press 'd'", align="left", font=("Courier", 10, "normal"))
    
    # Spec B Title
spec_b_title = turtle.Turtle()
spec_b_title.speed(0)
spec_b_title.penup()
spec_b_title.color("white")
spec_b_title.hideturtle()
spec_b_title.goto(440, -270)
spec_b_title.write("Special: Press 'Arrow Left'", align="right", font=("Courier", 10, "normal"))

    # Spec A indicator
n_spec = 2
qtd_spec = {'a':n_spec, 'b':n_spec}

spec_a_vec = []
for i in range(n_spec):
    spec_a_vec.append(turtle.Turtle())
    spec_a_vec[i].speed(0)
    spec_a_vec[i].penup()
    spec_a_vec[i].shape("circle")
    spec_a_vec[i].color("red")
    spec_a_vec[i].shapesize(stretch_wid=.5, stretch_len=.5)
    spec_a_vec[i].goto(-420+15*i, -280)

    # Spec B indicator

spec_b_vec = []
for i in range(n_spec):
    spec_b_vec.append(turtle.Turtle())
    spec_b_vec[i].speed(0)
    spec_b_vec[i].penup()
    spec_b_vec[i].shape("circle")
    spec_b_vec[i].color("red")
    spec_b_vec[i].shapesize(stretch_wid=.5, stretch_len=.5)
    spec_b_vec[i].goto(420-15*i, -280)

# Function

n=3
move = 5
def paddle_a_up():
    y = paddle_a.ycor()
    for i in range(n):    
        y += move
        paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_a.ycor()
    for i in range(n):
        y -= move
        paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor()
    for i in range(n):
        y += move
        paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()
    for i in range(n):
        y -= move
        paddle_b.sety(y) 

def gain_spec(spec_indicator, user):
    if qtd_spec[user] < n_spec:
        spec_indicator[qtd_spec[user]].color("red")
        qtd_spec[user] += 1

def used_spec(spec_indicator, user):
    if qtd_spec[user] > 0:
        qtd_spec[user] -= 1
        spec_indicator[qtd_spec[user]].color("blue")
        return True
    else:
        return False

def special_b():
    if ball.xcor() > 360 and ball.xcor() < 400 and used_spec(spec_b_vec, 'b') and ball.dx < 0:
        ball.color("red")
        ball.dx *= 4
        pen2.clear()
        pen2.write("Velocidade: {}".format(ball.dx), align= "right", font= ("Courier", 12, "normal"))
    else:
        pass

def special_a():
    if ball.xcor() < -360 and ball.xcor() > -400 and used_spec(spec_a_vec, 'a') and ball.dx > 0:
        ball.color("red")
        ball.dx *= 4
        pen2.clear()
        pen2.write("Velocidade: {}".format(ball.dx), align= "right", font= ("Courier", 12, "normal"))
    else:
        pass

def normal():
    ball.dx *= 0.5
    if ball.dx < 0.11:
        ball.dx = 0.1
        ball.color("white")
    elif ball.dx < 0.25:
        ball.color('yellow')
    pen2.clear()
    pen2.write("Velocidade: {}".format(ball.dx), align= "right", font= ("Courier", 12, "normal"))
    
#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

wn.onkeypress(special_a, "d")
wn.onkeypress(special_b, "Left")

#Main game Loop

while True:
    wn.update()
    spec_b_title.clear()
    spec_b_title.write("Special {0}: Press 'Arrow Left'".format(qtd_spec['b']), align="right", font=("Courier", 10, "normal"))

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking ball

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        
    if ball.xcor() > 440:
        ball.goto(0, 0)
        normal()
        ball.dx *=-0.5
        score_a += 1
        pen.clear()
        pen.write("Player A: {0}  Player B: {1}".format(score_a, score_b), align= "center", font= ("Courier", 24, "normal"))

    if ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A: {0}  Player B: {1}".format(score_a, score_b), align= "center", font= ("Courier", 24, "normal"))

    #Contact Check Ball and Paddle
    if ball.xcor() > 375:
        if (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(375)
            ball.dx *= -1
            gain_spec(spec_b_vec, 'b')
            if ball.dx > 0.11 or ball.dx  < -0.11:
                normal()
                 
    
    if ball.xcor() < -375:

        if (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-375)
            ball.dx *= -1
            gain_spec(spec_a_vec, 'a')
            if ball.dx > 0.11 or ball.dx  < -0.11:
                normal()