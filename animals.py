# animals.py
import pygame
import random

class Animal:
    def __init__(self, game, images, x, y, animation_speed, speed):
        self.game = game
        self.images = images
        self.rect = images[0].get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.frame_index = 0
        self.animation_speed = animation_speed
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        self.animate()

        if self.rect.right < 0:
            self.reset_position()

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            self.frame_index = 0

    def draw(self):
        if self.should_draw():
            self.game.screen.blit(self.images[int(self.frame_index)], self.rect)

    def should_draw(self):
        # Determine if the animal should be drawn based on the current scene
        if isinstance(self, Snail) or isinstance(self, Fly):
            return not self.game.transition
        elif isinstance(self, Hyena) or isinstance(self, Vulture):
            return self.game.transition and not self.game.transition2
        elif isinstance(self, Scorpion) or isinstance(self, Crow):
            return self.game.transition2 and not self.game.transition3
        elif isinstance(self, Mouse) or isinstance(self, Pigeon):
            return self.game.transition3
        return False

    def reset_position(self):
        if isinstance(self, (Snail, Hyena, Scorpion, Mouse)):
            self.rect.x = self.game.screen_width + random.randint(0, 200)
            # Ensure flying enemies are spawned far enough from ground enemies
            if isinstance(self, Snail):
                potential_fly_enemies = [self.game.animals["fly"], self.game.animals["vulture"], self.game.animals["crow"], self.game.animals["pigeon"]]
                for fly_enemy in potential_fly_enemies:
                    if abs(fly_enemy.rect.x - self.rect.right) < 200:
                        fly_enemy.rect.x = self.rect.right + 200
            elif isinstance(self, Hyena):
                if abs(self.game.animals["vulture"].rect.x - self.rect.right) < 200:
                    self.game.animals["vulture"].rect.x = self.rect.right + 200
            elif isinstance(self, Scorpion):
                if abs(self.game.animals["crow"].rect.x - self.rect.right) < 200:
                    self.game.animals["crow"].rect.x = self.rect.right + 200
            elif isinstance(self, Mouse):
                if abs(self.game.animals["pigeon"].rect.x - self.rect.right) < 200:
                    self.game.animals["pigeon"].rect.x = self.rect.right + 200
        else:  # Flying enemies
            self.rect.x = self.game.screen_width + random.randint(400, 600)
            self.rect.y = self.y
            # Ensure flying enemies are spawned far enough from ground enemies
            if isinstance(self, Fly):
                if abs(self.rect.x - self.game.animals["snail"].rect.left) < 200:
                    self.rect.x = self.game.animals["snail"].rect.left + 200
            elif isinstance(self, Vulture):
                if abs(self.rect.x - self.game.animals["hyena"].rect.left) < 200:
                    self.rect.x = self.game.animals["hyena"].rect.left + 200
            elif isinstance(self, Crow):
                if abs(self.rect.x - self.game.animals["scorpion"].rect.left) < 200:
                    self.rect.x = self.game.animals["scorpion"].rect.left + 200
            elif isinstance(self, Pigeon):
                if abs(self.rect.x - self.game.animals["mouse"].rect.left) < 200:
                    self.rect.x = self.game.animals["mouse"].rect.left + 200

    def reset(self):
        self.reset_position()
        self.frame_index = 0

class Hyena(Animal):
    def __init__(self, game):
        super().__init__(game, game.hyena_images, game.screen_width, 380,
                        game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Snail(Animal):
    def __init__(self, game):
        super().__init__(game, game.snail_images, game.screen_width, 400, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Scorpion(Animal):
    def __init__(self, game):
        super().__init__(game, game.scorpion_images, game.screen_width, 370, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Fly(Animal):
    def __init__(self, game):
        super().__init__(game, game.fly_images, game.screen_width + random.randint(400, 600), 220, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Vulture(Animal):
    def __init__(self, game):
        super().__init__(game, game.vulture_images, game.screen_width + random.randint(400, 600), 220, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Crow(Animal):
    def __init__(self, game):
        super().__init__(game, game.crow_images, game.screen_width + random.randint(400, 600), 220, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Pigeon(Animal):
    def __init__(self, game):
        super().__init__(game, game.pigeon_images, game.screen_width + random.randint(400, 600), 220, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)

class Mouse(Animal):
    def __init__(self, game):
        super().__init__(game, game.mouse_images, game.screen_width, 400, game.BASE_ANIMAL_ANIMATION_SPEED, game.BASE_ANIMAL_SPEED)