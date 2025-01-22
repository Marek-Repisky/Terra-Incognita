import pygame
import json
import os
import math
from player import Player
from animals import Hyena, Snail, Scorpion, Fly, Vulture, Crow, Pigeon, Mouse
from background import Background

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()

        # Load sounds
        self.jump_sound = pygame.mixer.Sound("dist/sounds/jump.mp3")
        self.game_over_sound = pygame.mixer.Sound("dist/sounds/game-over.mp3")
        self.background_music = pygame.mixer.Sound("dist/sounds/background-music.mp3")
        self.jump_sound.set_volume(0.1)
        self.game_over_sound.set_volume(0.3)
        self.background_music.set_volume(0.1)

        # Start playing background music on loop
        self.background_music.play(-1)

        # Screen dimensions
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Title
        pygame.display.set_caption("Terra Incognita")

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        # Load and scale images
        self.load_images()

        # Game Variables
        self.BASE_PLAYER_ANIMATION_SPEED = 0.07
        self.BASE_ANIMAL_ANIMATION_SPEED = 0.1
        self.BASE_ANIMAL_SPEED = 4
        self.BASE_SCROLL_SPEED = 4

        # Initialize player, animals, and background
        self.player = Player(self)
        self.animals = {
            "hyena": Hyena(self),
            "snail": Snail(self),
            "scorpion": Scorpion(self),
            "fly": Fly(self),
            "vulture": Vulture(self),
            "crow": Crow(self),
            "pigeon": Pigeon(self),
            "mouse": Mouse(self)
        }
        self.background = Background(self)

        # Score
        self.score = 0
        self.font = pygame.font.Font("dist/font/Pixeltype.ttf", 40)

        # Game over flag
        self.game_over = False

        # Transition flags and scores
        self.transition = False
        self.transition2 = False
        self.transition3 = False
        self.scene_duration = 500

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Leaderboard
        self.leaderboard_scores = self.load_leaderboard()
        self.score_saved = False

    def load_images(self):
        # Initial background images
        self.sky_image = pygame.image.load("dist/img/background/firstScene/sky.png").convert_alpha()
        self.ground_image = pygame.image.load("dist/img/background/firstScene/ground.png").convert_alpha()

        # New background images (for transition 1)
        self.parallax_images = [
            pygame.image.load("dist/img/background/secondScene/parallax1-1.png").convert_alpha(),
            pygame.image.load("dist/img/background/secondScene/parallax1-2.png").convert_alpha(),
            pygame.image.load("dist/img/background/secondScene/parallax1-3.png").convert_alpha(),
            pygame.image.load("dist/img/background/secondScene/parallax1-4.png").convert_alpha()
        ]

        # New background images (for transition 2)
        self.parallax2_images = [
            pygame.image.load("dist/img/background/thirdScene/parallax2-1.png").convert_alpha(),
            pygame.image.load("dist/img/background/thirdScene/parallax2-2.png").convert_alpha(),
            pygame.image.load("dist/img/background/thirdScene/parallax2-3.png").convert_alpha(),
            pygame.image.load("dist/img/background/thirdScene/parallax2-4.png").convert_alpha()
        ]

        # New background images (for transition 3)
        self.parallax3_images = [
            pygame.image.load("dist/img/background/fourthScene/parallax3-1.png").convert_alpha(),
            pygame.image.load("dist/img/background/fourthScene/parallax3-2.png").convert_alpha(),
            pygame.image.load("dist/img/background/fourthScene/parallax3-3.png").convert_alpha(),
            pygame.image.load("dist/img/background/fourthScene/parallax3-4.png").convert_alpha(),
            pygame.image.load("dist/img/background/fourthScene/parallax3-5.png").convert_alpha()
        ]

        # Player images
        self.player_images = [
            pygame.image.load("dist/img/player/player1.png").convert_alpha(),
            pygame.image.load("dist/img/player/player2.png").convert_alpha()
        ]

        # Animal images
        self.hyena_images = [pygame.image.load(f"dist/img/animals/groundEnemy/hyena/hyena{i}.png").convert_alpha() for i in range(1, 7)]
        self.snail_images = [pygame.image.load(f"dist/img/animals/groundEnemy/snail/snail{i}.png").convert_alpha() for i in range(1, 3)]
        self.scorpion_images = [pygame.image.load(f"dist/img/animals/groundEnemy/scorpion/scorpion{i}.png").convert_alpha() for i in range(1, 5)]
        self.fly_images = [pygame.image.load(f"dist/img/animals/flyingEnemy/fly/fly{i}.png").convert_alpha() for i in range(1, 3)]
        self.vulture_images = [pygame.image.load(f"dist/img/animals/flyingEnemy/vulture/vulture{i}.png").convert_alpha() for i in range(1, 5)]
        self.crow_images = [pygame.image.load(f"dist/img/animals/flyingEnemy/crow/crow{i}.png").convert_alpha() for i in range(1, 7)]
        self.pigeon_images = [pygame.image.load(f"dist/img/animals/flyingEnemy/pigeon/pigeon{i}.png").convert_alpha() for i in range(1, 7)]
        self.mouse_images = [pygame.image.load(f"dist/img/animals/groundEnemy/mouse/mouse{i}.png").convert_alpha() for i in range(1, 5)]

        self.scale_images()

    def scale_images(self):
        # Scale background images to fit the screen
        self.sky_image = pygame.transform.scale(self.sky_image, (self.screen_width, self.screen_height))
        self.ground_image = pygame.transform.scale(self.ground_image, (self.screen_width, self.ground_image.get_height()))

        # Scale parallax images (all transitions)
        for images, heights in [
            (self.parallax_images, (160, -100)),
            (self.parallax2_images, (-425, -125)),
            (self.parallax3_images, (215, -60))
        ]:
            for i in range(len(images)):
                if i == 0:  # Ground image
                    images[i] = pygame.transform.scale(images[i], (self.screen_width, self.screen_height + heights[0]))
                else:  # Sky images
                    images[i] = pygame.transform.scale(images[i], (self.screen_width, self.screen_height + heights[1]))

    def load_leaderboard(self):
        if os.path.exists('leaderboard.json'):
            try:
                with open('leaderboard.json', 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_leaderboard(self, scores):
        with open('leaderboard.json', 'w') as f:
            json.dump(scores, f)

    def update_leaderboard(self, new_score):
        scores = self.load_leaderboard()
        scores.append(new_score)
        scores.sort(reverse=True)
        scores = scores[:5]  # Keep only top 5 scores
        self.save_leaderboard(scores)
        return scores

    def reset_game(self):
        self.player.reset()
        for animal in self.animals.values():
            animal.reset()
        self.background.reset()
        self.score = 0
        self.game_over = False
        self.transition = False
        self.transition2 = False
        self.transition3 = False
        self.score_saved = False
        self.background_music.play(-1)
        self.player.animation_speed = self.BASE_PLAYER_ANIMATION_SPEED
        for animal in self.animals.values():
            animal.animation_speed = self.BASE_ANIMAL_ANIMATION_SPEED
            animal.speed = self.BASE_ANIMAL_SPEED
        self.background.scroll_speed = self.BASE_SCROLL_SPEED

    def get_current_scene(self, score):
        scene_cycle = score // self.scene_duration % 4  # 4 scenes total (0, 1, 2, 3)

        if scene_cycle == 0:  # Initial background (0-499, 2000-2499, etc.)
            return False, False, False
        elif scene_cycle == 1:  # Transition 1 (500-999, 2500-2999, etc.)
            return True, False, False
        elif scene_cycle == 2:  # Transition 2 (1000-1499, 3000-3499, etc.)
            return True, True, False
        else:  # Transition 3 (1500-1999, 3500-3999, etc.)
            return True, True, True

    def calculate_speed_multiplier(self, score):
        # Increase by 1% for every 100 points
        multiplier = 1 + (score // 100) * 0.1
        return multiplier

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if (event.key in [pygame.K_SPACE, pygame.K_w, pygame.K_UP]
                        and not self.player.is_jumping
                        and not self.game_over):
                    self.player.jump()
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()
        return True

    def update(self):
        if not self.game_over:
            self.player.update()
            for animal in self.animals.values():
                animal.update()
            self.background.update()

            # Check for collision
            self.check_collisions()

            # Increase score and update transitions
            self.score += 1
            speed_multiplier = self.calculate_speed_multiplier(self.score)

            # Update speeds
            self.player.animation_speed = self.BASE_PLAYER_ANIMATION_SPEED * speed_multiplier
            for animal in self.animals.values():
                animal.animation_speed = self.BASE_ANIMAL_ANIMATION_SPEED * speed_multiplier
                animal.speed = self.BASE_ANIMAL_SPEED * speed_multiplier
            self.background.scroll_speed = self.BASE_SCROLL_SPEED * speed_multiplier

            old_transition, old_transition2, old_transition3 = self.transition, self.transition2, self.transition3
            self.transition, self.transition2, self.transition3 = self.get_current_scene(self.score)

            # If any transition state changes, reset ALL enemies to the right side
            if (self.transition != old_transition or
                    self.transition2 != old_transition2 or
                    self.transition3 != old_transition3):
                for animal in self.animals.values():
                    animal.reset_position()

    def check_collisions(self):
        if not self.transition:
            if self.player.rect.colliderect(self.animals["snail"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
            if self.player.rect.colliderect(self.animals["fly"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
        elif self.transition and not self.transition2:
            if self.player.rect.colliderect(self.animals["hyena"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
            if self.player.rect.colliderect(self.animals["vulture"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
        elif self.transition2 and not self.transition3:
            if self.player.rect.colliderect(self.animals["scorpion"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
            if self.player.rect.colliderect(self.animals["crow"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
        elif self.transition3:
            if self.player.rect.colliderect(self.animals["mouse"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()
            if self.player.rect.colliderect(self.animals["pigeon"].rect):
                self.game_over = True
                self.background_music.stop()
                self.game_over_sound.play()

    def draw(self):
        self.background.draw()

        if not self.game_over:
            self.player.draw()
            for animal in self.animals.values():
                animal.draw()

            # Display score
            score_text = self.font.render("Score: " + str(self.score), True, self.black)
            self.screen.blit(score_text, (10, 10))
        else:
            if not self.score_saved:
                self.leaderboard_scores = self.update_leaderboard(self.score)
                self.score_saved = True

            # Semi-transparent overlay
            overlay = pygame.Surface((self.screen_width, self.screen_height))
            overlay.fill((0, 0, 0))
            overlay.set_alpha(128)
            self.screen.blit(overlay, (0, 0))

            # Game over title
            title_font = pygame.font.Font("dist/font/Pixeltype.ttf", 74)
            game_over_text = title_font.render("Game Over", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 100))
            self.screen.blit(game_over_text, text_rect)

            # Final score
            score_font = pygame.font.Font("dist/font/Pixeltype.ttf", 48)
            final_score_text = score_font.render(f"Final Score: {self.score}", True, self.white)
            final_score_rect = final_score_text.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 30))
            self.screen.blit(final_score_text, final_score_rect)

            # Leaderboard
            leaderboard_font = pygame.font.Font("dist/font/Pixeltype.ttf", 36)
            leaderboard_title = leaderboard_font.render("Top Scores:", True, self.white)
            self.screen.blit(leaderboard_title, (self.screen_width / 2 - 60, self.screen_height / 2 + 10))

            for i, high_score in enumerate(self.leaderboard_scores):
                score_text = leaderboard_font.render(f"{i + 1}. {high_score}", True, self.white)
                self.screen.blit(score_text, (self.screen_width / 2 - 40, self.screen_height / 2 + 40 + (i * 30)))

            # Restart instructions with pulsing effect
            restart_font = pygame.font.Font("dist/font/Pixeltype.ttf", 36)
            alpha = abs(math.sin(pygame.time.get_ticks() * 0.003)) * 255
            restart_text = restart_font.render("Press 'R' to Restart", True, self.white)
            restart_text.set_alpha(int(alpha))
            restart_rect = restart_text.get_rect(center=(self.screen_width / 2, self.screen_height - 50))
            self.screen.blit(restart_text, restart_rect)

        # Update the display
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
