import turtle

for x,y,r in [(200,200,50), (-200,-200,30), (100, 100, 50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write((x,y))

    
