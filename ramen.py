#储存拉面相关的所有信息
ramen = {
    '粗细':'二细',
    '加料':['辣椒','香菜','白萝卜']
}
print('您点拉面粗细是',ramen['粗细'],'您要的加料有',sep='',end='：')

for topping in ramen['加料']:
    if topping != '白萝卜':
        print(topping,end = '，')
    else:
        print(topping,end = '。')
