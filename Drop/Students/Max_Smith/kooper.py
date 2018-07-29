import turtle
window = turtle.Screen()
kooper = turtle.Turtle()

kooper.color("green","black")
kooper.left(90)
kooper.forward(100)
kooper.right(90)
kooper.circle(10)
for i in range(1,999):
    kooper.left(15)
    kooper.forward(50)
    kooper.left(157)
    kooper.forward(50)
window.exitonclick()

