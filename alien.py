alien_0 = {'颜色':'蓝色','点数':5}
# new_point = alien_0['点数']
# print('你刚刚杀死的外星人,获得了' + str(alien_0['点数']) + '分!')
alien_0['x_位置'] = 0
alien_0['y_位置'] = 25
alien_0['运动速度'] = '中等'
alien_0['运动速度'] = '快'
# print('(' + str(alien_0['x_位置']),str(alien_0['y_位置']) + ')',sep=',')
print("原来x_位置:" + str(alien_0['x_位置']))
if alien_0['运动速度'] == '慢':
    x_increment = 1
elif alien_0['运动速度'] == '中等':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_位置'] = alien_0['x_位置'] + x_increment

print('新的x_位置:' + str(alien_0['x_位置']))
del alien_0['颜色']
print(alien_0)