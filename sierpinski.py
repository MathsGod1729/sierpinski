import pygame
import random as rnd

pygame.init()

# Set width and height of screen
WIDTH = 600
HEIGHT = 600

# Set the colour of the initial triangle's points
TRIANGLE_COLOUR = 'red'

# Draw the three points of the initial triangle
POINTS = [
    (300, 75),
    (50, 508),
    (550, 508) ]

# Set the colour of the first point and subsequent points
INIT_COLOUR = 'cyan'
COLOUR = 'white'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clicked = False # boolean that determines what to do when the user clicks the screen

# Initialize the pos variable to be the origin
pos = (0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for p in POINTS:
        pygame.draw.circle(screen, TRIANGLE_COLOUR, p, 3)
        pygame.display.flip()

    # draw a point 
    if event.type == pygame.MOUSEBUTTONDOWN:
        if not clicked:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, INIT_COLOUR, pos, 2)
            pygame.display.flip()
            pygame.time.wait(200)
            clicked = True
        else:
            pygame.time.wait(200)
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            clicked = False
        
    if clicked:
        r = rnd.randint(0,2)
        pos = ((pos[0]+POINTS[r][0])//2, (pos[1]+POINTS[r][1])//2)
        pygame.draw.circle(screen, COLOUR, pos, 2)
        pygame.display.flip()

pygame.quit()