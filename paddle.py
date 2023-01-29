from turtle import Turtle

#Creamos una clase Paddle haciendo herencia de la clase Turtle para heredar sus métodos.
class Paddle(Turtle):

    #Iniciamos constructor poniendo la posición del objeto como parámetro porque será diferente en cada instancia.
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        #Con Shapesize indicamos altura y anchura del objeto instanciado
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 80
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() -80
        self.goto(self.xcor(), new_y)




