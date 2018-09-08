import turtle
import random


   
def move_random():
    turtle.setheading(random.randint(0, 360))
    turtle.forward(random.randint(50, 100))

def restart():
    turtle.reset()

turtle.onkey(move_random, ' ')
turtle.onkey(restart, 'Escape')

turtle.listen()

    
