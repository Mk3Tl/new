from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,268)
        self.write(f"score: {self.score}",align="center",font=("Courier",18,"normal"))
    

    def increase_scoreboard(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}",align="center",font=("Courier",18,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier",18,"normal"))