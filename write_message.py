# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/7

filename = 'E:/text_files/programming.txt'

with open(filename, 'r+') as file_object:
    file_object.write('这个世界会好吗？\n')
    file_object.write('会的，一切都会好的！\n')

with open(filename, 'a') as file_object:
    file_object.write('因为我选择学习编程，\n')
    file_object.write('在大数据中寻找意义！')
#
with open(filename) as file_object:
    writefile = file_object.read()
    print(writefile)

