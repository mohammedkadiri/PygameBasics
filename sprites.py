
import pygame
import random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(700-20)

    def update(self):
        self.rect.y += 1

        if self.rect.y > 410:
            self.reset_pos()

class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = pos[1]


pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(black, 20, 15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)


player = Player(red, 20, 15)
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)

    all_sprites_list.update()

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    for block in blocks_hit_list:
        score += 1
        print(score)
        block.reset_pos()

    all_sprites_list.draw(screen)

    clock.tick(20)

    pygame.display.flip()

pygame.quit()

