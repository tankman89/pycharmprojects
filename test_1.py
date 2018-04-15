# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/1


def price_pizza(*toppings):
    # toppings_price = {'番茄': 2, '牛肉': 5, '芝士': 6}
    # size_price = {'16寸': 20, '20寸': 25}
    topping_price = 0
    # price = 0
    for current_price in toppings:
        while current_price == '番茄':
            topping_price += 2
        while current_price == '牛肉':
            topping_price += 5
            break
        return current_price


price = price_pizza('番茄', '牛肉')
print(price)
