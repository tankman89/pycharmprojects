available_toppings = ['香菜','辣椒','红油','糖蒜','青椒','青菜']
requested_toppings = ['辣椒','红油','番茄']
# requested_toppings =['香菜']
# if '香菜' in requested_toppings:
#     print('要求加香菜!')
# if '辣椒' in requested_toppings:
#     print('要求加辣椒!')
# for requested_topping in requested_toppings:
#     if requested_topping == '青椒':
#         print('抱歉.青椒没有了!,可以换成青菜吗?')
#     else:
#         print('要求加'+ requested_topping+'!')
# print('您的拉面已经制作好了!')
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print('要求加' + requested_topping + '!')
#         print('您的拉面已经制作好了!')
# else:
#     print('您点的清汤拉面马上好!')
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('要求加'+ requested_topping + '!')
    else:
        print('抱歉,您要加的'+requested_topping+'本店没有!'+'\n')
print('您的拉面已经制作好了!')
