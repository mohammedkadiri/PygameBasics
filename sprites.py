
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = -20
        self.rect.x = random.randrange(SCREEN_WIDTH - 20)

    def update(self):
        """ Automatically called when we need to move the block."""
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()

class Player(Block):
    """This class represnets the player. """
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Game(object):
    """This class represents an instance of the game. If we need to
    reset the game we'd just need to create a new instance of this
    class. """

    def __init__(self):
        self.score = 0
        self.game_over = False

        # create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block of sprites
        for i in range(50):
            block = Block(BLACK, 20, 15)

            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # Create the player
        self.player = Player(RED,20,15)
        self.all_sprites_list.add(self.player)

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False

    def run_logic(self):

        if not self.game_over:
            self.all_sprites_list.update()

            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            for block in blocks_hit_list:
                self.score += 1
                print(self.score)

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(WHITE)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():

    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)


    done = False
    clock = pygame.time.Clock()

    game = Game()


    while not done:

        done = game.process_events()

        game.run_logic()

        game.display_frame(screen)

        clock.tick(20)

    pygame.quit()
    

if __name__ == '__main__':
    main()
