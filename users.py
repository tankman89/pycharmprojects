current_users = ['王二小','王麻子','小李子','达尔文']
new_users = ['张三','王五','小李子']
for new_user in new_users:
    if new_user in current_users:
        print('对不起',new_user,'这个名字已经被使用!',sep='')
    else:
        print(new_user + '这个名字可以用!')
