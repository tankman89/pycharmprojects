# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/1

import pizza

pizza.make_pizza('16寸', '番茄')
pizza.make_pizza('20寸', '番茄', '牛肉', '芝士', location='厦岭路8号')

check_out = input('请问需要结账吗？（是的/不）')
if check_out == '是的':
    print('祝您用餐愉快！')

pizza.price_pizza('番茄', '牛肉')