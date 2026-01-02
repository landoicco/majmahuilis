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
from .settings import *
from .sound import *

__all__ = [
    "Game",
    "mini_map",
    "Map",
    "NPC",
    "ObjectRenderer",
    "Player",
    "Sound",
]
