from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0) , (-40,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("circle")
        snake.penup()
        snake.color('Green')
        snake.goto(position)
        self.segment.append(snake)
    
    def extent(self):
        self.add_segment(self.segment[-1].position())
    
    def reset(self):
        for segm in self.segment:
            segm.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1 ):
            x = self.segment[seg_num - 1].xcor()
            y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x,y)
        self.segment[0].forward(MOVE)
        
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
            
