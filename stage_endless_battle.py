import sys
import random as r
import pygame as pg
from sprites_class import *
from ElementsAndGroup import *
from datetime import datetime
from threading import Timer
import time as t
from game_main import *
# screen = pg.display.set_mode((1280, 720))


def num_to_pic(num):
    pics = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        20: twenty,
        30: thirty,
        40: forty,
        50: fifty,
        60: sixty,
        70: seventy,
        80: eighty,
        90: ninety
    }

    return pics.get(num, None)


def num_to_score1(num):
    pics = {
        0: b_zero1,
        1: b_one1,
        2: b_two1,
        3: b_three1,
        4: b_four1,
        5: b_five1,
        6: b_six1,
        7: b_seven1,
        8: b_eight1,
        9: b_nine1,
        10: b_ten1,
        20: b_twenty1,
        30: b_thirty1,
        40: b_forty1,
        50: b_fifty1,
        60: b_sixty1,
        70: b_seventy1,
        80: b_eighty1,
        90: b_ninety1
    }

    return pics.get(num, None)


def num_to_score2(num):
    pics = {
        0: b_zero2,
        1: b_one2,
        2: b_two2,
        3: b_three2,
        4: b_four2,
        5: b_five2,
        6: b_six2,
        7: b_seven2,
        8: b_eight2,
        9: b_nine2,
        10: b_ten2,
        20: b_twenty2,
        30: b_thirty2,
        40: b_forty2,
        50: b_fifty2,
        60: b_sixty2,
        70: b_seventy2,
        80: b_eighty2,
        90: b_ninety2
    }

    return pics.get(num, None)


stage = 1
the_round = pg.sprite.Group()


def print_the_round():
    global stage, the_round
    if stage <= 9:
        the_round = pg.sprite.Group(round_bg, num_to_pic(stage))
    elif stage > 9:
        stage1 = stage//10*10
        stage2 = stage - stage1
        the_round = pg.sprite.Group(round_bg, num_to_pic(stage1), num_to_pic(stage2))
    the_round.update()
    the_round.draw(screen)
    pg.display.update()


def stage_game():
    global stage
    stage = 1
    print_the_round()
    stage_mode = MainGame(1, (stage - 1) // 10 + 1, 26-stage+(stage-1)//10*10)
    while stage_mode.pass_the_round == 1:
        t.sleep(1)
        after_round = pg.sprite.Group(after_round_bg)
        stage_mode.game_mode = (stage - 1) // 10 + 1
        if stage_mode.game_mode == 1:
            stage_mode.max_step = 26-stage
            after_round.add(flight1_1, flight1_2)
        if stage_mode.game_mode == 2:
            stage_mode.max_step = 26 - stage + 10
            after_round.add(flight2_1, flight2_2)
        if stage_mode.game_mode == 3:
            stage_mode.max_step = 26 - stage + 20
            after_round.add(flight1_1, flight2_2, flight3)
        after_round.update()
        after_round.draw(screen)
        pg.display.update()
        t.sleep(2)
        # print(stage_mode.game_mode)
        stage_mode.start_game()
        # print(stage_mode.pass_the_round)
        if stage_mode.pass_the_round == 1:
            # print("过关了")
            stage += 1
            # print(stage)
            t.sleep(1)
            if stage == 31:
                stage_mode.game.add(clear)
                stage_mode.game.update()
                stage_mode.game.draw(screen)
                pg.display.update()
                t.sleep(2)
                menu.update()
                menu.draw(screen)
                pg.display.update()
                stage_mode.pass_the_round = 0
            else:
                stage_mode.game.add(next_stage)
                stage_mode.game.update()
                stage_mode.game.draw(screen)
                pg.display.update()
                t.sleep(1)
                print_the_round()
        elif stage_mode.pass_the_round == 0:
            t.sleep(1)
            lose = pg.sprite.Group(you_lose)
            lose.update()
            lose.draw(screen)
            pg.display.update()
            t.sleep(1)
            menu.update()
            menu.draw(screen)
            pg.display.update()


def endless_game():
    global stage
    stage = 1
    print_the_round()
    endless_mode = MainGame(2, r.randint(1, 3), 101)
    quit_endless = 0
    while quit_endless == 0:
        t.sleep(1)
        after_round = pg.sprite.Group(after_round_bg)
        endless_mode.game_mode = r.randint(1, 3)
        if endless_mode.game_mode == 1:
            after_round.add(flight1_1, flight1_2)
        if endless_mode.game_mode == 2:
            after_round.add(flight2_1, flight2_2)
        if endless_mode.game_mode == 3:
            after_round.add(flight1_1, flight2_2, flight3)
        after_round.update()
        after_round.draw(screen)
        pg.display.update()
        t.sleep(2)
        # print(endless_mode.game_mode)
        endless_mode.start_game()
        # print(endless_mode.pass_the_round)
        # print("过关了")
        stage += 1
        # print(stage)
        endless_mode.game.add(back_but)
        endless_mode.game.update()
        endless_mode.game.draw(screen)
        pg.display.update()
        done = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print("退出游戏")
                    pg.quit()
                    exit()
                # 退出游戏
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if 1100 <= x <= 1200 and 550 <= y <= 648:
                        quit_endless = 1
                    done = 1
            if done == 1:
                break
        if quit_endless == 0:
            endless_mode.game.add(next_stage)
            endless_mode.game.update()
            endless_mode.game.draw(screen)
            pg.display.update()
            t.sleep(1)
            print_the_round()

        elif quit_endless == 1:
            menu.update()
            menu.draw(screen)
            pg.display.update()


def print_the_score():
    global score1, score2, score
    score = pg.sprite.Group(score_bg)
    if score1 <= 9:
        score.add(num_to_score1(score1))
    elif score1 > 9:
        score1_1 = score1//10*10
        score1_2 = score1 - score1_1
        score.add(num_to_score1(score1_1), num_to_score1(score1_2))
    if score2 <= 9:
        score.add(num_to_score2(score2))
    elif score2 > 9:
        score2_1 = score2//10*10
        score2_2 = score2 - score2_1
        score.add(num_to_score2(score2_1), num_to_score2(score2_2))
    score.add(back_but)
    score.update()
    score.draw(screen)
    pg.display.update()


def battle_game():
    global stage, score1, score2
    stage = 1
    print_the_round()
    t.sleep(1)
    score1 = 0
    score2 = 0
    quit_battle = 0
    while quit_battle == 0:
        mode_choosing_page.update()
        mode_choosing_page.draw(screen)
        pg.display.update()
        break_while = 0
        while break_while == 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print("退出游戏")
                    pg.quit()
                    exit()
                # 退出游戏
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    b_mode = 0
                    if 150 <= x <= 450 and 300 <= y <= 560:
                        b_mode = 1
                        break_while = 1
                    if 460 <= x <= 760 and 300 <= y <= 579:
                        b_mode = 2
                        break_while = 1
                    if 770 <= x <= 1130 and 300 <= y <= 599:
                        b_mode = 3
                        break_while = 1
        battle_mode = BattleMainGame(b_mode)
        battle_mode.start_game()
        if battle_mode.winner == 1:
            battle_mode.game.add(win1)
            score1 += 1
        if battle_mode.winner == 2:
            battle_mode.game.add(win2)
            score2 += 1
        battle_mode.game.update()
        battle_mode.game.draw(screen)
        pg.display.update()
        stage += 1
        t.sleep(1)
        if battle_mode.winner == 1:
            win1.kill()
        if battle_mode.winner == 2:
            win2.kill()
        battle_mode.game.update()
        battle_mode.game.draw(screen)
        print_the_score()
        # print(stage)
        t.sleep(1)
        break_while = 0
        while break_while == 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print("退出游戏")
                    pg.quit()
                    exit()
                # 退出游戏
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if 1100 <= x <= 1200 and 550 <= y <= 648:
                        quit_battle = 1
                        menu.update()
                        menu.draw(screen)
                        pg.display.update()
                    break_while = 1
        if quit_battle == 0:
            battle_mode.game.add(next_stage)
            battle_mode.game.update()
            battle_mode.game.draw(screen)
            pg.display.update()
            t.sleep(1)
            print_the_round()
            t.sleep(1)

        elif quit_battle == 1:
            t.sleep(1)
            menu.update()
            menu.draw(screen)
            pg.display.update()
