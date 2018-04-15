users = {
    'tankman': {
        '姓': '孙',
        '名': '斌',
        '身份证地址': '郑州',
        '爱好': '',
    },
    'mcurie':{
        '姓': 'marie',
        '名': 'curie',
        '身份证地址': '纽约',
        '爱好': '篮球',
    },
}
for username, user_info in users.items():
    full_name = user_info['姓'].title() + user_info['名']
    location = user_info['身份证地址']
    hobby = user_info['爱好']
    if len(user_info['爱好']) == 0:
        print('用户名：' + username)
        print('名字是:' + full_name)
        print('家庭住址是:' + location)
    if len(user_info['爱好']) != 0:
        print('用户名：' + username)
        print('名字是:' + full_name)
        print('他还有个爱好是:' + hobby)


