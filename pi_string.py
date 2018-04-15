# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/6
filename = 'e:/text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
birthday = input('请输入你的出生日期,看看是不是在π里面:')
if birthday in pi_string:
    print('恭喜您！您的生日在π里面。')
else:
    print('您的生日不在π的前一百万位置里面！')
# print(pi_string[0])
# print(len(pi_string))
