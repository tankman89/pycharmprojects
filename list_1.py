dinner_list=['唐僧','孙悟空','猪八戒','沙和尚','白龙马']
#参加今天晚宴的名单
print('今天参加晚宴的名单有',end='')
print(*dinner_list,sep=',',end='。')
print()
message=dinner_list.remove('唐僧')
print('由于工作关系，唐僧今天无法参加晚宴。')#指出某位嘉宾无法参加晚宴
dinner_list.insert(0,'白骨精')#将无法出席的唐僧更换成白骨精
print('现将唐僧更换为白骨精，下面是最新的人员名单')
print('最新的人员名单：',end='')
print(*dinner_list,sep=',',end='。')
print('\n'*0)#换一行，不空行
print('请'+str(dinner_list)+'先生准时在老地方参加晚宴。')#向每一位人员发出邀请
print('\n'*0)
print('有一桌客人退订了，空出一张更大的餐桌，我将邀请：红孩儿，牛魔王，铁扇公主一家参加。')
dinner_list.insert(1,'红孩儿')#将一位新嘉宾添加到名单开头
dinner_list.insert(3,'牛魔王')#将一位新嘉宾添加到名单中间
dinner_list.insert(9, '铁扇公主')
print('新的人员名单是：',end='')
print(*dinner_list,sep=' ',end='。')
print('\n')
print('紧急通知:由于餐桌损坏，只能有两名嘉宾参加！')#通知每一位嘉宾无法参加今天的晚宴
cannot=dinner_list.pop(0)
print(cannot+'先生很抱歉，无法邀请您来共进晚餐！')
cannot=dinner_list.pop(0)
print(cannot+'先生很抱歉，无法邀请您来共进晚餐！')
cannot=dinner_list.pop(0)
print(cannot+'先生很抱歉，无法邀请您来共进晚餐！')
cannot=dinner_list.pop(0)
print(cannot+'先生很抱歉，无法邀请您来共进晚餐！')
cannot=dinner_list.pop(1)
print(cannot+'先生很抱歉，无法邀请您来共进晚餐！')
cannot=dinner_list.pop(1)
print(cannot+'先生很抱歉，无法邀请您来共进晚餐！')
print(dinner_list)
print(dinner_list[0]+'先生和'+dinner_list[1]+'女士很高兴通知您参加今天的晚宴')
del dinner_list[0]
del dinner_list[0]
print('晚宴结束了，宴会名单上只有'+str(dinner_list)+'人。')