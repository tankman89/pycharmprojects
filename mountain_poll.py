# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/3/25
# 调查结果
responses = {}
# 设置一个标志,指出调查是否继续
polling_active = True
# 可供选择的出行方式
trip_mode = ['步行', '驾车', '公交', '叫车']
while polling_active:
    # 提示被调查者输入用户名和回答
    name = input('\n请说下您的名字：')
    if name:
        print(*trip_mode, sep=',', end='。')
        response = input('\n请问您出行最愿意选择以上哪种交通方式呢？')
    # 将答案存储再字典中
    # 直接对字典的键和值进行定义
    responses[name] = response

    # 请问还有人愿意参加调查吗
    repeat = input('请问还有人愿意参加调查吗？（yes/no）')
    if repeat == 'no':
        polling_active = False
print('\n---调查结果---')
for name, response in responses.items():
    print(name + '出行更喜欢选择：' + response + '。')
