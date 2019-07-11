

import pygame


def main():

    pygame.init()

    size = [626, 417]

    screen = pygame.display.set_mode(size)

    done = False

    clock = pygame.time.Clock()

    galaxy = pygame.image.load("graphics/galaxy.jpg").convert()
    spaceship= pygame.image.load("graphics/spaceship.gif").convert()
    spaceship.set_colorkey((255, 255, 255))

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

        screen.blit(galaxy, [0, 0])
        screen.blit(spaceship, [x, y])
        pygame.display.flip()

        clock.tick(20)
    pygame.quit()


if __name__ == '__main__':
    main()