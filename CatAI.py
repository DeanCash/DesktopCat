from CatMisc import CatState as _CatState
from Constants import DEFAULT_COLOR
import random
# cannot import Cat class to use for type annotations
# because of circulair import error
from CatMisc import CatDirection, CatState, CatType; import pygame
from pygame import Surface, Vector2; from pygame.time import Clock
from SpriteAtlasManager import SpriteAtlas; from itertools import cycle
class Cat:
    # im using this dumb copied class so I get intellisense lol
    def __init__(self, screen: Surface, clock: Clock, position: Vector2, cattype: CatType):
        self.screen = screen
        self.clock = clock
        self.position = position
        self.type = cattype
        self.state = CatState.Idle
        self.facing = CatDirection.Left
        self.ai = CatBehaviour(self)
        self.__cat_sprite: Surface = None
        self.__sprite_atlas: SpriteAtlas = None
        self.__animation_sprites: cycle[list[Surface]] = None
        self.__animation_sprites_cycle: cycle[list[Surface]] = None
        self.__animation_sprites_len = 0
        self.__animation_frame_duration = 0.4
        self.__animation_frame_duration = 0.18
        self.__freeze_sprite = False
        self.__ticks_passed = 0.0

class CatBehaviour:
    def __init__(self, cat: Cat) -> None:
        self.cat = cat
        self.__time_since_decision = 0
        # the weight is the amount of occurrences of the variant
        self.__choices_weights = self.__make_choices_weights()
        self.__outer_bounds = self.__make_outer_bounds()
        self.__current_decision: CatState = None
        self.__busy = False

    def __make_choices_weights(self):
        choices = []
        for s in CatState:
            for _ in range(s.value[0]):
                choices.append(s)
        return choices

    def __make_outer_bounds(self):
        outer_padding = 100
        screen_w = self.cat.screen.get_width()
        screen_h = self.cat.screen.get_height()
        # !
        return pygame.Rect(outer_padding, outer_padding, screen_w - (outer_padding * 2), screen_h - (outer_padding * 20))

    def decision(self):
        choice = random.choice(self.__choices_weights)
        if choice == CatState.Idle:
            pass
        elif choice == CatState.Walking:
            new_position


        pygame.draw.rect(self.cat.screen, DEFAULT_COLOR, self.__outer_bounds)

        self.__time_since_decision += self.cat.clock.get_time() / 1000

