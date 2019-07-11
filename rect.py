
import pygame

pygame.init()


size = [700, 500]
screen = pygame.display.set_mode(size)

WHITE =(255,255, 255)
BLACK = (0, 0, 0)

done = False

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [rect_x, rect_y, 50, 50])

    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    pygame.display.flip()

    clock.tick(20)
pygame.quit()