from copy import deepcopy
import re
from CatMisc import CatType, CatState
from SpriteAtlas import SpriteAtlas
from Constants import *

import pygame
from pygame import Surface, Rect, Vector2
from pygame.time import Clock

import os
from itertools import cycle
from typing_extensions import Self

class Cat:
    def __init__(self, screen: Surface, clock: Clock, position: Vector2, cattype: CatType) -> Self:
        self.screen = screen
        self.clock = clock
        self.position = position
        self.type = cattype
        self.state = CatState.Idle
        self.__cat_sprite: Surface = None
        self.__sprite_atlas: SpriteAtlas = None
        self.__animation_sprites: cycle[list[Surface]] = None
        self.__animation_sprites_cycle: cycle[list[Surface]] = None
        # self.__animation_sprites_len = 0
        self.__animation_frame_duration = 0.4
        self.__animation_frame_duration = 0.18
        self.__freeze_sprite = False
        self.__ticks_passed = 0.0
        self._i = 0

        self.set_type(self.type)

    def set_type(self, new_cat_type: CatType) -> None:
        sprite_atlas_path = new_cat_type.value[0] if os.path.exists(new_cat_type.value[0]) else os.path.join(SPRITES_DIR, new_cat_type.value[0])
        sprite_atlas = pygame.image.load(sprite_atlas_path).convert_alpha()

        self.__sprite_atlas = SpriteAtlas(sprite_atlas_path, sprite_atlas, CAT_SPRITE_SIZE)
        self.__set_animation_array()

    def __set_animation_array(self) -> None:
        temp_array = []

        if self.state == CatState.Idle:
            # temp_surface = self.__sprite_atlas.get_sprite_at((0, 12))
            # temp_size: tuple[int, int] = temp_surface.get_size()
            # self.__animation_sprites_len = 1

            # temp_array.append(pygame.transform.scale(temp_surface, (temp_size[0] * CFG_CAT_SCALE, temp_size[1] * CFG_CAT_SCALE)))
            # for i in range(3):
            #     self.__animation_sprites_len += 1
            #     temp_surface = self.__sprite_atlas.get_next_sprite()
            #     temp_size: tuple[int, int] = temp_surface.get_size()

            #     temp_array.append(pygame.transform.scale(temp_surface, (temp_size[0] * CFG_CAT_SCALE, temp_size[1] * CFG_CAT_SCALE)))
            temp_array = self.__sprite_atlas.get_sprites_onward_scaled((0, 3), 4, CFG_CAT_SCALE)
            # self.__animation_sprites_len = len(temp_array)

        self.__animation_sprites = cycle(temp_array)
        self.__animation_sprites_cycle = cycle(self.__make_cycling_from_single(temp_array))
        self.__cat_sprite = next(self.__animation_sprites)

        # TODO scaling of cat
        # pygame.transform.scale(self.__sprite_atlas.atlas, (size[0] * scale, size[1] * scale))

    def __make_cycling_from_single(self, array: list[Surface]):
        temp_cycle_array = array.copy()
        arr_copy_rev = list(reversed(array.copy()))
        arr_copy_rev.pop(0)
        temp_cycle_array.extend(arr_copy_rev)
        return temp_cycle_array

    def render(self) -> None:
        if not self.__freeze_sprite:
            if self.__ticks_passed >= self.__animation_frame_duration:
                self.__cat_sprite = next(self.__animation_sprites_cycle)
                self.__ticks_passed = 0.0
                self._i += 1
            # ? Uncomment to freeze cat after first cycle of animation is done
            # if self._i >= self.__animation_sprites_len - 1:
            #     self.__freeze_sprite = True
            #     print(self._i)

        self.screen.blit(self.__cat_sprite, self.position)
        self.__ticks_passed += self.clock.get_time() / 1000
