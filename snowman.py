
import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)


def main():


    def draw_snowman(screen, x, y):
        pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
        pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
        pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

    pygame.init()

    size = [400, 500]
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    done = False


    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        draw_snowman(screen, 10, 10)

        draw_snowman(screen, 300, 10)

        draw_snowman(screen, 10, 300)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()





if __name__ == '__main__':
    main()