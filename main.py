import paddle
import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


#Instanciamos pantalla y le damos propiedades
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

#Instanciamos nuestros objetos paddle. Uno para cada lado de nuestra pantalla
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
#Instanciamos nuestro objeto bola
ball = Ball()
#Instanciamos marcador izquierdo
score = Score()

#Indicamos a nuestra pantalla que debe ponerse a la escucha mediante método listen
screen.listen()

#Configuramos las teclas que servirán para mover nuestra barra en nuestras instancias mediante los métodos
# "go_up" y "go_down" que hemos creado en la clase Paddle
screen.onkey(r_paddle.go_up, 'p')
screen.onkey(r_paddle.go_down, 'l')

screen.onkey(l_paddle.go_up, 'q')
screen.onkey(l_paddle.go_down, 'a')



#Creamos booleano para indicar que mientras esté como True se irá actualizando la pantalla.
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    #Llamamos al método "move" que hemos creado en la clase Ball para que se mueva hacia arriba a la derecha al iniciar el juego.
    ball.move()

    #Detectar colisión con pared y techo
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detectar colisión con el paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed(+40)

    #Detectar cuando la pelota derecha falla
    if ball.xcor() > 380:
        ball.ball_in_the_center()
        score.l_point()

    #Detecar cuando la pelota izquierda falla
    if ball.xcor() < -380:
        ball.ball_in_the_center()
        score.r_point()

screen.exitonclick()
