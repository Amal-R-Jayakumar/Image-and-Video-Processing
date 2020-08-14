import turtle
turlte_color=turtle.Screen()
turlte_color.bgcolor('black')
my_turtle=turtle.Turtle()
my_turtle.pensize(1)
my_turtle.shape('turtle')
my_turtle.speed(1000)
for j in range(12):
    my_turtle.right(30)
    n=50
    for i in range(5):
        my_turtle.pensize(1)
        my_turtle.color('red')
        n=n+4
        my_turtle.circle(n)
    n=75
    for i in range(5):
        my_turtle.pensize(1)
        my_turtle.color('yellow')
        n=n+4
        my_turtle.circle(n)
    n=100
    for i in range(5):
        my_turtle.pensize(1)
        my_turtle.color('white')
        n=n+8
        my_turtle.circle(n)
