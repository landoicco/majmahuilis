import pygame
from .settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture(
            "resources/textures/sky.png", (WIDTH, HALF_HEIGHT)
        )
        self.sky_offset = 0
        self.blood_screen = self.get_texture("resources/textures/blood_screen.png", RES)
        self.game_over_image = self.get_texture("resources/textures/game_over.png", RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    # TODO: Improve how health looks on screen
    def draw_player_health(self):
        health = str(self.game.player.health)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(health, True, (255, 255, 255))
        # Draw text on screen
        self.screen.blit(text_surface, (100, 100))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        # Floor
        pygame.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(
            self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True
        )
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture("resources/textures/1.png"),
            2: self.get_texture("resources/textures/2.png"),
            3: self.get_texture("resources/textures/3.png"),
            4: self.get_texture("resources/textures/4.png"),
            5: self.get_texture("resources/textures/5.png"),
        }
