prompt = "给我说一句话!"
prompt += "\n输入'退出'来结束这个程序."
active = True
# message = ""
while active:
    message = input(prompt)
    if message == '退出':
        active = False
    elif message == '不玩了':
        active = False
    else:
        print(message)
        continue