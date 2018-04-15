list=['陈长庚','孙喜梅','孙斌','李小静','邹喆','杨晓娜']
print(list[0].title())#访问列表元素，并对其修改输出首字母大写
message=list[-1]+'是我在车辆教研室的同事！'#显示倒数第一个元素
print(message)

list[0]='曹鹏'#修改列表元素
print(list)
list.append('刘华莉')#在列表末尾添加元素
print(list)

list=[]#在空白列表中添加元素
list.append('张三')
list.append('李四')
list.append('王二麻子')
print(list)
#在列表中插入元素
list=['陈长庚','孙喜梅','李小静','孙斌','邹喆','杨晓娜']
list.insert(1,'张三')
print(list)
#删除列表中元素
del list[0]
print(list)
#弹出列表中最后一个元素，并且把这个元素储存入一个变量
list=['陈长庚','孙喜梅','李小静','孙斌','王春燕','邹喆','杨晓娜']
last_join=list.pop()
first_join=list.pop(0)
print(last_join+'老师是最后加入我们办公室的老师！欢迎她加入！')#使用弹出的元素
print(first_join+'老师是第一个加入我们办公室的老师！')#使用弹出元素

list.remove('王春燕')#不清楚元素位置，只根据元素信息对其进行删除
print(list)
leave_list='李小静'#删除元素值，并继续使用
list.remove(leave_list)
print(leave_list)
