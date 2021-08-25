import turtle
colors=["red", "blue", "green", "yellow"]
l1=[30, 40, 50, 60, 70]
def con_circle(c,l):
    for i in range(len(c)):
        turtle.pencolor(c[i])
        turtle.circle(l[i])
con_circle(colors,l1)
