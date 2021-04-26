import random
import sys
from typing import *


def get_score(name: str) -> int:
    """
    取得該使用者的預設分數。假如該使用者不存在，得分由0開始

    :param name: 使用者名稱
    :return: 該使用者得分
    """
    with open('rating.txt', 'r') as ratings:
        for person in ratings:
            if name == person.split(' ')[0]:
                return int(person.split(' ')[1].replace('\n', ''))
        else:
            return 0


def decide_win_overs(opts: List[str]) -> Dict[str, List[str]]:
    """
    當電腦選擇了玩家選擇的選項的後一半項目時，電腦贏

    :param opts: List[str]: 可選選項
    :return: Dict[str, List[str]]: 回傳的Dict的key是某個選項，value是該選項會被擊敗的項目
    """
    win_over_opt: Dict[str, Union[List[str], None]] = {}.fromkeys(opts)
    for index, opt in enumerate(opts):
        if index + len(opts) // 2 >= len(opts):
            win_over_opt[opt] = opts[index + 1:]
            win_over_opt[opt].extend(opts[: index - len(opts) // 2])
        else:
            win_over_opt[opt] = opts[index + 1: index + len(opts) // 2 + 1]
    return win_over_opt


name = input('Enter your name: ')
print(f'Hello, {name}')
score = get_score(name)
opts = input().split(',')
if len(opts) == 1 and opts[0] == '': opts = ['scissors', 'rock', 'paper']
win_over_opt = decide_win_overs(opts)
print("Okay, let's start")

while 1:
    inp = input()
    if inp == '!exit':
        print('Bye!')
        sys.exit(0)
    elif inp in opts:
        com_opt = random.choice(opts)
        if com_opt in win_over_opt[inp]:
            print('Sorry, but the computer chose {}'.format(com_opt))
        elif com_opt == inp:
            print('There is a draw ({})'.format(inp))
            score += 50
        else:
            print('Well done. The computer chose {} and failed'.format(com_opt))
            score += 100
    elif inp == '!rating':
        print(f'Your rating: {score}')
    else:
        print('Invalid input')