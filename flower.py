import turtle
def flower():
    t = turtle.Turtle()
    t.color("blue")
    t.shape("turtle")
    t.speed(10)
    for i in range(45):
        for j in range(2):
            t.forward(100)
            t.right(45)
            t.forward(100)
            t.right(135)
        t.right(8)
    t.right(90)
    t.forward(300)
flower()
