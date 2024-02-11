from turtle import Turtle

FONT = ("arial",18,"normal")
try:
    score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    score = open('highestScore.txt', 'w').write(str(0))
except ValueError:
    score = 0

class Scoreboard(Turtle):

    def __init__(self,lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highScore = score
        self.goto(-580,y=260)
        self.lives = lives
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.highScore} \
        | Lives: {self.lives}", align='left', font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()
 
    def reset(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()
        open('highestScore.txt', 'w').write(str(self.highScore))        
        