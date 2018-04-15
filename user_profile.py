# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/1


def build_profile(**user_info):
    """创建一个字典，其中包含所知道的用户的一切信息"""
    profile = {}
    # profile['first_name'] = first
    # profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(name='王小二',
                             location='中原路5号',
                             field='足球')
print(user_profile)
