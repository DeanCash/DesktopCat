from os.path import join as __join
from json import load as __load

from CatMisc import CatType
from pygame import Vector2

transparent_color = (255, 0, 128)  # Transparency color
FPS = 60

sprites_dir: str = "assets/sprites_sheets"
config_dir: str = "config"
settings_file: str = "settings.json"

with open(__join(config_dir, settings_file)) as f:
    settings = __load(f)

for cattype in CatType:
    type_name = cattype.name.lower()
    if type_name == settings['cat_type'].lower():
        cfg_cat_type: CatType = cattype
        break
# if not a valid CatType then error
else:
    raise Exception(f"Not a valid CatType in {settings_file} '{settings['cat_type']}'")

cfg_cat_scale: int | float = settings['cat_size']
# each cat in the atlas sprites are 32x32
CAT_SPRITE_SIZE: Vector2 = Vector2(32, 32)
# each sprite atlas has a size of 128x672
CAT_ATLAS_SIZE: Vector2 = Vector2(128, 672)

VERSION = "BETA "
WINDOW_TITLE: str = "Desktop_Goose"

