cars=['思域','索纳塔','福克斯','宝来']
#cars.sort()#永久性排序，应用在list
print(cars)
#cars.sort(reverse=True)#降序排列
print(cars)
print(sorted(cars,reverse=True))#临时降序排列，对所有迭代对象进行排序
#print(cars)
cars.reverse()#永久翻转元素顺序打印
print(cars)
cars.reverse()#可以继续翻转回来
print(cars)
#print(cars.reverse())#降序列表 ,无返回值
#cars.reverse()#再次降序列表
#print(cars)#输出正序
#list(reversed(cars))

