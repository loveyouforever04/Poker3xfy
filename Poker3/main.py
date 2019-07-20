# test 

import time
# import our modules
from display.menu import *
from machine.std_mach import *
from dealer.mike import*
# Phase 1-----------------------------------------------------------------------
# 打印开始界面
dsp_start()
time.sleep(1)  # 延迟3秒
# Phase 2-----------------------------------------------------------------------
# 打印选择游戏玩法界面
game_type = dsp_choice_game()

deck = []
make_deck_by_type(game_type,deck)
print(deck)
# Phase 4-----------------------------------------------------------------------
# 预先准备4+1个位置放牌
player_a = []
player_b = []
player_c = []
player_d = []
player_dumy = []  # 放置预留牌的位置

# 按游戏类型发牌
if game_type == 1:
    deal_to_multi_players(deck, player_a, player_b, player_c)
    record_deck(player_a, '争上游01副牌.txt')
    record_deck(player_b, '争上游02副牌.txt')
    record_deck(player_c, '争上游03副牌.txt')

if game_type == 2:
    deal_to_multi_players(deck, player_a, player_b, player_c, player_d)
    record_deck(player_a, "桥牌01.txt")
    record_deck(player_b, "桥牌02.txt")
    record_deck(player_c, "桥牌03.txt")
    record_deck(player_d, "桥牌04.txt")

if game_type == 3:
    deal_to_multi_players_remain(deck, 3,player_dumy,player_a, player_b, player_c)
    record_deck(player_a, "三人斗地主-牌01.txt")
    record_deck(player_b, "三人斗地主-牌02.txt")
    record_deck(player_c, "三人斗地主-牌03.txt")
    record_deck(player_dumy, "三人斗地主-牌预留.txt")

if game_type == 4:
    deal_to_multi_players_remain(deck, 8,player_dumy,player_a, player_b, player_c)
    record_deck(player_a, "四人斗地主-牌01.txt")
    record_deck(player_b, "四人斗地主-牌02.txt")
    record_deck(player_c, "四人斗地主-牌03.txt")
    record_deck(player_dumy, "四人斗地主-牌预留.txt")
