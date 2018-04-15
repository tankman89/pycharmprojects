players =['孙杨','孔令辉','刘国梁','傅园慧','邓亚萍']
players[-2] ='张怡宁' #替换掉列表中某值,可以直接赋值
print('以下女运动员都曾经在奥运拿过金牌:')
# x = [players for players in players[3:]]#列表解析是形成新列表
# print(x)
for players in players[-2:]:
     print(players)