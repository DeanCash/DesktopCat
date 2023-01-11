import pygame

from os.path import join as __join

from CatMisc import CatType
from pygame import Vector2
from Initcat import load_init as __load_init

transparent_color = (255, 0, 128)  # Transparency color
FPS = 60

ASSETS_DIR: str = "assets"
SPRITES_DIR: str = __join(ASSETS_DIR, "sprites_sheets")
FONTS_DIR: str = __join(ASSETS_DIR, "fonts")
CONFIG_DIR: str = "config"
SETTINGS_FILE: str = "settings.ini"
ICON_FILE = __join(ASSETS_DIR, "icon.ico")
DEFAULT_FONT_FILE = __join(FONTS_DIR, "CatFont.otf")
DEFAULT_FONT_SIZE = 36
DEFAULT_COLOR = pygame.Color(255, 255 ,255)

try:
    settings = __load_init(__join(CONFIG_DIR, SETTINGS_FILE))
except FileNotFoundError as e:
    # in future will handle this
    raise FileNotFoundError(e)

for cattype in CatType:
    type_name = cattype.name.lower()
    if type_name == settings['cat_type'].lower():
        cfg_cat_type: CatType = cattype
        break
# if not a valid CatType then error
else:
    raise Exception(f"Not a valid CatType in {SETTINGS_FILE} '{settings['cat_type']}'")

CFG_CAT_SCALE: float = float(settings['cat_size'])
# each cat in the atlas sprites are 32x32
CAT_SPRITE_SIZE: Vector2 = Vector2(32, 32)
# each sprite atlas has a size of 128x672
CAT_ATLAS_SIZE: Vector2 = Vector2(128, 672)
SANDBOX_MODE: bool = settings['sandbox_mode']

PROGRAM_NAME = "Desktop_Cat"

VERSION_TYPE: str = "ALPHA"
VERSION_NUMBER: int | float = 0.1
VERSION = f"{VERSION_TYPE} v{VERSION_NUMBER}"

WINDOW_TITLE: str = f"{PROGRAM_NAME} - {VERSION}"

