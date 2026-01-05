from engine.sprite_object import *
from engine.npc import *
from .texture import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = "resources/sprites/npc/"
        self.static_sprite_path = "resources/sprites/static_sprites/"
        self.anim_sprite_path = "resources/sprites/animated_sprites/"
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # Sprite map
        add_sprite(
            SpriteObject(game, path="resources/sprites/static_sprites/candelabra.png")
        )
        add_sprite(
            AnimatedSprite(
                game, path="resources/sprites/animated_sprites/green_light/0.png"
            )
        )

        # NPC map
        add_npc(NPC(game, paths=BMONKEY))
        add_npc(NPC(game, paths=BMONKEY, pos=(11.5, 4.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
