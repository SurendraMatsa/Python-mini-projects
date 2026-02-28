from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard



screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)


snake = Snake()
screen.listen()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.score_increase()
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() <-300 or snake.head.ycor() > 240 or snake.head.ycor() < -270 :
        scoreboard.reset()
        snake.reset()

    for seg in snake.segment[1:]:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10 :
            scoreboard.reset()
            snake.reset()
        


screen.exitonclick()