import pygame
from pygame import Surface, Vector2
from typing import Union, Tuple
from typing_extensions import Self

class SpriteAtlas:
    def __init__(self, path: str, atlas_surface: Surface, sprite_size: Vector2) -> Self:
        self.file_path = path
        self.atlas = atlas_surface
        self.sprite_size = sprite_size
        # setting default value to negative size of sprite size, so now if get_next_sprite gets called
        # it will always get the first sprite from atlas without need for a previous get_sprite_at call
        self.index = Vector2(0, 0) - sprite_size

        size = self.atlas.get_size()
        self.__bounds = Vector2(size[0] // self.sprite_size[0], size[1] // self.sprite_size[1])

    def get_sprite_at(self, position_x_y: Union[Vector2, Tuple[int, int]]) -> Surface:
        if (position_x_y[0] > self.__bounds[0]) or (position_x_y[1] > self.__bounds[1]) or (position_x_y[0] < 0) or (position_x_y[1] < 0):
            raise Exception("Out of bounds")

        pixel_position_x_y: Vector2 = Vector2(0, 0) + ((position_x_y[0] * self.sprite_size.x), (position_x_y[1] * self.sprite_size.y))

        self.index = pixel_position_x_y
        return self.atlas.subsurface(pixel_position_x_y, self.sprite_size)

    def get_next_sprite(self) -> Surface:
        atlas_size = self.atlas.get_size()
        next_position: Vector2 = self.index + (self.sprite_size.x, 0)
        if next_position.x >= atlas_size[0]:
            next_position.x = 0
            next_position.y += self.sprite_size.y
        if next_position.y >= atlas_size[1]:
            next_position.y = 0
        self.index = next_position
        return self.atlas.subsurface(next_position, self.sprite_size)

    def get_sprites_onward(self, from_x_y: Union[Vector2, Tuple[int, int]], amount_inclusive: int):
        sprites: list[Surface] = []
        sprites.append(self.get_sprite_at(from_x_y))
        for _ in range(amount_inclusive - 1):
            sprites.append(self.get_next_sprite())
        return sprites

    def get_sprites_onward_scaled(self, from_x_y: Union[Vector2, Tuple[int, int]], amount_inclusive: int, scale: int):
        sprites: list[Surface] = []
        sprites.append(pygame.transform.scale(self.get_sprite_at(from_x_y), (self.sprite_size.x * scale, self.sprite_size.y * scale)))
        for _ in range(amount_inclusive - 1):
            sprites.append(pygame.transform.scale(self.get_next_sprite(), (self.sprite_size.x * scale, self.sprite_size.y * scale)))
        return sprites
