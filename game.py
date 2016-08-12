#my 1st pygame file. Group

import pygame

#Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#this initializes the game v
pygame.init()
#Set the width and height of the screen [width, height]
size = (700, 700) #(700, 700) makes a square
screen = pygame.display.set_mode(size) #this is saying here's my screen and this is the size I'm making it.
pygame. display.set_caption("MY FIRST GAME! :)")

clock = pygame.time.Clock() #used to manage how fast the screen updates

#this is the game loop
done = False
#main event loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

screen.fill(RED) #background images

#updating the screen
pygame.display.flip()

clock.tick(60) #60 frames per second