rivers = {
    '尼罗河':'埃及',
    '长江':'中国',
    '密西西比河':'美国'
}
for river,country in sorted(rivers.items()):
    print('\n',river,'流经',country,end='。\n',sep='')
