

import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def main():

    def draw_stick_figure(screen, x, y):
        # Head
        pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

        # Legs
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

        # Body
        pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

        # Arms
        pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
        pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


    pygame.init()

    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    done = False

    clock = pygame.time.Clock()

    x_coord = 10
    y_coord = 10

    x_speed = 0
    y_speed = 0

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                if event.key == pygame.K_RIGHT:
                    x_speed = 3
                if event.key == pygame.K_UP:
                    y_speed = -3
                if event.key == pygame.K_DOWN:
                    y_speed = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0

            # pos = pygame.mouse.get_pos()
            # x = pos[0]
            # y = pos[1]

            x_coord += x_speed
            y_coord += y_speed

            print("x_speed:", x_speed, "y_speed:", y_speed, "x_coord", x_coord, "y_coord", y_coord)

            screen.fill(WHITE)
            draw_stick_figure(screen, x_coord, y_coord)

            pygame.display.flip()

            clock.tick(20)
    pygame.quit()











if __name__ == '__main__':
     main()