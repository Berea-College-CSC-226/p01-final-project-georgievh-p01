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

import pygame
import random


class Game:
    def __init__(self, width=800, height=600):

        # Initialize Pygame
        pygame.init()

        # Screen settings
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("SquareShooter")

        # Colors
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)

        # Game state
        self.clock = pygame.time.Clock()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.running = True

        # Game objects
        self.player = Player(50, self.height // 2)
        self.bullets = []
        self.enemies = []

        # Game parameters
        self.frame_count = 0
        self.spawn_rate = 60

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Shooting
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self.bullets)

    def update(self):
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(-5)
        if keys[pygame.K_DOWN]:
            self.player.move(5)

        # Spawn enemies
        self.frame_count += 1
        if self.frame_count >= self.spawn_rate:
            self.spawn_enemy()
            self.frame_count = 0

        # Update bullets
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.is_off_screen(self.width):
                self.bullets.remove(bullet)

        # Update enemies
        for enemy in self.enemies[:]:
            enemy.move()
            if enemy.is_off_screen():
                self.enemies.remove(enemy)

        # Check collisions
        self.check_collisions()

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.collides_with(enemy):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    break

        # Check if enemies reach left side
        for enemy in self.enemies:
            if enemy.rect.right < 0:
                self.running = False

    def spawn_enemy(self):
        y = random.randint(0, self.height - 30)
        enemy = Enemy(self.width, y)
        self.enemies.append(enemy)

    def draw(self):
        # Clear screen
        self.screen.fill(self.black)

        # Draw player
        pygame.draw.rect(self.screen, self.blue, self.player.rect)

        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.white, bullet.rect)

        # Draw enemies
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, self.red, enemy.rect)

        # Draw score
        score_text = self.font.render("Score: " + str(self.score), True, self.white)
        self.screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()


class Player:
    def __init__(self, x, y, size=40):
        self.size = size
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def move(self, dy):
        self.rect.y += dy
        # Keep player on screen
        screen_height = pygame.display.get_surface().get_height()
        self.rect.y = max(0, min(self.rect.y, screen_height - self.size))

    def shoot(self, bullets):
        bullet = Bullet(self.rect.right, self.rect.centery - 5)
        bullets.append(bullet)


class Bullet:
    def __init__(self, x, y, size=10, speed=10):
        self.size = size
        self.speed = speed
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def move(self):
        self.rect.x += self.speed

    def is_off_screen(self, screen_width):
        return self.rect.left > screen_width

    def collides_with(self, other):
        return self.rect.colliderect(other.rect)


class Enemy:
    def __init__(self, x, y, size=30, speed=3):
        self.size = size
        self.speed = speed
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def move(self):
        self.rect.x -= self.speed

    def is_off_screen(self):
        return self.rect.right < 0


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()