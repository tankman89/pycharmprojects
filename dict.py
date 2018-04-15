favorite_foods = ['麻辣烫','串串香','酸奶','烤面筋']
wang = {
    '姓':'段',
    '名':'雪丹',
    '年龄':'28',
    '家庭住址':'温莎花园',
    '喜欢的食物':favorite_foods,
    }
print(wang['姓'] + wang['名'] + '不想锻炼身体,想放弃,想吃的东西有',end=':')
for favorite_food in favorite_foods:
    if favorite_food != '烤面筋':
        print(favorite_food,end=',')
    else:
        print(favorite_food,end='。')
    # if favorite_food == '麻辣烫':
    #     print(favorite_food,end='。')
    # if favorite_food == '酸奶':
    #     print('\n其实我自己会做酸奶!')