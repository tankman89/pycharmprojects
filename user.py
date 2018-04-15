# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/10
import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    verify_name = input('请验证您的用户名？')
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            while True:
                if verify_name == username:
                    return username
                else:
                    verify_name = input('对不起，请重新输入！')
    except FileNotFoundError:
        print('对不起，查询不到您的用户信息！')
        return None


def get_new_username():
    """提示输入新的用户名"""
    username = input("请问您的姓名是？")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("欢迎回来 " + username + "！")
    else:
        username = get_new_username()
        print('当您回来的时候，我们会记得你的' + username + '！')



