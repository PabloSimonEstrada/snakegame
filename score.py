from turtle import Turtle

with open("../../Desktop/high_score.txt") as h_s:
    high_score_text = h_s.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high_score_text)
        self.show_new_score()

    def show_new_score(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.pencolor("white")
        self.write(f"Score {self.score} High Score {self.high_score}", align="center", font=("Arial", 22, "normal"))
        self.penup()
        self.hideturtle()

    """def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.pencolor("white")
        self.write("GAME OVER", align="center", font=("Arial", 29, "normal"))
        self.penup()
        self.hideturtle()"""

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/estra/Desktop/high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
            self.score = 0
            self.show_new_score()
