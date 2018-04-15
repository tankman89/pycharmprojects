

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计, 直到没有打印的设计为止
    打印每个设计后, 都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)
        # 模拟根据设计制作3D打印模型的过程
        print('\n打印模型：' + current_design, end='')


def show_completed_models(completed_models):
    """显示已经打印好的所有模型"""
    for completed_model in completed_models:
        print('\n' + completed_model)


unprinted_designs = ['苹果手机', '机器人', '十二面体']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




