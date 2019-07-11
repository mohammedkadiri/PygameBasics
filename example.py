
import pygame

pygame.init()


# Set the width and height of the screen
size=[700,500]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Mo's cool game")

#Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

#----- Main Program Loop ------
while not done:
    #Event processing should go below this comment
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: # if user clicked close
            done = True #Flag that we are done so we exit this loop


    screen.fill((255,255,255))

    text = font.render("Hello World", True, (0, 0, 0))

    screen.blit(text, [100, 100])
    pygame.display.flip()

    #Limit to 20 frames per second
    clock.tick(20)
pygame.quit()