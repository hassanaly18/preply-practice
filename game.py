import turtle
import random
import winsound
import time

level = 1
fallSpeed = 1
count = 3

#screen
screen = turtle.Screen() #making the new screen
screen.title("Catch the Flakes!") #canging the title
screen.bgcolor("skyblue")         #change the background color of screen
screen.setup(width=600, height=600) #change screen size
screen.tracer(0)

#santa object
santa = turtle.Turtle()  #making santa object
santa.shape("turtle")    #giving him shape of turtle
santa.color("red")       #changing color of santa
santa.penup()            #removing the pen line
santa.goto(0, -240)      #positioning the santa
santa.speed(0)

#message
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.color("red")

#obstacle
obstacle = turtle.Turtle()
obstacle.shape("square") 
obstacle.color("green") 
obstacle.penup()
obstacle.goto(random.randint(-280, 280), random.randint(100, 300))

#countdown
countdown = turtle.Turtle()
countdown.hideturtle()
countdown.penup()
countdown.color("red")
countdown.goto(0,0)

#functions
def move_left():
    x = santa.xcor()
    if x > -280:
        santa.setx(x-20)
        
def move_right():
    x = santa.xcor()
    if x < 280:
        santa.setx(x+20)
        
def collision(a,b):
    if a.distance(b) < 20:
        playsound()
        
    return a.distance(b) < 20   

def playsound():
    winsound.PlaySound("SystemAsterik", winsound.SND_ASYNC)
    
def game_over(text):
    global game_running
    game_running = False
    
    message.clear()
    message.goto(0,0)
    message.write(text + "\n\nPress R to Restart", align="center", font=("Arial", 28, "bold"))
    
def restart_game():
    global score, start_time, game_running, level, fallSpeed
    
    message.clear()
    
    score = 0
    level = 1
    fallSpeed = 1
    start_time = time.time()
    
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))
    
    level_writer.clear()
    level_writer.write(f"Level: {level}", font=("Arial", 16, "bold"))
    
    #reset position of turtle
    santa.goto(0, -240)
    
    obstacle.goto(random.randint(-280, 280), random.randint(150, 300))
    
    for snow in snowflakes:
        snow.goto(random.randint(-280, 280), random.randint(100, 300))
    
    start_countdown()
    game_running = True    
    
def start_countdown():
    global count
    count = 3
    countdown.clear()
    show_countdown() 

def show_countdown():
    global count
    countdown.clear()
    
    if count>0:
        countdown.write(count, align="center", font=("Arial", 50, "bold"))   
        count = count -1
        screen.ontimer(clear_countdown(), 5000)   

def clear_countdown():
    countdown.clear()

#Notice keyboard buttons
screen.listen()
screen.onkeypress(move_left, "Left") #left keyboard button
screen.onkeypress(move_right, "Right") #right keyboard button
screen.onkey(restart_game,"r")
screen.onkey(restart_game,"R")

#making the snowflakes
snowflakes = []
for i in range(10):
    snow = turtle.Turtle()
    snow.shape("circle")   #snowflake shape
    snow.color("white")
    snow.penup()
    snow.speed(0)
    snow.goto(random.randint(-280, 280), random.randint(100, 300))
    snowflakes.append(snow)
    
#Scoring 
score = 0

score_writer = turtle.Turtle()
score_writer.hideturtle()      #hiding turtle shape
score_writer.penup()
score_writer.goto(-280, 260)   #positioning score on top left
score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))  #writing text in score 

#Level
level_writer = turtle.Turtle()
level_writer.hideturtle()      #hiding turtle shape
level_writer.penup()
level_writer.goto(180, 260)   #positioning score on top right
level_writer.write(f"Level: {level}", font=("Arial", 16, "bold"))  #writing text in score 

start_time = time.time()  
time_limit = 30 

game_running = True

#loop to keep seeing the screen
# while True:
#     screen.update()
    
#     if not game_running:
#         continue
        
#     obs_y = obstacle.ycor() - fallSpeed
#     obstacle.sety(obs_y)
    
#     for snow in snowflakes:
        
#         #moving snowflakes down
#         y = snow.ycor()
#         y = y-fallSpeed        #speed of flakes coming down
#         snow.sety(y)
    
#         #reset snowflakes from the top
#         if y < -300:
#             snow.goto(random.randint(-280, 280), random.randint(100, 300))
        
#         #if santa touches the grinch, stop game
#         if santa.distance(obstacle) < 20:
#             print("Game over")
#             game_over(f"You touched the Grinch,\n You LOST! \n{score}")    
            
#         if collision(snow, santa):
#             score = score+1
#             score_writer.clear()
#             score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))
            
#             #stop the game if score is 20 before 30 seconds
#             if score >= 20: 
#                 print("You win")
#                 game_over(f"You WON | Score:{score}")
            
#             if score % 10 == 0:
#                 level = level+1
#                 fallSpeed = fallSpeed + 1
                
#                 level_writer.clear()
#                 level_writer.write(f"Level: {level}", font=("Arial", 16, "bold"))
            
#             snow.goto(random.randint(-280, 280), random.randint(150, 300))   
#             obstacle.goto(random.randint(-280, 280), random.randint(150, 300)) 
    
#     elapsed = time.time() - start_time
    
#     if elapsed > time_limit:
#         print("Time is up!")
#         game_over(f"Your time is up!\nScore: {score}")           
    
while True:
    screen.update()
    
    if not game_running:
        continue
    
    obs_y = obstacle.ycor() - fallSpeed
    obstacle.sety(obs_y)
    
    if obstacle.ycor() < -300:
        obstacle.goto(random.randint(-280, 280), random.randint(150, 300))
    
    for snow in snowflakes:
        snow.sety(snow.ycor() - fallSpeed)
        
        if snow.ycor() < -300:
            snow.goto(random.randint(-280, 280), random.randint(150, 300))
            
        if collision(snow, santa):
            score = score+1
            score_writer.clear()
            score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))
            snow.goto(random.randint(-280, 280), random.randint(150, 300))
        
        # obstacle.goto(random.randint(-280, 280), random.randint(150, 300))        
        
        if santa.distance(obstacle) < 20 and game_running:
            game_over(f"You touched the grinch!\nSore: {score}")
            
        if time.time() - start_time > time_limit:
            game_over(f"Time is up!\nScore: {score}")    
                        
