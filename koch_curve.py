from turtle import *


def turtle_drawing():
    t = Turtle()
    s = Screen()

    s.setup(width=900, height=500, startx=50, starty=250)
    s.bgcolor('#222222')

    t.speed(50)
    t.color('grey')
    t.pensize(1.2)

    def draw_curve(length, deep):
        if deep == 0:
            t.forward(length)
        else:
            for i in [60, -120, 60, 0]:
                draw_curve(length / 3, deep - 1)
                t.left(i)

    draw_curve(400, 4)
    s.exitonclick()


if __name__ == '__main__':
    turtle_drawing()
