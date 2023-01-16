import pygame as pg
import sys
import random as r
from pygame.locals import *
from sprites_class import *
from ElementsAndGroup import *


def num_to_step(num):
    pics = {
        0: s0,
        1: s1,
        2: s2,
        3: s3,
        4: s4,
        5: s5,
        6: s6,
        7: s7,
        8: s8,
        9: s9,
        10: s10,
        11: s11,
        12: s12,
        13: s13,
        14: s14,
        15: s15,
        16: s16,
        17: s17,
        18: s18,
        19: s19,
        20: s20,
        21: s21,
        22: s22,
        23: s23,
        24: s24,
        25: s25
    }

    return pics.get(num, None)


def num_to_remain(num):
    pics = {
        0: r0,
        1: r1,
        2: r2,
        3: r3,
        4: r4,
        5: r5,
        6: r6,
        7: r7,
        8: r8,
        9: r9,
        10: r10,
        11: r11,
        12: r12,
        13: r13,
        14: r14,
        15: r15,
        16: r16,
        17: r17,
        18: r18,
        19: r19,
        20: r20,
        21: r21,
        22: r22,
        23: r23,
        24: r24,
        25: r25
    }

    return pics.get(num, None)


class GridPoint(pg.sprite.Sprite):
    def __init__(self, x, y, color, value):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.value = value
# 格子上的点


class Flight(pg.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.direction = direction
        self.flight_place = []


class Flight1(Flight):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        if self.direction == 1:
            self.flight_place = ([(self.x, self.y), (self.x-2, self.y+1),
                                  (self.x - 1, self.y + 1), (self.x, self.y + 1),
                                  (self.x + 1, self.y + 1), (self.x + 2, self.y + 1),
                                  (self.x, self.y + 2), (self.x - 1, self.y + 3),
                                  (self.x, self.y + 3), (self.x + 1, self.y + 3)])
        elif self.direction == 2:
            self.flight_place = ([(self.x, self.y), (self.x-1, self.y-2),
                                  (self.x - 3, self.y - 1), (self.x - 1, self.y - 1),
                                  (self.x - 3, self.y), (self.x - 2, self.y),
                                  (self.x - 1, self.y), (self.x - 3, self.y + 1),
                                  (self.x - 1, self.y + 1), (self.x - 1, self.y + 2)])
        elif self.direction == 3:
            self.flight_place = ([(self.x, self.y), (self.x-1, self.y-3),
                                  (self.x, self.y - 3), (self.x + 1, self.y - 3),
                                  (self.x, self.y - 2), (self.x - 2, self.y - 1),
                                  (self.x - 1, self.y - 1), (self.x, self.y - 1),
                                  (self.x + 1, self.y - 1), (self.x + 2, self.y - 1)])

        elif self.direction == 4:
            self.flight_place = ([(self.x, self.y), (self.x+1, self.y-2),
                                  (self.x + 3, self.y - 1), (self.x + 1, self.y - 1),
                                  (self.x + 3, self.y), (self.x + 2, self.y),
                                  (self.x + 1, self.y), (self.x + 3, self.y + 1),
                                  (self.x + 1, self.y + 1), (self.x + 1, self.y + 2)])
# 第一种飞机


class Flight2(Flight):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        if self.direction == 1:
            self.flight_place = ([(self.x, self.y), (self.x-2, self.y+2),
                                  (self.x-1, self.y+1), (self.x, self.y+1),
                                  (self.x+1, self.y+1), (self.x+2, self.y+2),
                                  (self.x, self.y+2), (self.x, self.y+3),
                                  (self.x-1, self.y+4), (self.x, self.y+4),
                                  (self.x+1, self.y+4)])
        if self.direction == 2:
            self.flight_place = ([(self.x, self.y), (self.x-2, self.y-2),
                                  (self.x-4, self.y-1), (self.x-1, self.y-1),
                                  (self.x-4, self.y), (self.x-3, self.y),
                                  (self.x-2, self.y), (self.x-1, self.y),
                                  (self.x-4, self.y+1), (self.x-1, self.y+1),
                                  (self.x-2, self.y+2)])
        if self.direction == 3:
            self.flight_place = ([(self.x, self.y), (self.x - 2, self.y - 2),
                                  (self.x - 1, self.y - 1), (self.x, self.y - 1),
                                  (self.x + 1, self.y - 1), (self.x + 2, self.y - 2),
                                  (self.x, self.y - 2), (self.x, self.y - 3),
                                  (self.x - 1, self.y - 4), (self.x, self.y - 4),
                                  (self.x + 1, self.y - 4)])
        if self.direction == 4:
            self.flight_place = ([(self.x, self.y), (self.x + 2, self.y - 2),
                                  (self.x + 4, self.y - 1), (self.x + 1, self.y - 1),
                                  (self.x + 4, self.y), (self.x + 3, self.y),
                                  (self.x + 2, self.y), (self.x + 1, self.y),
                                  (self.x + 4, self.y + 1), (self.x + 1, self.y + 1),
                                  (self.x + 2, self.y + 2)])
# 第二种飞机


class Flight3(Flight):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        if self.direction == 1:
            self.flight_place = ([(self.x, self.y), (self.x-2, self.y+1),
                                  (self.x-1, self.y+1), (self.x, self.y+1),
                                  (self.x+1, self.y+1), (self.x+2, self.y+1),
                                  (self.x, self.y+2), (self.x, self.y+3),
                                  (self.x-1, self.y+4), (self.x+1, self.y+4)])
        if self.direction == 2:
            self.flight_place = ([(self.x, self.y), (self.x-1, self.y-2),
                                  (self.x-4, self.y-1), (self.x-1, self.y-1),
                                  (self.x-3, self.y), (self.x-2, self.y),
                                  (self.x-1, self.y), (self.x-4, self.y+1),
                                  (self.x-1, self.y+1), (self.x-1, self.y+2)])
        if self.direction == 3:
            self.flight_place = ([(self.x, self.y), (self.x - 2, self.y - 1),
                                  (self.x - 1, self.y - 1), (self.x, self.y - 1),
                                  (self.x + 1, self.y - 1), (self.x + 2, self.y - 1),
                                  (self.x, self.y - 2), (self.x, self.y - 3),
                                  (self.x - 1, self.y - 4), (self.x + 1, self.y - 4)])
        if self.direction == 4:
            self.flight_place = ([(self.x, self.y), (self.x + 1, self.y - 2),
                                  (self.x + 4, self.y - 1), (self.x + 1, self.y - 1),
                                  (self.x + 3, self.y), (self.x + 2, self.y),
                                  (self.x + 1, self.y), (self.x + 4, self.y + 1),
                                  (self.x + 1, self.y + 1), (self.x + 1, self.y + 2)])
# 第三种飞机


class MainGame(object):
    def __init__(self, game_method, game_mode, max_step):
        self.clock = pg.time.Clock()
        self.game_mode = game_mode
        self.game_method = game_method
        self.grid_list = []
        self.max_step = max_step
        self.head_to_find = 0
        self.head = 0
        self.time = 0
        self.step = 0
        self.pass_the_round = 1
        self.finish = 0
        # print("游戏初始化")

    def __init_grid(self):
        self.grid_list = []
        for i in range(0, 10):
            row_list = []
            for j in range(0, 10):
                x = 450 + i * 45
                y = 130 + j * 45
                gp = GridPoint(x, y, 0, 0)
                row_list.append(gp)
            self.grid_list.append(row_list)
            self.game = pg.sprite.Group(bg1, grid)
            if self.game_method == 1:
                self.game.add(steps, s0, num_to_remain(self.max_step))
            self.game.update()
            self.game.draw(screen)
            pg.display.update()
            self.head = 0
            self.time = 0
            self.step = 0
            self.pass_the_round = 1
            self.finish = 0
            if self.game_mode == 1:
                self.head_to_find = 2
            if self.game_mode == 2:
                self.head_to_find = 2
            if self.game_mode == 3:
                self.head_to_find = 3
        # print("格子初始化")

    # 初始化方格

    def add_flight1(self):
        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 3 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 3 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if y - 3 >= 0 and x - 2 >= 0 and x + 2 <= 9:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane1 = Flight1(x, y, dire)
            # print("没出界")
            # 用flight_place中每一个元素遍历整个格子
            for temp in plane1.flight_place:
                # print(temp[0], temp[1])
                overlap = 0
                # print(self.grid_list[temp[0]][temp[1]].color)
                if self.grid_list[temp[0]][temp[1]].color != 0:
                    # print(overlap)
                    overlap = 1
                    break

            if overlap == 0:
                # print("here")
                for temp in plane1.flight_place:
                    if temp[0] == plane1.x and temp[1] == plane1.y:
                        self.grid_list[temp[0]][temp[1]].color = 2
                        # print(temp[0], temp[1])
                    else:
                        self.grid_list[temp[0]][temp[1]].color = 1
                # print("造好了")
                break

    # 添加第一种飞机

    def add_flight2(self):
        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 4 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 4 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if x + 2 <= 9 and x - 2 >= 0 and y - 4 >= 0:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane2 = Flight2(x, y, dire)

            # 用flight_place中每一个元素遍历整个格子
            for temp in plane2.flight_place:
                overlap = 0
                if self.grid_list[temp[0]][temp[1]].color != 0:
                    overlap = 1
                    break
            if overlap == 0:
                for temp in plane2.flight_place:
                    if temp[0] == plane2.x and temp[1] == plane2.y:
                        self.grid_list[temp[0]][temp[1]].color = 2
                        # print(temp[0], temp[1])
                    else:
                        self.grid_list[temp[0]][temp[1]].color = 1
                break

    # 添加第二种飞机

    def add_flight3(self):
        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 4 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 4 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if x + 2 <= 9 and x - 2 >= 0 and y - 4 >= 0:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane3 = Flight3(x, y, dire)
            # 用flight_place中每一个元素遍历整个格子
            for temp in plane3.flight_place:
                overlap = 0
                if self.grid_list[temp[0]][temp[1]].color != 0:
                    overlap = 1
                    break
            if overlap == 0:
                for temp in plane3.flight_place:
                    if temp[0] == plane3.x and temp[1] == plane3.y:
                        self.grid_list[temp[0]][temp[1]].color = 2
                        # print(temp[0], temp[1])
                    else:
                        self.grid_list[temp[0]][temp[1]].color = 1
                break

    # 添加第三种飞机

    def game_event_handler(self):  # 事件监测
        global x1, y1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("退出游戏")
                pg.quit()
                exit()
            # 退出游戏
            if self.head < self.head_to_find:
                if self.game_method == 1:
                    if self.step == self.max_step:
                        self.finish = 1
                        self.pass_the_round = 0
                        # print("失败")
                        break
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    # print(x, y)
                    if 450 <= x <= 900 and 130 <= y <= 580:
                        # print("点中了")
                        if self.time == 0:
                            i = (x - 450) // 45
                            j = (y - 130) // 45
                            x1 = i
                            y1 = j
                            # print(x1, y1)
                            if self.grid_list[i][j].value == 0:
                                # print("没翻过")
                                choose.rect.x = self.grid_list[i][j].x - 2
                                choose.rect.y = self.grid_list[i][j].y - 2
                                self.game.add(choose)
                                self.game.update()
                                self.game.draw(screen)
                                pg.display.update()
                                self.time += 1
                        elif self.time == 1:
                            choose.kill()
                            i = (x - 450) // 45
                            j = (y - 130) // 45
                            # print("翻过了")
                            # print(x1, y1)
                            if i == x1 and j == y1:
                                # print("同一个")
                                self.grid_list[i][j].value = 1
                                if self.grid_list[i][j].color == 0:
                                    white = Element("./image/white.png")
                                    white.rect.x = self.grid_list[i][j].x
                                    white.rect.y = self.grid_list[i][j].y
                                    self.game.add(white)
                                    # print("白")
                                elif self.grid_list[i][j].color == 1:
                                    blue = Element("./image/blue.png")
                                    blue.rect.x = self.grid_list[i][j].x
                                    blue.rect.y = self.grid_list[i][j].y
                                    self.game.add(blue)
                                elif self.grid_list[i][j].color == 2:
                                    red = Element("./image/red.png")
                                    red.rect.x = self.grid_list[i][j].x
                                    red.rect.y = self.grid_list[i][j].y
                                    self.game.add(red)
                                    self.head += 1
                                self.game.update()
                                self.game.draw(screen)
                                pg.display.update()
                                self.time = 0
                                if self.game_method == 1:
                                    self.step += 1
                                    num_to_step(self.step-1).kill()
                                    num_to_remain(self.max_step-self.step+1).kill()
                                    self.game.add(num_to_step(self.step), num_to_remain(self.max_step-self.step))
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()
                            else:
                                x1 = i
                                y1 = j
                                choose.rect.x = self.grid_list[i][j].x - 2
                                choose.rect.y = self.grid_list[i][j].y - 2
                                self.game.add(choose)
                                self.game.update()
                                self.game.draw(screen)
                                pg.display.update()
            if self.head == self.head_to_find:
                self.pass_the_round = 1
                self.finish = 1
                # print("成功")
                break

    def start_game(self):
        self.__init_grid()
        if self.game_mode == 1:
            self.add_flight1()
            self.add_flight1()
        if self.game_mode == 2:
            self.add_flight2()
            # print("第二种飞机")
            self.add_flight2()
        if self.game_mode == 3:
            self.add_flight1()
            self.add_flight2()
            self.add_flight3()
        # print("游戏开始")
        while self.finish == 0:
            self.clock.tick(60)
            self.game_event_handler()
        # print("游戏结束")


class BattleMainGame(object):
    def __init__(self, game_mode):
        self.clock = pg.time.Clock()
        self.game_mode = game_mode
        self.grid_list1 = []
        self.grid_list2 = []
        self.head_to_find = 0
        self.head1 = 0
        self.head2 = 0
        self.time = 0
        self.step = 0
        self.winner = 0
        self.finish1 = 0
        self.finish2 = 0
        self.turn = 0
        # print("游戏初始化")

    def __init_grid(self):
        self.grid_list1 = []
        self.grid_list2 = []
        for i in range(0, 10):
            row_list = []
            for j in range(0, 10):
                x = 180 + i * 40
                y = 150 + j * 40
                gp = GridPoint(x, y, 0, 0)
                row_list.append(gp)
            self.grid_list1.append(row_list)
        for i in range(0, 10):
            row_list = []
            for j in range(0, 10):
                x = 700 + i * 40
                y = 150 + j * 40
                gp = GridPoint(x, y, 0, 0)
                row_list.append(gp)
            self.grid_list2.append(row_list)
        self.game = pg.sprite.Group(bg1, battle_grid1, battle_grid2)
        self.game.update()
        self.game.draw(screen)
        pg.display.update()
        self.head1 = 0
        self.head2 = 0
        self.time = 0
        self.step = 0
        self.winner = 0
        self.finish1 = 0
        self.finish2 = 0
        self.turn = 1
        if self.game_mode == 1:
            self.head_to_find = 2
        if self.game_mode == 2:
            self.head_to_find = 2
        if self.game_mode == 3:
            self.head_to_find = 3
    # print("格子初始化")
    # 初始化方格

    def add_flight1(self):
        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 3 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 3 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if y - 3 >= 0 and x - 2 >= 0 and x + 2 <= 9:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane1 = Flight1(x, y, dire)
            # print("没出界")
            # 用flight_place中每一个元素遍历整个格子
            for temp in plane1.flight_place:
                # print(temp[0], temp[1])
                overlap = 0
                # print(self.grid_list1[temp[0]][temp[1]].color)
                if self.grid_list1[temp[0]][temp[1]].color != 0:
                    # print(overlap)
                    overlap = 1
                    break

            if overlap == 0:
                # print("here")
                for temp in plane1.flight_place:
                    if temp[0] == plane1.x and temp[1] == plane1.y:
                        self.grid_list1[temp[0]][temp[1]].color = 2
                    else:
                        self.grid_list1[temp[0]][temp[1]].color = 1
                # print("造好了")
                break

        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 3 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 3 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if y - 3 >= 0 and x - 2 >= 0 and x + 2 <= 9:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane1 = Flight1(x, y, dire)
            # print("没出界")
            # 用flight_place中每一个元素遍历整个格子
            for temp in plane1.flight_place:
                # print(temp[0], temp[1])
                overlap = 0
                # print(self.grid_list2[temp[0]][temp[1]].color)
                if self.grid_list2[temp[0]][temp[1]].color != 0:
                    # print(overlap)
                    overlap = 1
                    break

            if overlap == 0:
                # print("here")
                for temp in plane1.flight_place:
                    if temp[0] == plane1.x and temp[1] == plane1.y:
                        self.grid_list2[temp[0]][temp[1]].color = 2
                        # print(self.grid_list2[temp[0]][temp[1]].color)
                    else:
                        self.grid_list2[temp[0]][temp[1]].color = 1
                # print("造好了")
                break
    # 添加第一种飞机

    def add_flight2(self):
        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 4 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 4 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if x + 2 <= 9 and x - 2 >= 0 and y - 4 >= 0:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane2 = Flight2(x, y, dire)

            # 用flight_place中每一个元素遍历整个格子
            for temp in plane2.flight_place:
                overlap = 0
                if self.grid_list1[temp[0]][temp[1]].color != 0:
                    overlap = 1
                    break
            if overlap == 0:
                for temp in plane2.flight_place:
                    if temp[0] == plane2.x and temp[1] == plane2.y:
                        self.grid_list1[temp[0]][temp[1]].color = 2
                    else:
                        self.grid_list1[temp[0]][temp[1]].color = 1
                break

        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 4 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 4 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if x + 2 <= 9 and x - 2 >= 0 and y - 4 >= 0:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane2 = Flight2(x, y, dire)

            # 用flight_place中每一个元素遍历整个格子
            for temp in plane2.flight_place:
                overlap = 0
                if self.grid_list2[temp[0]][temp[1]].color != 0:
                    overlap = 1
                    break
            if overlap == 0:
                for temp in plane2.flight_place:
                    if temp[0] == plane2.x and temp[1] == plane2.y:
                        self.grid_list2[temp[0]][temp[1]].color = 2
                    else:
                        self.grid_list2[temp[0]][temp[1]].color = 1
                break
    # 添加第二种飞机

    def add_flight3(self):
        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 4 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 4 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if x + 2 <= 9 and x - 2 >= 0 and y - 4 >= 0:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane3 = Flight3(x, y, dire)
            # 用flight_place中每一个元素遍历整个格子
            for temp in plane3.flight_place:
                overlap = 0
                if self.grid_list1[temp[0]][temp[1]].color != 0:
                    overlap = 1
                    break
            if overlap == 0:
                for temp in plane3.flight_place:
                    if temp[0] == plane3.x and temp[1] == plane3.y:
                        self.grid_list1[temp[0]][temp[1]].color = 2
                    else:
                        self.grid_list1[temp[0]][temp[1]].color = 1
                break

        while True:
            while True:
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                dire = r.randint(1, 4)
                if dire == 1:
                    if x + 2 <= 9 and x - 2 >= 0 and y + 4 <= 9:
                        break
                elif dire == 2:
                    if y - 2 >= 0 and x - 4 >= 0 and y + 2 <= 9:
                        break
                elif dire == 3:
                    if x + 2 <= 9 and x - 2 >= 0 and y - 4 >= 0:
                        break
                elif dire == 4:
                    if y - 2 >= 0 and x + 4 <= 9 and y + 2 <= 9:
                        break
            plane3 = Flight3(x, y, dire)
            # 用flight_place中每一个元素遍历整个格子
            for temp in plane3.flight_place:
                overlap = 0
                if self.grid_list2[temp[0]][temp[1]].color != 0:
                    overlap = 1
                    break
            if overlap == 0:
                for temp in plane3.flight_place:
                    if temp[0] == plane3.x and temp[1] == plane3.y:
                        self.grid_list2[temp[0]][temp[1]].color = 2
                    else:
                        self.grid_list2[temp[0]][temp[1]].color = 1
                break
    # 添加第三种飞机

    def game_event_handler(self):  # 事件监测
        global x1, y1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("退出游戏")
                pg.quit()
                exit()
            # 退出游戏
            if self.head1 < self.head_to_find and self.head2 < self.head_to_find:
                if self.turn == 1:
                    self.game.add(my_turn1)
                    self.game.update()
                    self.game.draw(screen)
                    pg.display.update()
                    if event.type == MOUSEBUTTONDOWN:
                        x, y = pg.mouse.get_pos()
                        # print(x, y)
                        if 180 <= x <= 580 and 150 <= y <= 550:
                            # print("点中了")
                            if self.time == 0:
                                i = (x - 180) // 40
                                j = (y - 150) // 40
                                x1 = i
                                y1 = j
                                # print(x1, y1)
                                if self.grid_list1[i][j].value == 0:
                                    # print("没翻过")
                                    choose.rect.x = self.grid_list1[i][j].x - 4
                                    choose.rect.y = self.grid_list1[i][j].y - 5
                                    self.game.add(choose)
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()
                                    self.time += 1
                            elif self.time == 1:
                                choose.kill()
                                i = (x - 180) // 40
                                j = (y - 150) // 40
                                # print("翻过了")
                                # print(x1, y1)
                                if i == x1 and j == y1:
                                    # print("同一个")
                                    self.grid_list1[i][j].value = 1
                                    self.turn = 2
                                    my_turn1.kill()
                                    if self.grid_list1[i][j].color == 0:
                                        white = Element("./image/s_white.png")
                                        white.rect.x = self.grid_list1[i][j].x
                                        white.rect.y = self.grid_list1[i][j].y
                                        self.game.add(white)
                                        # print("白")
                                    elif self.grid_list1[i][j].color == 1:
                                        blue = Element("./image/s_blue.png")
                                        blue.rect.x = self.grid_list1[i][j].x
                                        blue.rect.y = self.grid_list1[i][j].y
                                        self.game.add(blue)
                                    elif self.grid_list1[i][j].color == 2:
                                        red = Element("./image/s_red.png")
                                        red.rect.x = self.grid_list1[i][j].x
                                        red.rect.y = self.grid_list1[i][j].y
                                        self.game.add(red)
                                        self.head1 += 1
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()
                                    self.time = 0
                                else:
                                    x1 = i
                                    y1 = j
                                    choose.rect.x = self.grid_list1[i][j].x - 4
                                    choose.rect.y = self.grid_list1[i][j].y - 5
                                    self.game.add(choose)
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()
                    if self.head1 == self.head_to_find:
                        self.winner = 1
                        self.finish1 = 1
                        break

                elif self.turn == 2:
                    self.game.add(my_turn2)
                    self.game.update()
                    self.game.draw(screen)
                    pg.display.update()
                    if event.type == MOUSEBUTTONDOWN:
                        x, y = pg.mouse.get_pos()
                        # print(x, y)
                        if 700 <= x <= 1100 and 150 <= y <= 550:
                            # print("点中了")
                            if self.time == 0:
                                i = (x - 700) // 40
                                j = (y - 150) // 40
                                x1 = i
                                y1 = j
                                # print(x1, y1)
                                if self.grid_list2[i][j].value == 0:
                                    # print("没翻过")
                                    choose.rect.x = self.grid_list2[i][j].x - 4
                                    choose.rect.y = self.grid_list2[i][j].y - 5
                                    self.game.add(choose)
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()
                                    self.time += 1
                            elif self.time == 1:
                                choose.kill()
                                i = (x - 700) // 40
                                j = (y - 150) // 40
                                # print(x1, y1)
                                if i == x1 and j == y1:
                                    # print("同一个")
                                    self.grid_list2[i][j].value = 1
                                    self.turn = 1
                                    my_turn2.kill()
                                    if self.grid_list2[i][j].color == 0:
                                        white = Element("./image/s_white.png")
                                        white.rect.x = self.grid_list2[i][j].x
                                        white.rect.y = self.grid_list2[i][j].y
                                        self.game.add(white)
                                        # print("白")
                                    elif self.grid_list2[i][j].color == 1:
                                        blue = Element("./image/s_blue.png")
                                        blue.rect.x = self.grid_list2[i][j].x
                                        blue.rect.y = self.grid_list2[i][j].y
                                        self.game.add(blue)
                                    elif self.grid_list2[i][j].color == 2:
                                        red = Element("./image/s_red.png")
                                        red.rect.x = self.grid_list2[i][j].x
                                        red.rect.y = self.grid_list2[i][j].y
                                        self.game.add(red)
                                        self.head2 += 1
                                        # print("红")
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()
                                    self.time = 0
                                else:
                                    x1 = i
                                    y1 = j
                                    choose.rect.x = self.grid_list2[i][j].x - 4
                                    choose.rect.y = self.grid_list2[i][j].y - 5
                                    self.game.add(choose)
                                    self.game.update()
                                    self.game.draw(screen)
                                    pg.display.update()

                    if self.head2 == self.head_to_find:
                        self.winner = 2
                        self.finish2 = 1
                        break

    def start_game(self):
        self.__init_grid()
        if self.game_mode == 1:
            self.add_flight1()
            self.add_flight1()
        if self.game_mode == 2:
            self.add_flight2()
            self.add_flight2()
        if self.game_mode == 3:
            self.add_flight1()
            self.add_flight2()
            self.add_flight3()
        # print("游戏开始")
        while self.finish1 == 0 and self.finish2 == 0:
            self.clock.tick(60)
            self.game_event_handler()
        # print("游戏结束")
