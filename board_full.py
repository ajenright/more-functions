from turtle import *

# Square

def square(size, sq_color):
    # Copy your square function from Exercise 1 here
    pass

def next_color(current_color):
    # Copy your next_color function from Exercise 4 here
    pass

# For Exercise 5, Only modify this function
# This function draws a row of squares.  `number` is the number of squares across it should draw. Each square is of size sq_size.
# The colors start with sq_color, and then should be chosen by next_color()
def row(number, sq_size, sq_color):
    pass
    

#### Do not modify anything below this line before Exercise 8
# Draw board

penup()
goto(-200, 200)
pendown()
square(400, "black")
first_color = "red"
for i in range(8):
    row(8, 400/8, first_color)
    first_color = next_color(first_color)

    penup()
    back(400)
    right(90)
    forward(400/8)
    left(90)
    pendown()

penup()
goto(-200, 200)
pendown()






done()
