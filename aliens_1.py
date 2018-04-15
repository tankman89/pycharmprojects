aliens = [] #创建一个用于储存外星人的空列表
# 创建10个绿色的外星人
for alien_number in range(10):
    new_alien = {'颜色':'蓝色','分数':'2','速度':'慢速'}
    aliens.append(new_alien)
for alien_number in range(5):
    new_alien = {'颜色':'黄色','分数':'5','速度':'快速'}
    aliens.append(new_alien)

#将前三个蓝色外星人改为金色
for alien in aliens[:3]:
    if alien['颜色'] == '蓝色':
        alien['颜色'] = '金色'
        alien['分数'] = '10'
        alien['速度'] = '极速'
# 将前三个蓝色外星人改为金色
for alien in aliens[-5:]:
    if alien['颜色'] == '黄色':
        alien['颜色'] = '红色'
        alien['分数'] = '8'
        alien['速度'] = '急速'
# 显示前十五个外星人
for alien in aliens[:15]:
    print(alien)
print("...")