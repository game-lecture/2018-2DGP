import turtle

count = 0
while (count <= 5):
    turtle.penup()
    turtle.goto(count * 100, 500)
    turtle.pendown()
    turtle.goto(count * 100, 0)
    count = count + 1

count = 0
while (count <= 5):
    turtle.penup()
    turtle.goto(0, count * 100)
    turtle.pendown()
    turtle.goto(500, count * 100)
    count = count + 1
    
    

