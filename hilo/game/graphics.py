import turtle

def main():
    _t = turtle.Turtle()

def draw_spade(_t):
        draw_rectangle(_t, 0, 0, 50, 10, 0, "black", "black")
        draw_circle(_t, 0, 50, 25, "black", "black")
        draw_triangle(_t, 0, 100, 25, "black", "black", 90)
    
def draw_heart(_t):
    draw_circle(_t, -25, 50, 25, "red", "red")
    draw_circle(_t, 25, 50, 25, "red", "red")
    draw_triangle(_t, 0, 100, 25, "red", "red", 270)

def draw_clubs(_t):
    draw_rectangle(_t, 0, 0, 50, 10, 0, "black", "black")
    draw_circle(_t, -5, 50, 5, "black", "black")
    draw_circle(_t, 0, 55, 5, "black", "black")
    draw_circle(_t, 5, 50, 5, "black", "black")

def draw_diamond(_t):
    draw_triangle(_t, 0, 100, 25, "red", "red", 270)
    draw_triangle(_t, 0, 100, 25, "red", "red", 90)
    
def draw_triangle(_t, _x, _y, side, fillcolor, pencolor, tilt):
    """
    Atomic shape used to create the triforce used on the shield.
    _x, and _y are for coordinates
    side is used for the triangle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.up()
    _t.goto(_x, _y)
    _t.setheading(tilt)
    _t.fillcolor(fillcolor)
    _t.down()
    _t.begin_fill()
    for _i in range(3):
        _t.forward(side)
        _t.left(120)
    _t.end_fill()
    _t.up()
def draw_circle(_t, _x, _y, radius, fillcolor, pencolor):
    """
    This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
    _x, and _y are for coordinates
    radius is used for the circle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    _t.up()
    _t.goto(_x,_y)
    _t.down()
    _t.circle(radius)
    _t.end_fill()
    _t.speed(0)
def draw_rectangle(_t, _x, _y, height, width, tilt, fillcolor, pencolor):
    """
    _x, and _y are for coordinates
    height and width are used for the rectangle size
    tilt is for the direction that the rectangle is tilted or not.
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.setheading(tilt)
    _t.up()
    _t.goto(_x, _y)
    _t.down()
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    for _i in range(2):
        _t.forward(width)
        _t.left(90)
        _t.forward(height)
        _t.left(90)

    _t.right(90)
    _t.end_fill()
    _t.up()