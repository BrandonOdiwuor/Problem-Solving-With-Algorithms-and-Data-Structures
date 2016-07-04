import turtle

t = turtle.Turtle()
my_win = turtle.Screen()

def drawspiral(t, line_length):
  if line_length > 0:
    t.forward(line_length)
    t.right(90)
    drawspiral(t, line_length - 5)  

drawspiral(t, 400)
my_win.exitonclick()

