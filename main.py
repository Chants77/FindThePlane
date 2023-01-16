import pygame as pg
import sys
import random as r
from pygame.locals import *
from sprites_class import *
from ElementsAndGroup import *
from stage_endless_battle import *
from game_main import *
# layer
# 1 封面
# 2 menu
# 21 stage
# 22 endless
# 23 battle
# 24 rule1
# 242 rule2


def back_to_menu():
    global layer
    menu.update()
    menu.draw(screen)
    music_but.add(is_music_but)
    music_but.draw(screen)
    layer = 2
    pg.display.update()
# 回到菜单界面


click = 0
music = 1
layer = 1


def menu_part():
    menu_event_handler()
    global click, layer, music
    if click == 1:
        x, y = pg.mouse.get_pos()
        if layer == 1:
            if 950 <= x <= 1184 and 480 <= y <= 582:
                back_to_menu()
        # 开始
        elif layer == 2:
            if 470 <= x <= 870 and 150 <= y <= 250:
                layer = 21
                stage_game()
                layer = 2
                # print(layer)
            elif 470 <= x <= 870 and 300 <= y <= 400:
                layer = 22
                endless_game()
                layer = 2
            elif 470 <= x <= 870 and 450 <= y <= 550:
                layer = 23
                battle_game()
                layer = 2
            elif 1080 <= x <= 1219 and 480 <= y <= 614:
                rule1.update()
                rule1.draw(screen)
                layer = 24
                pg.display.update()
            # 进入游戏规则界面
            elif 1100 <= x <= 1224 and 5 <= y <= 127:
                # print("点中了")
                if music == 1:
                    music = 0
                    is_music_but.kill()
                    # print("关掉了")
                    music_but.add(no_music_but)
                    music_but.draw(screen)
                    pg.mixer.music.pause()
                    pg.display.update()
                elif music == 0:
                    music = 1
                    no_music_but.kill()
                    # print("开了")
                    music_but.add(is_music_but)
                    music_but.draw(screen)
                    pg.mixer.music.unpause()
                    pg.display.update()
        elif layer == 24:
            if 20 <= x <= 100 and 20 <= y <= 100:
                back_to_menu()
            # 关闭游戏规则界面
            if 1100 <= x <= 1200 and 550 <= y <= 648:
                rule2.update()
                rule2.draw(screen)
                layer = 242
                pg.display.update()
            # 跳转到第二页
        elif layer == 242:
            if 1100 <= x <= 1200 and 550 <= y <= 648:
                rule1.update()
                rule1.draw(screen)
                layer = 24
                pg.display.update()
            # 跳转到第一页
            elif 20 <= x <= 100 and 20 <= y <= 100:
                back_to_menu()
            # 关闭游戏规则界面
        click = 0


def menu_event_handler():  # 事件监测
    global layer
    global click
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("退出游戏")
            pg.quit()
            exit()
        # 退出游戏
        if event.type == MOUSEBUTTONDOWN:
            click = 1


def main():
    pg.init()  # 游戏初始化
    pg.mixer.init()
    pg.mixer.music.load("./music/bg_music.mp3")
    pg.mixer.music.play()
    icon = pg.image.load("./image/icon.ico")
    pg.display.set_icon(icon)
    pg.display.set_caption("FindThePlane")
    pg.mixer.music.load("./music/bg_music.mp3")
    pg.mixer.music.play(-1)

    cover.update()
    cover.draw(screen)
    pg.display.update()

    # 计时器
    clock = pg.time.Clock()

    while True:
        clock.tick(60)
        menu_part()

    pg.quit()


if __name__ == "__main__":
    main()
