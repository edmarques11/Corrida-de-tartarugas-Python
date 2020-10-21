from logging.config import listen

import pygame

from turtle import *
from random import *

# https://repl.it/@aislanrafael/projectraceturtle codigo do Aislan
# github do aislan https://github.com/aislan/python_turtle_exemplos
# link que o Joanes mandou https://projects.codeclubworld.org/pt-BR/09_python/04/Turtle%20Power.html


screen = Screen()
shape('classic')
penup()
speed(0)
goto(-500, 200)
pendown()
begin_fill()
fd(1000)
right(90)
fd(400)
right(90)
fd(1000)
right(90)
fd(400)
end_fill()

penup()
fd(10)
right(90)
for i in range(11):
    write(i)
    fd(100)

backward(1100)
right(90)
fd(12)
left(90)
pensize(5)
pendown()
pencolor('white')

# listras laranjas
for i in range(7):
    fd(1000)
    penup()
    backward(1000)
    right(90)
    forward(66)
    left(90)
    pendown()

# começo das listras brancas na pista
penup()
left(90)
fd(429)
right(90)
fd(5)
for i in range(5):
    pencolor('orange')
    pendown()
    fd(100)
    penup()
    fd(100)
backward(1000)
right(90)
fd(66)
left(90)
for i in range(5):
    pencolor('orange')
    pendown()
    fd(100)
    penup()
    fd(100)
backward(1000)
right(90)
fd(66)
left(90)
for i in range(5):
    pencolor('orange')
    pendown()
    fd(100)
    penup()
    fd(100)
backward(1000)
right(90)
fd(66)
left(90)
for i in range(5):
    pencolor('orange')
    pendown()
    fd(100)
    penup()
    fd(100)
backward(1000)
right(90)
fd(66)
left(90)
for i in range(5):
    pencolor('orange')
    pendown()
    fd(100)
    penup()
    fd(100)
backward(1000)
right(90)
fd(66)
left(90)
for i in range(5):
    pencolor('orange')
    pendown()
    fd(100)
    penup()
    fd(100)
backward(1000)
# fim das listras brancas

fd(945)
right(90)
fd(28)
left(180)
backward(5)
pendown()
pensize(10)
forward(397)
right(90)
penup()
forward(27)
right(90)
pendown()
pencolor('red')
forward(397)
penup()
# final da pista
goto(-500, 140)
left(90)
nome = 'BARRICHELLO'
write(nome, color('white'), font=('Arial', 14))
goto(295, 140)
write(nome, color('white'), font=('Arial', 14))
goto(-500, 74)
nome = 'SCHUMACHER'
write(nome, color('white'), font=('Arial', 14))
goto(295, 74)
write(nome, color('white'), font=('Arial', 14))
goto(-500, 8)
nome = 'VETEL'
write(nome, color('white'), font=('Arial', 14))
goto(295, 8)
write(nome, color('white'), font=('Arial', 14))
goto(-500, -58)
nome = 'RAIKONEN'
write(nome, color('white'), font=('Arial', 14))
goto(295, -58)
write(nome, color('white'), font=('Arial', 14))
goto(-500, -124)
nome = 'FELIPE MASSA'
write(nome, color('white'), font=('Arial', 14))
goto(295, -124)
write(nome, color('white'), font=('Arial', 14))
goto(-500, -190)
nome = 'AYRTON SENNA'
write(nome, color('white'), font=('Arial', 14))
goto(295, -190)
write(nome, color('white'), font=('Arial', 14))

# Largada
color('black')
goto(-550, 140)
letra = 'L'
write(letra, font=('Arial', 40))
goto(-550, 80)
letra = 'A'
write(letra, font=('Arial', 40))
goto(-550, 20)
letra = 'R'
write(letra, font=('Arial', 40))
goto(-550, -40)
letra = 'G'
write(letra, font=('Arial', 40))
goto(-550, -100)
letra = 'A'
write(letra, font=('Arial', 40))
goto(-550, -153)
letra = 'D'
write(letra, font=('Arial', 40))
goto(-550, -210)
letra = 'A'
write(letra, font=('Arial', 40))
hideturtle()

barrichello = Turtle()
barrichello.shapesize(3, 3)
barrichello.penup()
barrichello.shape('turtle')
barrichello.color('purple')
barrichello.goto(-500, 165)

schumacher = Turtle()
schumacher.shapesize(3, 3)
schumacher.penup()
schumacher.shape('turtle')
schumacher.color('red')
schumacher.goto(-500, 99)

vetel = Turtle()
vetel.shapesize(3, 3)
vetel.penup()
vetel.shape('turtle')
vetel.color('yellow')
vetel.goto(-500, 33)

raikonen = Turtle()
raikonen.shapesize(3, 3)
raikonen.penup()
raikonen.shape('turtle')
raikonen.color('green')
raikonen.goto(-500, -33)

felipemassa = Turtle()
felipemassa.shapesize(3, 3)
felipemassa.penup()
felipemassa.shape('turtle')
felipemassa.color('pink')
felipemassa.goto(-500, -99)

airtonsena = Turtle()
airtonsena.shapesize(3, 3)
airtonsena.penup()
airtonsena.shape('turtle')
airtonsena.color('blue')
airtonsena.goto(-500, -165)

pygame.init()
pygame.mixer.music.load('papaleguas.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	pass
pygame.quit()

play = False

listen()
def Play():
	while True:
		barrichello.fd(randint(1, 10))
		schumacher.fd(randint(1, 10))
		vetel.fd(randint(1, 10))
		raikonen.fd(randint(1, 10))
		felipemassa.fd(randint(1, 10))
		airtonsena.fd(randint(1, 10))
		if barrichello.xcor() > 475 or schumacher.xcor() > 475 or vetel.xcor() > 475 or raikonen.xcor() > 475 or felipemassa.xcor() > 475 or airtonsena.xcor() > 475:
			pygame.init()
			pygame.mixer.music.load('Ayrton Senna.mp3')
			pygame.mixer.music.play()
			while pygame.mixer.get_busy():
				pass
			pygame.mixer.unload()
			pygame.quit()
			break

screen.onkeypress(Play,'Up')
screen.listen()

done()