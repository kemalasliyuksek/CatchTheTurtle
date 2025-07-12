import turtle

from random import randint

# GAME BOARD
game_board = turtle.Screen()
game_board.bgcolor("lightblue")
game_board.setup(width=800, height=600)
game_board.title("Catch The Turtle")

# SCORE
score = 0
score_text = turtle.Turtle()
score_text.hideturtle()
score_text.penup()
score_text.goto(0, 250)
score_text.write(f"Score: {score}", move=False, align='center', font=('Arial', 25, 'bold'))

# COUNTDOWN
game_time = 20
time_text = turtle.Turtle()
time_text.hideturtle()
time_text.penup()
time_text.goto(0, 220)
time_text.write(f"Remaining Time: {game_time}", align='center', font=('Arial', 18, 'normal'))

# TURTLE
turtle_object = turtle.Turtle()
turtle_object.shape("turtle")
turtle_object.color("red")
turtle_object.shapesize(stretch_wid=2, stretch_len=2, outline=1)

def hit_turtle(x, y):
    global score, game_started
    score += 1
    score_text.clear()
    score_text.write(f"Score: {score}", align='center', font=('Arial', 25, 'bold'))

    if not game_started:
        start_game()

def start_game():
    global game_started
    if not game_started:
        game_started = True
        countdown()
        move_random()

def finish_game():
    game_board.clear()
    finish_text = turtle.Turtle()
    finish_text.hideturtle()
    finish_text.penup()
    finish_text.write("Game Over", align="center", font=("Courier", 24, "bold"))
    finish_score = turtle.Turtle()
    finish_score.hideturtle()
    finish_score.penup()
    finish_score.goto(0, -30)
    finish_score.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))

def countdown():
    global game_time
    if game_time > 0:
        game_time -= 1
        time_text.clear()
        time_text.write(f"Remaining Time: {game_time}", align='center', font=('Arial', 18, 'normal'))
        game_board.ontimer(countdown, 1000)
    else:
        finish_game()

def move_random():
    x = randint(-200, 200)
    y = randint(-200, 100)
    turtle_object.penup()
    turtle_object.hideturtle()
    turtle_object.goto(x, y)
    turtle_object.showturtle()
    turtle_object.pendown()
    print(turtle_object.position())

    if game_time != 0:
        game_board.ontimer(move_random, 750)

game_started = False

turtle_object.onclick(hit_turtle, 1, True)

game_board.mainloop()