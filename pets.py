# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/3/25


def describe_pet(pet_name, animal_type='小狗'):
    """显示宠物信息"""
    print('\n我有一只' + animal_type + '。')
    print('我' + animal_type + '的名字叫' + pet_name + '。')


def build_person(first_name, last_name, age='25'):
    person = {'姓': first_name, '名': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('张', '炬')
surname = musician['姓']
name = musician['名']
age_1 = musician['age']
print('唐朝乐队的贝斯手' + surname + name + '永远活在' + age_1 + '岁' + '。')



# # 位置实参
# describe_pet('黑子')
# describe_pet('丸子', '萨摩耶')
# # 关键字实参
# describe_pet(animal_type='仓鼠', pet_name='哆啦A梦')
# describe_pet(pet_name='阿黄')
#

