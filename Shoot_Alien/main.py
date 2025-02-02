#import the pygame zero libary
import pgzrun
from random import randint

#Pygame Standard for deciding the title of your game window
TITLE="Good shot"
#Pygame Standard for deciding the width and height for your game window in pixles 
WIDTH=500
HEIGHT=500

#varible to store the message displayed on your screen
message=""

#Actor is built-in object in pgzero
#interact with other actors , move around on the screen
#similar to a sprite in scratch
alien=Actor("alien")


#defult functions which will be called to update the screen
def draw():
    #screen is another built-in object
    screen.clear()
    screen.fill(color=(128,0,0))
#place_alien()
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

def place_alien():
    alien.x= randint(50, WIDTH-50)
    alien.y=randint(50, WIDTH-50)

def on_mouse_down(pos):
    #print("Hello World")
    global message 
    if alien.collidepoint(pos):
        message ="Good shot"
        place_alien()
    else:
        message ="Your aim is so bad"


#This methd needs to be called to start processing
place_alien()
pgzrun.go()
