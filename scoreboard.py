from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("consolas", 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=280)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

    