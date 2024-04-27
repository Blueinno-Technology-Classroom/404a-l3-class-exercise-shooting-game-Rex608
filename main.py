import pgzrun
import random
import pygame

pygame.mouse.set_visible(False)

WIDTH = 720
HEIGHT = 480

target1 = Actor("target_red1")
target1.x = WIDTH/2
target1.y = HEIGHT/2
target1.dx = random.randint(1,5)

brown_duck = Actor("duck_outline_target_white")
brown_duck.x = random.randint(0,WIDTH)
brown_duck.top = random.randint(0,HEIGHT-brown_duck.height)
brown_duck.dx = random.randint(1,5)

aim = Actor("crosshair_outline_large")

score = 0



def update():
    target1.x += target1.dx
    if target1.right >= WIDTH :
        target1.left = 0
        target1.y = random.randint(0,HEIGHT)
        target1.dx = random.randint(1,5)
    if target1.top <= 0:
        target1.top = 0
    if target1.bottom >= HEIGHT:
        target1.bottom = HEIGHT
        
    brown_duck.x += brown_duck.dx
    if brown_duck.right >= WIDTH :
        brown_duck.left = 0
        brown_duck.y = random.randint(0,HEIGHT)
        brown_duck.dx = random.randint(1,5)
    if brown_duck.top <= 0:
        brown_duck.top = 0
    if brown_duck.bottom >= HEIGHT:
        brown_duck.bottom = HEIGHT

def on_mouse_move(pos):
    aim.pos = pos

def on_mouse_down():
    global score
    if aim.colliderect(target1):
        target1.left = 0
        target1.dx += 2
        target1.top = random.randint(0,HEIGHT-target1.height)
        score += 10
    elif aim.colliderect(brown_duck):
        brown_duck.left = 0
        brown_duck.dx += 2
        brown_duck.top = random.randint(0,HEIGHT-brown_duck.height)
        score += 50
    
def draw():
    screen.clear()
    target1.draw()
    brown_duck.draw()
    aim.draw()
    screen.draw.text(str(score),(10,10),fontsize= 50, color='green')
pgzrun.go()