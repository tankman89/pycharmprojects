million=[value for value in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))
odd = []
for value in range(1,100,2):
    odd.append(value)
    if len(odd)==20:
        break
print(odd)
x=[]
y=[]
for value in range(3,30,):
    if value % 3 == 0:
        x.append(value)
    else:y.append(value)
print(x)
print(y)
x=[]
x=[value**3 for value in range(1,11)]
print(*x)
print(len(x))