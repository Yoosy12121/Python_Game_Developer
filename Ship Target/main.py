"""" An example of using animation() and clock scheduling to move actors around.

There are two actors in this example , each with a different movment stratedgy.

The block 
---------

The block moves in a loop around the screen:

*  We schedule the move_block() function to be called every 2 seconds using 
clock.schedule_interval().
* The next position of the bloxk is given by calling next() on a "cycle"
object,returned by itertools .cycle(). This will cycle through the block
coordinates we provide it, repeating without end.
*We use animate ( ) to move back .


the ship


the ship  moves in random dance in the middle of the screen . the ship flips backand forth between a rotation phase



next_ship_target(): pick a new target location for the ship at random , and
animate the rotating the ship to aim at it .when the roatation is comeperiljewli





"""
import random 
import itertools
import pgzrun

WIDTH = 400
HIEGHT = 400



#Define four sets of coordinates for the bloxk to move between
BLOCK_POSITIONS = [
    (350,50),
    (350,350),
    (50,350),
    (50,50),
]
#The cycle() function will let is cycle through the position indefineitely
block_positions = itertools.cycle(BLOCK_POSITIONS)


block = Actor('block',center=(50,50))
ship = Actor('ship',center=(200,200))


def draw():
    screen.clear()
    block.draw()
    ship.draw()


    #Block movement


    def move_block():
        animate(
            block,
            duration=1,
            pos=next(block_positions)
        )




    move_block()