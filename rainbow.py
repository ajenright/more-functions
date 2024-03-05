from turtle import *

def next_color(current_color):
    return "orange"


### Do not modify anything below this line

def bar(bar_color):
    color(bar_color)
    begin_fill()
    forward(200)
    right(90)
    forward(30)
    right(90)
    forward(200)
    right(90)
    forward(30)
    right(90)
    end_fill()

### Main code that draws a rainbow

rainbow_color = "red"
for i in range(7):
    bar(rainbow_color)
    right(90); forward(30); left(90)
    rainbow_color = next_color(rainbow_color)

done()
    
