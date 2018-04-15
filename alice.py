# !/usr/bin/python3
# -*- coding:utf-8 -*-
# author:tank_man time:2018/4/7

filename = 'E:/text_files/alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = '对不起，没有找到' + filename + '。'
    print(msg)
else:
    # 计算文本包含有多少个单词
    words = contents.split()
    num_words = len(words)
    print(num_words)
    # 计算文本除去Alice还有多少个单词
while 'Alice' in words:
    words.remove('Alice')
if 'Alice' not in words:
    ex_alice_words = len(words)
    print(ex_alice_words)
    # 计算文本中含有多少个Alice
    alice_words = words.count('Alice')
    print(alice_words)






