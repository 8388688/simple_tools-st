import math
import time
from os.path import join

from simple_tools.data_base import science_tuple, pass_
from simple_tools.data_process import filter_
from simple_tools.system_extend import safe_md
from simple_tools.data_base import ST_WORK_SPACE

__all__ = [
    'add1', 'average_generator', 'convert_system', 'is_prime',
    'dec_to_r_convert', 'decomposition', 'decomposition_gui',
    'divisionAlgorithm', 'euclidean_algorithm',
    'get_prime_range', 'generate_prime_range',
    'r_to_dec_convert', 'saving_decomposition',
    'r2dec_convert', 'dec2r_convert',
]

LOCAL_WORK_SPACE = join(ST_WORK_SPACE, 'maths')
safe_md(LOCAL_WORK_SPACE, quiet=True)


def average_generator(*args):
    count1 = 0
    l1 = []
    sum1 = 0
    for a000 in args:
        l1.append(filter_(a000, ('f_dec', 'int',)))
    for a000 in l1:
        count1 += 1
        c = sum1
        sum1 = (c * count1 - c + a000) / count1
        yield sum1
        del c


def convert_system(value1, cm1='', cm2='', cm3='', returns=False, error_tips_='你输入的数字太大了！', precision=None):
    """转换系统

    将一个数以 KM…… 的形式输出

    :param value1: 输入的大数
    :param cm1: 文本1
    :param cm2: 文本2
    :param cm3: 文本3
    :param returns: 默认为False，True时直接忽略cm1, cm2, cm3三个参数，True时返回转换后的值和原来的值，不打印结果，False时只返回转换后的值，打印结果。
    :param error_tips_: 错误提示
    :param precision: 输出精度，例：10表示精确到十位，0.01表示精确到百分位，默认为None，（None表示无损输出）
    :return: 转换后的数（以str的形式输出）
    """
    re_obj = obj = value1
    count = 0
    pre = 0
    if precision is not None:
        pre = 1 / precision
    while (obj >= 1000 or obj <= -1000) and obj != 0 and obj != 1:
        if 1000 > obj > -1000:
            break
        elif obj > 1e66 or obj < -1e66:
            print(error_tips_)
            break
        obj /= 1000
        count += 1
    if obj != 0:
        if obj // 1 == re_obj:
            if precision is not None:
                obj = obj * pre // 1 / pre
            if not returns:
                print(cm1, '=', obj, science_tuple[count], sep='')
        else:
            if precision is not None:
                obj = obj * pre // 1 / pre
            if not returns:
                print(cm3, '\n', cm1, obj, science_tuple[count], cm2, '\n', sep='')
    if returns:
        return str(obj) + science_tuple[count], re_obj
    else:
        return str(obj) + science_tuple[count]


def is_prime(n=None):
    key_ = True
    if n is None:
        n = filter_(input('>>>'), ('unsigned', 'f_dec', 'int'))
    else:
        n = filter_(n, ('unsigned', 'f_dec', 'int'))
    for a000 in range(2, math.ceil(math.sqrt(n + 1)), 1):
        if n % a000 == 0:
            key_ = False
            break
    return key_


def decomposition_gui(int1=None, tip1='输入一个整数', record=True):
    """分解质因数 - 已弃用

    :param int1: 当 int1 为 None 的时候，弹出 tip1 提示输入
    :param tip1: 输入提示，（当 int1 不为 None 的时候直接忽略此参数）
    :param record: 是否将此次分解记录，默认为 True
    :return: 以元组的格式返回分解后的质因数
    """

    if int1 is None:
        a = filter_(input(tip1), ('unsigned', 'f_dec', 'int'))
    else:
        if type(int1) is not int:
            a = filter_(int1, ('unsigned', 'f_dec', 'int'))
        else:
            a = int1

    print(f'\033[0;36m{decomposition_gui.__name__} 使用的是 {decomposition.__name__} 的 API。\033[0m')
    obj_list = decomposition(a)
    if record:
        file_name = join(ST_WORK_SPACE, 'primeNumber.s8l')
        open(file_name, 'a').close()
        file = open(file_name, 'r+')
        fr = file.read()
        for i in obj_list:
            if str(i) not in fr:
                file.write(str(i) + ', ')
        file.close()
    if int1 is None:
        print(obj_list)
    else:
        return obj_list


def decomposition(frequently, **kwargs):
    """分解质因数 - 纯净版

    kwargs: 如下
    \n max_safe_time: 安全锁 - 检测程序运行超过 %d 秒后自动 return 掉
    \n safe_tip: 安全锁启动的时候弹出的提示, 仅当 quiet 参数被设置为 False 的时候有效
    \n quiet: 安静模式: [需要验证]将此项设置为 False 可以加快计算速度

    :param frequently: 要分解的目标数值
    :param kwargs: 可选项
    :return:
    """
    frequently_var, start_time, i, decomposition_list = abs(frequently), time.time(), 1, []
    max_safe_time, quiet, safe_tip = kwargs.get('max_safe_time', None), kwargs.get('quiet', None), kwargs.get(
        'safe_tip', '\033[0;31m启动安全锁\033[0m')
    while i * i <= frequently_var:
        i += 1
        while frequently_var % i == 0:
            frequently_var //= i
            decomposition_list.append(i)
        if not quiet:
            print(
                f'正在计算第{len(decomposition_list) + 1}个质因数, 已完成'
                f'{round(i / math.sqrt(frequently_var) * 10000) / 100 if i / math.sqrt(frequently_var) <= 1 else 100}%')
        if max_safe_time is not None and time.time() - start_time > max_safe_time:
            print(safe_tip) if not quiet else pass_
            break
    else:
        used_time = time.time() - start_time
        print(f'用时{used_time}秒\n' if not quiet else '', end='')

    decomposition_list.append(frequently_var)
    while 1 in decomposition_list:
        decomposition_list.remove(1)

    return decomposition_list


def euclidean_algorithm(value1, value2, print_=True, p_print=False):
    a = value1
    b = value2
    # count = 0
    # while a != b:
    #     count += 1
    #     if a > b:
    #         a -= b
    #         a = float('%.10f' % a)
    #         b = float('%.10f' % b)
    #         if p_print:
    #             print(count, ')\t', a, '\t', b, sep='')
    #     elif b > a:
    #         b -= a
    #         a = float('%.10f' % a)
    #         b = float('%.10f' % b)
    #         if p_print:
    #             print(count, ')\t', a, '\t', b, sep='')
    #     if count % 100 == 0:
    #         input('请按Enter键继续......')
    # if print_:
    #     print(a)
    # return a

    while a != 0 and b != 0:
        if a > b:
            a %= b
            if p_print:
                print(a, b, sep='\t')
        elif b > a:
            b %= a
            if p_print:
                print(a, b, sep='\t')
        else:
            break
    if a == 0:
        if print_:
            print(b)
        return a
    else:
        if print_:
            print(a)
        return b


def add1(*args):
    """测试版

    :param args:
    :return:
    """
    print(f'WARNING: function {add1.__name__} is still a Experimental Features.')
    count = 0

    def add(a, b):
        a1 = filter_(a, 'float')
        b1 = filter_(b, 'float')
        print('a1=', a1, ' b1=', b1, sep='')
        l1 = l2 = None
        print(a1, b1)
        if int(a1) == a1 and int(b1) == b1:
            r = int(a1) + int(b1)
        else:
            if '.' in a1:
                l1 = a1.split('.')
            if '.' in b1:
                l2 = b1.split('.')
            r1 = int(l1[0]) + int(l2[0])
            if len(l1[1]) >= len(l2[1]):
                l2[1] += '0' * (len(l1) - len(l2))
            else:
                l1[1] += '0' * (len(l2) - len(l1))
            r2 = int(l1[1]) + int(l2[1])
            r = str(r1) + '.' + str(r2)
        print('r=', r)

        return r

    list1 = list(args)
    for a000 in range(0, len(list1), 1):
        list1[a000] = str(filter_(list1[a000], 'float'))
    for a000 in range(0, len(list1), 2):
        count += add(count, list1[a000])
    return count


def get_prime_range(start=2, end=100, step=1):  # 埃拉托斯特尼筛法 - 改进版
    DELETED_CODE = -2  # -2 表示将要被删除的
    prime_list = list(range(2, end, 1))
    # prime_list = list(range(start, end, step))
    lim_max = math.sqrt(end)
    start_n = -1
    while start_n <= lim_max:
        start_n += 1
        for i in range(len(prime_list)):
            if prime_list[i] != prime_list[start_n] and prime_list[i] % prime_list[start_n] == 0:
                prime_list[i] = DELETED_CODE
            else:
                pass

        while DELETED_CODE in prime_list:
            # 重复执行删除 prime_list 中第一个值为 -2 的元素, 直到 prime_list 中没有值为 -2 的元素
            prime_list.remove(DELETED_CODE)

    db = set(list(range(start, end, step)))
    final_prime_list = sorted(list(db & set(prime_list)))

    return final_prime_list


def generate_prime_range(start=2, end=100, step=1):
    """用生成器获取 start - end 区间的质数

    一个 bug: 当调用 `generate_prime_range(start=10, end=100, step=1)` 时会返回 10 - 100 区间所有不能被 10 整除的数.
    是由于 prime_list 会默认传入的第一个参数是质数, 导致后面的计算全部出错(解决方法: 禁止用户修改 start 参数[滑稽]).

    @param start: 起始值(包括)
    @param end: 结束值(不包括)
    @param step: 步长值
    @return: 计算出的质数列表
    """
    print(f'\033[1;31m{generate_prime_range.__name__} is probably including many bugs.\033[0m')
    prime_list = []
    for x in range(start, end, step):
        x_sqrt = math.sqrt(x)
        for prime in prime_list:
            if x % prime == 0:
                break
            if prime > x_sqrt:
                prime_list.append(x)
                yield x
                break
        else:
            prime_list.append(x)
            yield x


def r_to_dec_convert(values, r):  # R:无符号十进制整型数
    """进制转换

    :param values:
    :param r:
    :return:
    """
    value_r = filter_(r, ('unsigned', 'int'))
    output = count = 0
    for a000 in str(values):
        if 58 > ord(a000) >= 48:
            output += int(a000) * value_r ** (len(str(values)) - count)
        elif 65 <= ord(a000) < 91 or 97 <= ord(a000) < 123:
            output += (ord(a000.upper()) - 55) * value_r ** (len(str(values)) - count)
        else:
            print('Invalid values!')
            return -1
        count += 1

    return output / r


def dec_to_r_convert(val, r, **kwargs):
    """10 进制转 R 进制

    **kwargs 选项:
    - charset: 字符表，默认为 DEFAULT_DIGITAL_CHARSET_PREPARED 的值:
    这个数组决定 return 扔出的 str 每一位上的字符显示.
    - figure_type: 可选 ["auto" | "f_int" | "f_flt"]
        - "auto": 自动判断 val 是 int 还是 float;
        - "f_int": 强制将 val 以 int 类型处理;
        - "f_flt": 强制将 val 以 float 类型处理;

    例如，十进制的 28，转换成 16 进制后本应为 1C，但实际为 112.
    前一个 1 是十六进制的一个十六，后面的 12，是十六进制的 C 转换为十进制所得的数字.
    return 的时候，两个数位上的三个数字转化成 str 后被平铺返回，就失去了原本数位的占位位置.

    add: DEFAULT_DIGITAL_CHARSET_PREPARED 中提供的字符集最多只能支持到三十六进制，如果你使用六十进位制，可以参考下面我们的预设:

    ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '-', '/') # 64 进位制，很少用到

    注意: 这里的字符 A 代表的是十进制的数字 0.
    同样的，这里的数字 0 也不代表十进制的 0，而是十进制的 52.

    :param val: 一个十进制数
    :param r:
    :param kwargs:
    :return: 一个 r 进制数
    """
    # val = int(val)
    DEFAULT_DIGITAL_CHARSET_PREPARED = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    charset = kwargs.get('charset', DEFAULT_DIGITAL_CHARSET_PREPARED)

    if r < len(charset):
        charset = tuple(charset[0: r])
    else:
        print("参数 r 错误!")
        return -2

    val = filter_(val, ('unsigned', 'int'))
    output = str(charset[val % r])

    while val // r > 0:  # repeat until "val < r"
        val //= r
        output = str(charset[val % r]) + output
        # print(f'{val=},{r=},{output=}') # 早期的调试程序段

    return output


def r1_to_r2_convert(val, r1, r2):
    return dec_to_r_convert(r_to_dec_convert(val, r1), r2)


def dec2r_convert(fig, r, figure_type="auto"):
    """已弃用

    @param fig:
    @param r:
    @param figure_type:
    @return:
    """
    DIGITAL_CHARSET_PREPARED = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    if r < len(DIGITAL_CHARSET_PREPARED):
        digital_charset = tuple(DIGITAL_CHARSET_PREPARED[0: r])  # 设置准备的字符
    else:
        print("参数 r 错误!")
        return -1

    fig = filter_(fig, ("float",))
    fig_int = fig // 1
    fig_int_list = []
    fig_fra = fig % 1  # 此处也可替换为 `fig_fra = fig - fig_int`
    fig_fra_list = []
    fig_int_string = 0
    while fig_int // r != 0:  # repeat until(fig_int // r == 0)
        fig_int, cache_fil_item = divmod(fig_int, r)
        fig_int_list.append(cache_fil_item)
        fig_int_string += digital_charset[cache_fil_item]

    return fig_int_string


saving_decomposition = decomposition
divisionAlgorithm = euclidean_algorithm
r2dec_convert = r_to_dec_convert
# dec2r_convert = dec_to_r_convert

# get_prime_range = lambda start, end, step: list(generate_prime_range(start=start, end=end, step=step))
