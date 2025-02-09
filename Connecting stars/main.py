import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

star = []
lines =[]
next_star = 0

start_time = 0
total_time = 0
end_time = 0

number_of_star =10

def create_star():
    global start_time
    for count in range(0,number_of_star):
        star = Actor("star")
        star.pos = randint(40,WIDTH-40),randint(40,HEIGHT-40)
        star.append(star)
    start_time = time()


def draw():
    global total_time

    screen.blit("background",(0,0))
    number = 1
    for star in star:
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+20))
        star.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

    if next_star < number_of_star:
        total_time = time() -start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)


def update():
    pass

def on_mouse_down(pos):
    global next_star,lines

    if next_star < number_of_star:
        if star [next_star].collidepoint(pos):
            if next_star:
                lines.append((star[next_star-1].pos,star[next_star].pos))
            next_star = next_star+1
        else:
            lines = []
            next_star=0

create_star()

pgzrun.go()