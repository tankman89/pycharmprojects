myfoods=['花生','饺子','火锅']
friend_foods=['馒头','花卷','卤面']
print ('我最爱吃的东西有：',*myfoods,'。')
for myfoods_1 in myfoods[:]:
    friend_foods.append(myfoods_1)
print('我朋友最爱吃的东西有',end='：')
print (*friend_foods,sep=',',end='。')
# print('我朋友最爱吃的食物是:'.join(friend_foods)+'。')


