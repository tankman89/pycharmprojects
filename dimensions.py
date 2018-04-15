dimensions = (200,50)
print('原来的尺寸:')
for dimension in  dimensions:
    print(dimension)
dimensions = (400,100)
print('现在的尺寸:',*dimensions,end='。')

