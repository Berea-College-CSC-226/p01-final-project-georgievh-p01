######################################################################
# Author: Chris Georgiev
# Username: georgievh
#
# Assignment: T11: Final Project
#
# Purpose: showcase learned skills
######################################################################
# Acknowledgements:
# - see references in readme
####################################################################################

def increase_difficulty(self):
    # Increase difficulty
    self.difficulty_level += 1

    # Reduce spawn rate (enemies spawn more frequently)
    self.spawn_rate = max(10, self.spawn_rate - 5)

    # Increase enemy speed
    Enemy.base_speed += 0.5

    # Optional: make player movement slightly more challenging
    # Player.SPEED -= 0.1

    # Visual feedback for difficulty increase
    difficulty_text = self.font.render(f"Difficulty Level: {self.difficulty_level}", True, self.white)
    difficulty_rect = difficulty_text.get_rect(center=(self.width // 2, 50))
    self.screen.blit(difficulty_text, difficulty_rect)
    pygame.display.update()
    pygame.time.delay(500)  # Brief pause to show difficulty increase

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, window, screen_size):
        """
        Represents the player in the game.

        :param screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        self.x = 0
        self.y = 0
        self.velocity = 0


    def do_something(self, window):
        pygame.draw.rect(window, (255,0,0),(0,0,20,20))
        pygame.display.update()


def main():
    '''
    contains main gameloop and setup code
    :return:
    '''
    pygame.init()

    clock = pygame.time.Clock()

    is_running = True

    #window = pygame.display.set_mode((500,500))
    pygame.display.set_caption('SquareShooter')

    player_one = Player(window, (500, 500))
    player_one.do_something(window)

    while is_running:
        clock.tick(30)   # determines frames per second

        # handles closing the window gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            print('up pressed')
        elif keys[pygame.K_DOWN]:
            print('down pressed')


main()