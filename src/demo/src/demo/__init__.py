"""
Demo
Specific game code
"""

__version__ = "1.0.0"
__author__ = "Lando Icaza C."

from .game import *
from .map import *
from .npc import *
from .object_handler import *
from .object_renderer import *
from .player import *
from .raycasting import *
from .settings import *
from .sound import *
from .sprite_object import *
from .weapon import *

__all__ = [
    "Game",
    "mini_map",
    "Map",
    "NPC",
    "ObjectRenderer",
    "Player",
    "RayCasting",
    "Sound",
    "SpriteObject",
    "AnimatedSprite",
    "Weapon",
]
