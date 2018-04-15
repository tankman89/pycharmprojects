# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/3/31


def make_pizza(size, *toppings, location='市中心'):
    """概述要制作的比萨
    添加*后,可以向函数传递任意数量的实参
    首先匹配位置实参,和关键字实参,剩余的都交给最后一个形参中
    """
    print('\n\n您要的比萨尺寸是：' + size)
    print('在比萨上面添加有浇头：')
    for topping in toppings:
        print('-' + topping)
    print('马上给您送货到' + location, end='。')


def price_pizza(*toppings):
    # toppings_price = {'番茄': 2, '牛肉': 5, '芝士': 6}
    # size_price = {'16寸': 20, '20寸': 25}
    toppings = []
    toppings.append(toppings)
    topping_price = 0
    price = 0
    for current_price in toppings:
        if current_price == '番茄':
            price = topping_price + 2
        if current_price == '牛肉':
            price = topping_price + 2
    print(price)






