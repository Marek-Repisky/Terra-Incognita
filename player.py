# player.py
import pygame

class Player:
    def __init__(self, game):
        self.game = game
        self.rect = game.player_images[0].get_rect()
        self.x = 100
        self.y = 350
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 5
        self.is_jumping = False
        self.jump_height = 15
        self.y_velocity = 0
        self.frame_index = 0
        self.animation_speed = game.BASE_PLAYER_ANIMATION_SPEED

    def jump(self):
        self.is_jumping = True
        self.y_velocity = -self.jump_height
        self.game.jump_sound.play()

    def update(self):
        # Handle player movement
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < self.game.screen_width:
            self.rect.x += self.speed

        # Jumping physics
        if self.is_jumping:
            self.rect.y += self.y_velocity
            self.y_velocity += 0.8

            if self.rect.bottom >= self.game.screen_height - self.game.ground_image.get_height():
                self.rect.bottom = self.game.screen_height - self.game.ground_image.get_height()
                self.is_jumping = False
                self.y_velocity = 0

        # Animate the player
        if not self.is_jumping:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.game.player_images):
                self.frame_index = 0

    def draw(self):
        self.game.screen.blit(self.game.player_images[int(self.frame_index)], self.rect)

    def reset(self):
        self.rect.x = 100
        self.rect.y = 350
        self.is_jumping = False
        self.y_velocity = 0
        self.frame_index = 0