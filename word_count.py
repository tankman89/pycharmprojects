# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/7


def count_words(filename):
    # 计算一个文件大致包含多少个单词
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = '对不起，没有找到' + filename + '。'
        # print(msg)
        pass  # 异常的时候一声不吭
    else:
        # 计算文本包含有多少个单词
        words = contents.split()
        num_words = len(words)
        print('这个叫' + filename + '的文件大约有' + str(num_words) + '个单词。')


filenames = ['E:/text_files/alice.txt', 'E:/text_files/siddhartha.txt', 'E:/text_files/dict.txt']
for filename in filenames:
    count_words(filename)
# 如何才能读取文件名称


