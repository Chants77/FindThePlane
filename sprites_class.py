import pygame as pg
SCREEN_RECT = pg.Rect(0, 0, 1280, 720)
FPS = 60
NEXT_PAGE = pg.USEREVENT
screen = pg.display.set_mode((1280, 720))
layer = 0

# layer
# 1 封面
# 2 menu
# 21 stage
# 22 endless
# 23 battle
# 24 rule1
# 242 rule2


class Element(pg.sprite.Sprite):
    def __init__(self, image_name):
        super().__init__()
        self.image = pg.image.load(image_name)
        self.rect = self.image.get_rect()


class Background(Element):
    def __init__(self, image_name):
        super().__init__(image_name)
        self.rect.x = 0
        self.rect.y = 0


class Button(Element):
    def __init__(self, image_name, x, y):
        super().__init__(image_name)
        self.rect.x = x
        self.rect.y = y


class Number(Element):
    def __init__(self, image_name, number):
        super().__init__(image_name)
        self.rect.y = 300
        if 0 < number <= 9:
            self.rect.x = 950
        elif number >= 10:
            self.rect.x = 850
        elif number == 0:
            self.rect.x = 978
        self.number = number


class StepNumber(Element):
    def __init__(self, image_name, number, dire):
        super().__init__(image_name)
        self.dire = dire
        self.rect.x = 230
        if self.dire == 1:
            self.rect.y = 263
        elif self.dire == 2:
            self.rect.y = 325
        self.number = number


class GameBg(Element):
    def __init__(self, image_name, x, y):
        super().__init__(image_name)
        self.rect.x = x
        self.rect.y = y


class BattleNumber(Element):
    def __init__(self, image_name, number, winner):
        super().__init__(image_name)
        self.rect.y = 300
        if winner == 1:
            if 0 <= number <= 9:
                self.rect.x = 400
            elif number >= 10:
                self.rect.x = 250
            self.number = number
        if winner == 2:
            if 0 <= number <= 9:
                self.rect.x = 850
            elif number >= 10:
                self.rect.x = 700
            self.number = number
# class GameElement(Element):
#     def
