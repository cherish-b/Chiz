#my 1st pygame file. Group

import pygame
import random  

#Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (127.5, 0, 127.5)
TEAL = (35, 250, 228)
YELLOW = (255, 247, 0)

#this initializes the game v
pygame.init()
#Set the width and height of the screen [width, height]
size = (700, 700) #(700, 700) makes a square
my_screen = pygame.display.set_mode(size) #this is saying here's my screen and this is the size I'm making it.
pygame. display.set_caption("THE SOURCE OF MY PAIN, TEARS, AND MISERY.")

clock = pygame.time.Clock() #used to manage how fast the screen updates

#this is the game loop
x = 70 
y = 20
done = False
speedx = 10
speedy = 10
#main event loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	my_screen.fill(TEAL) #background images
	clock.tick(60) 

	# -------------------- CHERISH! -- this code is (almost!!) perfect.
	# The problem is -- you are bouncing if x is equal to 700. But, sometimes 
	# the ball does not hit exactly 700 -- what happens if x = 701? 
	# Try, instead of testing if x == 700, x == 0 etc, to bounce when x >= 700, x <= 0, etc. 
	# That should work :) 
	# I know it feels like you are not getting it, because the ball doesn't bounce yet,
	# but actually I can see that you are understanding more and more each time you
	# try to debug your code. You are doing a great job. I know it's annoying
	# when something doesn't work on the first try (trust me - nothing ever works on the first try!) 
	# and when it doesn't work over and over and over again. I see how hard you are
	# working to stay calm and work through your problem. Even today is a tremendous
	# improvement from yesterday (both in your code and in your approach).
	# I am really proud of you for your grit and determination today Cherish! 

	if x == 700:
		speedx = speedx * -1
		speedy = speedy + 10
	elif y  == 700: 
		speedx = speedx + 10
		speedy = speedy * -1
	elif x == 0: 
		speedx = speedx * -1
		speedy = speedy + 10
	elif y == 0:
		speedx = speedx + 10
		speedy = speedy * -1
	x = x + speedx
	y = y + speedy
	pygame.draw.circle(my_screen, YELLOW, (x,y), 30)
	pygame.display.flip()

#updating the screen
#60 frames per second
#whyyyyyyyyy
