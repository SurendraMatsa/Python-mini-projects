from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        with open("data.text") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write("Snake Game" ,align = ALIGNMENT, font = (FONT, 21, 'normal'))
        self.goto(0, 250)
        self.write(f'High Score : {self.high_score} Score : {self.score}', align = ALIGNMENT, font=(FONT, 16, 'normal'))
        self.goto(-300,250)
        self.write("__________________________________________________________________________________________________")
        self.goto(-300,246)
        self.write("__________________________________________________________________________________________________")
        self.goto(-300,-274)
        self.write("__________________________________________________________________________________________________")
        self.goto(180,-290)
        self.write("Developer : Surendra Matsa" ,align = ALIGNMENT, font = (FONT, 10, 'normal'))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.text", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def score_increase(self):
        self.score +=1
        self.update_score()
        