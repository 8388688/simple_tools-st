import random
from simple_tools import NULL

__all__ = ['create_random_list', 'random_choice', 'random_pop']


def create_random_list(start_=0, end_=10, step_=1, values=NULL, returns=True):
    """生成随机数列

    生成一个随机数列，或把现有的数列打乱

    :param start_: 起始值
    :param end_: 结束值(终止值)
    :param step_: 步长
    :param values: 默认为 NULL，如果你想要打乱现有的数列，就修改成一个可迭代序列，
     注：当这个参数不为 NULL 时则直接忽略 start_, end_, step_ 三个参数
    :param returns: 当此参数为 True 时返回乱序的数列，否则打印这个数列
    :return: 当 returns 为 True 时返回乱序的数列，否则返回 0
    """
    list1 = lists = []  # 列表元素初始化
    if values is NULL:
        for a000 in range(start_, end_, step_):
            # for 生成有序的数列
            lists.append(a000)  # 在数列的末尾增添元素
    # 把lists里的元素随机分布到 list1 里
    else:
        lists = values
    for a000 in range(len(lists)):
        # 生成随机数列
        random1 = random.randrange(0, len(lists), 1)  # 随机生成一个lists的下标
        list1.append(lists.pop(random1))
    if returns:
        return list1  # 返回 list1，以列表的格式
    else:
        print(list1)
        return 0


def random_choice():
    return random.choice([True, False])


def random_pop(*args, filters=None):
    base_value = list(args)
    for a000 in range(0, len(base_value), 1):
        yield base_value.pop(random.randint(0, len(base_value) - 1))
