import turtle

t = turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.color("red")


def triangle(sidelength):
  for side in range(3):
    t.fd(sidelength)
    t.rt(120)
  
triangle(100)

