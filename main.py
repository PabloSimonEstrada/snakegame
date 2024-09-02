from turtle import Screen
import time
from score import Score
from food import Food
from snake_module import Snake
screen = Screen()
screen.setup(width=600,height= 600)
screen.bgcolor("black")

screen.tracer(0)

game_is_on = True

snake = Snake()
score = Score()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.score += 1
        score.show_new_score()
        snake.extend()

    elif snake.segments[0].xcor() > 290 or  snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or  snake.segments[0].ycor() < -290:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 15:
            score.reset()
            snake.reset()




screen.title("Snake Game")


screen.exitonclick()