# filepath: SnakeGame/snake.py
import turtle
import time
import random

# Configuración inicial
delay = 0.1
score = 0
high_score = 0

# Configurar la pantalla
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactiva la actualización automática

# Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida de la serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()

# Lista de segmentos del cuerpo