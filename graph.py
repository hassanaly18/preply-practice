import turtle

t = turtle.Turtle()
t.speed(10)

screen = turtle.Screen()
screen.title("Pattern Multicolor")
screen.bgcolor("black")
screen.setup(600, 600)

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0,-250)

def move_left():
    paddle.setx(paddle.xcor() - 20)
def move_right():
    paddle.setx(paddle.xcor() + 20)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0,0)
    
ball.dx=5
ball.dy=5

score =0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-280, 260)
pen.write("Score: 0", font=("Arial", 16, "bold"))

while True:
    screen.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx = ball.dx *-1
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = ball.dy *-1
        
    if (ball.ycor() < -230 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy = ball.dy * -1
        
        score = score +1
        pen.clear()
        pen.write(f"Score: {score}", font=("Arial", 16, "bold"))
        
        if score%5==0 and score !=0:
            ball.dx = ball.dx * 1.5
            ball.dy = ball.dy * 1.5
        
         
    
    
    
    
    # turtle.done()

# for i in range(4):
#     t.forward(100)
#     t.right(90)

# turtle.done()    











    
# t = turtle.Turtle()
# t.color("blue")
# t.speed(10)

# d = 10

# screen = turtle.Screen()

# for i in range(40):
#     t.forward(d)
#     t.right(90)
#     d = d+10
    

# t.begin_fill()
# t.circle(50)

# # # for i in range(360): #making a circle
# # #     t.forward(2)
# # #     t.right(1)   
    
# t.end_fill()

turtle.done()    




# while True:
#     t = turtle.Turtle()
#     screen = turtle.Screen()
#     t.forward(100)
#     turtle.done()
    # t.backward(50)
    # t.left(100)
    # t.right(100)