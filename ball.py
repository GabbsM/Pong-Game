import turtle
from turtle import Turtle

#Creamos una clase "ball" haciendo herencia de la clase Turtle para heredar sus métodos.
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    #Creamos un método "move" para hacer mover a nuestra bola hacia arriba a la derecha
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_in_the_center(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()







