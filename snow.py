
import random
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()


    size = [700, 500]
    screen = pygame.display.set_mode(size)

    done = False

    clock = pygame.time.Clock()

    star_list = []

    for i in range(50):
        x = random.randrange(0, 700)
        y = random.randrange(0, 500)
        star_list.append([x, y])

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


        screen.fill(BLACK)

        for item in star_list:
            item[1] += 1
            pygame.draw.circle(screen, WHITE,item, 2)

            if item[1] > 500:
                item[1] = random.randrange(-20, -5)
                item[0] = random.randrange(700)

        pygame.display.flip()

        clock.tick(20)
    pygame.quit()

if __name__ == "__main__":
    main()