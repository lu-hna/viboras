from turtle import *
from random import randrange, choice
from freegames import square, vector

colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Asignar colores aleatorios a la serpiente y la comida
snake_color = choice([c for c in colors if c != 'red'])
colors.remove(snake_color)
food_color = choice([c for c in colors if c != 'red'])
colors.remove(food_color)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(20, -20)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        if len(colors) > 0:
            # Asignar nuevos colores aleatorios a la serpiente y la comida
            global snake_color, food_color
            snake_color = food_color
            food_color = choice(colors)
            colors.remove(food_color)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Actualizar la posición de la comida aleatoriamente
    while True:
        new_food = food.copy()
        new_food.x += randrange(-1, 2, 1) * 10
        new_food.y += randrange(-1, 2, 1) * 10
        if inside(new_food):
            food.x, food.y = new_food.x, new_food.y
            break

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 200)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()