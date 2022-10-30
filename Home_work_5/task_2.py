#  Создайте программу для игры с конфетами человек против человека.
#  Условие задачи: На столе лежит 2021 конфета.
#  Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать
#  все конфеты у своего конкурента?


import random

def game_friends_vs_friends(total_sweets, max_number_move, players):
    count = 0
    curr_player = random.randint(0, 1)
    while total_sweets > 0:
        print(f'{players[curr_player]}, ваш ход. Сколько конфет берете?')
        if curr_player == 0: curr_player = 1
        else: curr_player = 0
        move = int(input())
        if move > total_sweets or move > max_number_move:
            print(f'Можно взять не более {max_number_move} конфет, у нас всего {total_sweets} конфет.')
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                move = int(input())
                chance -= 1
            else:
                return print(f'Попыток не осталось. Game over!')
        total_sweets = total_sweets - move
        if total_sweets > 0: print(f'Осталось {total_sweets} конфет.')
        else: print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]
 
player1 = input('Первый игрок, Ваше имя?\n')
player2 = input('Второй игрок, Ваше имя?\n')
players = [player1, player2]
 
total_sweets = 2021
max_number_move = 28

winer = game_friends_vs_friends(total_sweets, max_number_move, players)
if not winer:
    print('Победителя нет.')
else: print(f'Поздравляю! Победил {winer}!')