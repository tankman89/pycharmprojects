# alien_0 = {'颜色':'蓝色','分数':'2'}
# alien_1 = {'颜色':'黄色','分数':'5'}
# alien_2 = {'颜色':'红色','分数':'8'}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

aliens = [] #创建一个用于储存外星人的空列表
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'颜色':'蓝色','分数':'2','速度':'慢速'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print('\n总共出现的外星人总数：', str(len(aliens)))