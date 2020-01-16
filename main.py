from gameboard import GameObject
import random

board = GameObject()

coins_in_pocket = 100
coins = coins_in_pocket
bet_count = 0

bet = [
    {"bet":4,"color":GameObject.red},
    {"bet":10,"color":GameObject.yellow},
    {"bet":14,"color":GameObject.green},
    {"bet":30,"color":GameObject.blue},
    {"bet":29,"color":GameObject.pink},
]

color_result = board.getRandomColorResult()
print('\n\n')
print("Coins in pocket : {}, bets : {}, Coins left : {}".format(coins_in_pocket,bet_count,coins))

print('\n--------------Bets breakdown------------')
for b in bet:
    print('{} @ {} coins'.format(b['color'],b['bet']))
    bet_count += b['bet']
    coins -= b['bet']
print('----------------------------------------\n')


if coins > 0:
    if color_result.getIsBokya():
        print('Bokya')
        print('No Reward')
    else:
        for res in bet:
            if res['color'] == color_result:
                print('Color result : {} @ x{}'.format(color_result,color_result.getMultiplier()))
                print('Bet on color {} : {}'.format(res['color'],res['bet']))
                reward = board.getReward(res['bet'],res['color'])
                print('Result : {} x {} = {}'.format(res['bet'],res['color'].getMultiplier(),reward))
                print('Reward : {}'.format(reward))
                total_coins = coins + reward
                print('\nTotal Coins = {} ( Coins left ({}) + Coins reward ({}) )'.format(total_coins,coins,reward))
                print('\n\n')
                break
else:
    print('You placed bets more than {} coins'.format(coins_in_pocket))
