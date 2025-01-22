# background.py
import pygame

class Background:
    def __init__(self, game):
        self.game = game
        self.sky_x = 0
        self.ground_x = 0
        self.scroll_speed = game.BASE_SCROLL_SPEED
        self.parallax_x = [0] * len(game.parallax_images)
        self.parallax2_x = [0] * len(game.parallax2_images)
        self.parallax3_x = [0] * len(game.parallax3_images)

    def update(self):
        # Move the background (check for transitions)
        if not self.game.transition and not self.game.transition2 and not self.game.transition3:
            self.sky_x -= self.scroll_speed // 2  # Slower for the sky
            self.ground_x -= self.scroll_speed
        elif self.game.transition and not self.game.transition2 and not self.game.transition3:
            # Move parallax background (transition 1)
            for i in range(len(self.game.parallax_images)):
                self.parallax_x[i] -= self.scroll_speed // (i + 2)  # Different speeds for each layer
        elif self.game.transition2 and not self.game.transition3:
            # Move parallax background (transition 2)
            for i in range(len(self.game.parallax2_images)):
                self.parallax2_x[i] -= self.scroll_speed // (i + 2)
        elif self.game.transition3:
            # Move parallax background (transition 3)
            for i in range(len(self.game.parallax3_images)):
                self.parallax3_x[i] -= self.scroll_speed // (i + 2)

        # Reset background positions
        if self.sky_x <= -self.game.screen_width:
            self.sky_x = 0
        if self.ground_x <= -self.game.screen_width:
            self.ground_x = 0

        # Reset parallax positions (transition 1)
        for i in range(len(self.game.parallax_images)):
            if self.parallax_x[i] <= -self.game.screen_width:
                self.parallax_x[i] = 0

        # Reset parallax positions (transition 2)
        for i in range(len(self.game.parallax2_images)):
            if self.parallax2_x[i] <= -self.game.screen_width:
                self.parallax2_x[i] = 0

        # Reset parallax positions (transition 3)
        for i in range(len(self.game.parallax3_images)):
            if self.parallax3_x[i] <= -self.game.screen_width:
                self.parallax3_x[i] = 0

    def draw(self):
        # Draw the background (with transitions)
        if not self.game.transition and not self.game.transition2 and not self.game.transition3:
            self.game.screen.blit(self.game.sky_image, (self.sky_x, 0))
            self.game.screen.blit(self.game.sky_image, (self.sky_x + self.game.screen_width, 0))
            self.game.screen.blit(self.game.ground_image, (self.ground_x, self.game.screen_height - self.game.ground_image.get_height()))
            self.game.screen.blit(self.game.ground_image, (self.ground_x + self.game.screen_width, self.game.screen_height - self.game.ground_image.get_height()))
        elif self.game.transition and not self.game.transition2 and not self.game.transition3:
            # Draw parallax background (transition 1)
            for i in range(len(self.game.parallax_images) - 1, -1, -1):  # Draw from back to front
                self.game.screen.blit(self.game.parallax_images[i], (self.parallax_x[i], 0 if i > 0 else self.game.screen_height - self.game.parallax_images[i].get_height()))
                self.game.screen.blit(self.game.parallax_images[i], (self.parallax_x[i] + self.game.screen_width, 0 if i > 0 else self.game.screen_height - self.game.parallax_images[i].get_height()))
        elif self.game.transition2 and not self.game.transition3:
            # Draw parallax background (transition 2)
            for i in range(len(self.game.parallax2_images) - 1, -1, -1):  # Draw from back to front
                self.game.screen.blit(self.game.parallax2_images[i], (self.parallax2_x[i], 0 if i > 0 else self.game.screen_height - self.game.parallax2_images[i].get_height()))
                self.game.screen.blit(self.game.parallax2_images[i], (self.parallax2_x[i] + self.game.screen_width, 0 if i > 0 else self.game.screen_height - self.game.parallax2_images[i].get_height()))
        elif self.game.transition3:
            # Draw parallax background (transition 3)
            for i in range(len(self.game.parallax3_images) - 1, -1, -1):  # Draw from back to front
                self.game.screen.blit(self.game.parallax3_images[i], (self.parallax3_x[i], 0 if i > 0 else self.game.screen_height - self.game.parallax3_images[i].get_height()))
                self.game.screen.blit(self.game.parallax3_images[i], (self.parallax3_x[i] + self.game.screen_width, 0 if i > 0 else self.game.screen_height - self.game.parallax3_images[i].get_height()))

    def reset(self):
        self.sky_x = 0
        self.ground_x = 0
        self.parallax_x = [0] * len(self.game.parallax_images)
        self.parallax2_x = [0] * len(self.game.parallax2_images)
        self.parallax3_x = [0] * len(self.game.parallax3_images)
