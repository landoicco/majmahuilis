import pygame
import sys

# Engine
from engine.util.object_renderer import *
from engine.util.pathfinding import *
from engine.util.raycasting import *
from engine.objects.sprite_object import *
from engine.objects.weapon import *
from engine.actors.player import *

# Customs
from .sound import *
from .map import *
from .texture import *
from .object_handler import *

from . import settings
from . import texture

weapon_path = "resources/sprites/weapon/shotgun/0.png"


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(settings.RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pygame.USEREVENT + 0
        self.settings = vars(settings)  # Store settings as a dictionary
        self.FPS = settings.FPS
        self.texture = texture
        pygame.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self, weapon_path)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(self.FPS)
        pygame.display.set_caption(f"{self.clock.get_fps():.1f}")

    # Debugging tool
    def draw_plain_map(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        # self.draw_plain_map()

    def check_events(self):
        self.global_trigger = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
