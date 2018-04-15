# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/3/25
# 创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['丹丹', '珂珂', '威威']
confirmed_users = []

# 每个用户,直到没有未验证的用户为止
# 将验证后的用户添加到已验证用户列表中

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print('需要验证的用户：' + current_users.title())
    confirmed_users.append(current_users)
# 显示所有已验证的用户
print('\n以下用户已经全部验证：')
for confirmed_user in confirmed_users:
    print(confirmed_user.title(), end=' ')
