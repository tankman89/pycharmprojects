# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/3/24
topping_list = ['香菜', '辣椒', '红油', '糖蒜', '青椒', '青菜']
print(*topping_list, sep=',', end='。')
topping_1 = input('\n请问您要选择上面哪些配料:')
available_topping = []
while topping_1:
    if topping_1 in topping_list:
        available_topping.append(topping_1)
        print('\n好的！给您加上', end='：')
        print(*available_topping, sep=' ', end='。')
        topping_1 = input('\n\n您看还要添加什么配料？')
    if topping_1 == '我选好了':
        print('这是您要点的配料', end='：')
        print(*available_topping, sep=',', end='。')
        en = input('\n如果是的话,请确认！')
        if en == '确认':
            print('\n一碗拉面！加上', end='')
            print(*available_topping, end='。')
            print('马上就来！')
            break
    if topping_1 not in topping_list:
        print('对不起！我们没有' + topping_1, end='。')
        topping_1 = input('\n请继续选择:')
        continue



