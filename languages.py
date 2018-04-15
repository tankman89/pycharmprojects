favlrite_languages = {
    '杜老师':'Java',
    '孙老师':'python',
    '牛老师':'C',
    }
x = ['杜老师','李老师','张老师']
for x in x:
    if x in favlrite_languages:
        print('感谢', x ,'参与调查',end='。',sep='')
    else:
        print('\n欢迎', x , '参与调查',end='。',sep='')





# print('杜老师最喜欢的编程语言是:' +
#       favlrite_languages['杜老师'] +
#       '。'
#       )
