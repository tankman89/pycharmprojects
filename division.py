# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/7

print('给我两个数字，我将把他们两个相除！')
print("输入'退出'退出！")

while True:
    first_number = input('\n请输入第一个数字')
    if first_number == '退出':
        break
    second_number = input('\n请输入第二个数字')
    if second_number == '退出':
        print('\n回头见！')
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('您不能除以0！')
    else:
        print(answer)
