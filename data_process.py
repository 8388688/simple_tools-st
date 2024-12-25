from simple_tools.data_base import tabs_bl
from simple_tools.default import deprecated

__all__ = ['binary_search', 'bl_properties_gen', 'generate_bl_properties',
           'dimensional_list', 'filter_', 'list2str',
           'search_to_str_in_list', 'review', "equals_list",
           "to_bytes_auto", "list2bytes", "bytes2list",

           "bl_properties", ]


def binary_search(list2, item):
    low = 0
    high = len(list2) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list2[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return mid
    return None


def bl_properties(*args, **kwargs):
    print(args)
    print(kwargs)
    deprecated(bl_properties, bl_properties_gen)


def bl_properties_gen(seq, title: None | str = "\033[0;31m目前暂时无法遍历 dict 和 set 类型\033[0m", digital=False,
                      __prefix_list=()):
    prefix = list(__prefix_list)

    SEQUENCES_LINE = (list, tuple)
    SEQUENCES_LIST = SEQUENCES_LINE + (dict, set)

    if title is not None:
        print(title)

    # if type(seq) in SEQUENCES_LIST:
    if type(seq) in SEQUENCES_LINE:
        for i in range(len(seq)):
            if i + 1 == len(seq):
                prefix_passed = tabs_bl[0]
            else:
                prefix_passed = tabs_bl[1]

            # print(i)
            yld = list2str(prefix + [prefix_passed[0], ] + [str(i) + ". " if digital else ""], "")
            if type(seq[i]) in SEQUENCES_LINE:
                yield yld + str(type(seq[i]))
                # print(yld, type(seq[i]), sep="")
                prefix.append(prefix_passed[1])
                for item in bl_properties_gen(seq[i], title=None, digital=digital, __prefix_list=prefix):
                    yield item
                prefix.pop(-1)
            else:
                yield yld + str(seq[i])
                # print(yld, seq[i], sep="")
    else:
        print(seq)


def list2str(lst, sep: str = '') -> str:
    str_l = ""
    if lst:
        for i in lst[:-1]:
            str_l += str(i) + sep
        str_l += str(lst[-1])
    else:
        pass
        # print("传入参数不能为空！")
    return str_l


def dimensional_list(value_list):
    output_list = []
    for a001 in value_list:
        if type(a001) in [list, tuple, set]:
            for a002 in dimensional_list(a001):
                output_list.append(a002)
        else:
            output_list.append(a001)

    return output_list


def filter_(v_str, pattern=('int',), contrary=False, returns=False, auto_convert=True):
    """字符过滤

    \n 字符过滤，兼容int, oct, dec, bin, hex, float, str, 单个字符, 大写字母, 小写字母, 控制字符等
    \n 字符过滤优先级：
    \n con = control = 1
    \n int = 2
    \n -- 0x = 0o = 0b = 2.1
    \n -- int = 2.2
    \n float = 3
    \n str = 4
    \n -- str_upper = 4.1
    \n -- str_lower = 4.2
    \n -- str_chinese = 4.3
    \n -- str = 4.4
    \n other_signs = 5
    \n -- non_chinese = 5.1
    \n -- non_english = 5.2
    \n other = 5
    \n other = 5
    \n other = 5
    \n other = 5

    \n 也就是说，如果一个 filter_ 同时过滤以下三个进程

    \n  1) filter_('1a213\b1dr4t', ('str_lower', ))
    \n  2) filter_('1a213\b1dr4t', ('1', ))
    \n  3) filter_('1a213\b1dr4t', ('unsigned', 'int'))
    \n 那么将会按照 3 - 1 - 2 的顺序执行。
    \n 附：保留字列表：
    \n [int, float, str, str_upper, str_lower, str_chinese, control, con]
    \n [unsigned, no_break, f_dec(强制转换十进制), 'non_chinese', 'non_english']
    \n 有待改进的地方：过滤时忽略 空格、tab和回车

    :param v_str: 必填，过滤的源文件
    :param pattern: 过滤参数
    :param contrary: 反向过滤
    :param returns: 当 returns 为 True 时以元组的形式返回 cache_dict 和 trash，否则只返回 cache_dict
    :param auto_convert: 过滤完成后自动转换成目标类型, 默认为 True
    :return: 当 returns 为 True 时以元组的形式返回 cache_dict 和 trash，否则只返回 cache_dict

    """
    base_string = v_str
    cache_dict = trash = ''
    class_ = pattern
    if 'control' in class_ or 'con' in class_:
        if type(base_string) is int or type(base_string) is float:
            if not contrary:
                cache_dict = ''
            else:
                cache_dict = base_string
        for a000 in base_string:
            if 32 > ord(a000):
                if contrary:
                    trash += a000
                else:
                    cache_dict += a000
            else:
                if contrary:
                    cache_dict += a000
                else:
                    trash += a000
        if cache_dict == '':
            cache_dict = ''
        else:
            if not contrary:
                if auto_convert:
                    cache_dict = str(cache_dict)
            else:
                cache_dict = str(cache_dict)
    elif 'int' in class_:
        if type(base_string) is int or type(base_string) is float:
            if not contrary:
                cache_dict = int(base_string)
            else:
                cache_dict = 0
        else:
            signs = ('0B', '0O', '0X', '0b', '0o', '0x')
            if base_string[0:2] in signs or 'f_dec' not in class_:
                base_string = str.upper(base_string)
                cache_dict += base_string[0:2]
                if signs.index(base_string[0:2]) == 0 or signs.index(base_string[0:2]) == 3:
                    wall = ('0', '1',)
                elif signs.index(base_string[0:2]) == 1 or signs.index(base_string[0:2]) == 4:
                    wall = ('0', '1', '2', '3', '4', '5', '6', '7',)
                elif signs.index(base_string[0:2]) == 2 or signs.index(base_string[0:2]) == 5:
                    wall = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            'A', 'B', 'C', 'D', 'E', 'F')
                else:
                    wall = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
                for a000 in base_string[2:-1]:
                    if a000 in wall:
                        if contrary:
                            trash += a000
                        else:
                            cache_dict += a000
                    else:
                        if contrary:
                            cache_dict += a000
                        else:
                            trash += a000
                if not contrary:
                    if cache_dict in signs:  # 没有什么可转换的
                        cache_dict = 0
                    else:
                        if auto_convert:
                            cache_dict = int(eval(cache_dict))
                else:
                    cache_dict = str(cache_dict)
            else:
                for a000 in base_string:
                    if 57 >= ord(a000) >= 48 or (a000 == '-' and cache_dict == '' and 'unsigned' not in class_):
                        if contrary:
                            trash += a000
                        else:
                            cache_dict += a000
                    else:
                        if contrary:
                            cache_dict += a000
                        else:
                            trash += a000
                if cache_dict == '':
                    cache_dict = 0
                else:
                    if not contrary:
                        if auto_convert:
                            cache_dict = int(cache_dict)
                    else:
                        cache_dict = str(cache_dict)
    elif 'float' in class_:
        if type(base_string) is int or type(base_string) is float:
            if not contrary:
                cache_dict = float(base_string)
            else:
                cache_dict = 0.0
        else:
            for a000 in base_string:
                if 57 >= ord(a000) >= 48 or '.' not in cache_dict and a000 == '.' or (a000 == '-' and cache_dict == ''):
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
            if cache_dict == '':
                cache_dict = 0.0
            else:
                if not contrary:
                    if auto_convert:
                        cache_dict = float(cache_dict)
                else:
                    cache_dict = str(cache_dict)
    elif 'str' in class_ or 'str_upper' in class_ or 'str_lower' in class_:
        if 'str_upper' in class_:
            for a000 in base_string:
                if 90 >= ord(a000) >= 65:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        elif 'str_lower' in class_:
            for a000 in base_string:
                if 121 >= ord(a000) >= 96:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        elif 'str_chinese' in class_:
            for a000 in base_string:
                if 40870 >= ord(a000) >= 13311:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        else:  # elif class_ == 'str':
            for a000 in base_string:
                if 121 >= ord(a000) >= 96 or 90 >= ord(a000) >= 65:
                    if contrary:
                        trash += a000
                    else:
                        cache_dict += a000
                else:
                    if contrary:
                        cache_dict += a000
                    else:
                        trash += a000
        if auto_convert:
            cache_dict = str(cache_dict)
    elif 'other_signs' in class_:
        if 'non_chinese' in class_:
            # 只过滤英文字符
            wall = ('\"', '\'', '`', '(', ')', '<', '>', '(', ')', '[',
                    ']', '{', '}', ',', '.', '?', '!', ':', ';', '~',
                    '&', '@', '#', '/', '|', '\\', '_', '^',)
        elif 'non_english' in class_:
            # 只过滤中文字符
            wall = ('·', '¨', '´', '«', '»', '¯', '¦', '¡', '¿', '‘',
                    '’', '〝', '〞', '＂', '＇', '【', '】', '《', '》', '＜',
                    '＞', '﹝', '﹞', '〔', '〕', '〈', '〉', '［', '］', '「',
                    '」', '｛', '｝', '〖', '〗', '『', '』', '、', '～', '＆',
                    '＠', '＃', '，', '。', '？', '！', '：', '；', '…', '　',
                    '︵', '︶', '︷', '︸', '︹', '︺', '︿', '﹀', '︽', '︾',
                    '﹁', '﹂', '﹃', '﹄', '︻', '︼', '／', '｜', '＼', '＿',
                    '￣', '﹏', '﹋', '﹍', '﹉', '﹎', '﹊', 'ˋ', '︴', 'ˇ',
                    '¨', 'ˊ', '‹', '›', '︗', '︘',)
            for i in wall:
                print(i + '\', \'' if 127 < ord(i) else '', end='')
        else:
            # 不分全/半角(不分中英，全部过滤)
            wall = ('\"', '‘', '’', '〝', '〞', '\'', '＂', '＇', '`', '(',
                    ')', '【', '】', '《', '》', '＜', '＞', '﹝', '﹞', '<',
                    '>', '(', ')', '[', ']', '〔', '〕', '〈', '〉', '{',
                    '}', '［', '］', '「', '」', '｛', '｝', '〖', '〗', '『',
                    '』', ',', '.', '?', '!', ':', ';', '、', '～', '＆',
                    '＠', '＃', '，', '。', '？', '！', '：', '；', '·', '…',
                    '~', '&', '@', '#', '︵', '︶', '︷', '︸', '︹', '︺',
                    '︿', '﹀', '︽', '︾', '﹁', '﹂', '﹃', '﹄', '︻', '︼',
                    '/', '／', '|', '｜', '\\', '＼', '_', '＿', '￣', '﹏',
                    '﹋', '﹍', '﹉', '﹎', '﹊', 'ˋ', '︴', '^', 'ˇ', '¨',
                    'ˊ', '　', '‹', '›', '︗', '︘', '¨', '´', '«', '¿',
                    '»', '¯', '¦', '¡',)
            for i in wall:
                print(i + '\', \'' if 127 < ord(i) else '', end='')
        for a000 in base_string:
            if a000 in wall:
                if contrary:
                    trash += a000
                else:
                    cache_dict += a000
            else:
                if contrary:
                    cache_dict += a000
                else:
                    trash += a000
        if auto_convert:
            cache_dict = str(cache_dict)
    else:
        a000 = []
        cache_dict = base_string
        for item in range(len(class_)):
            length_ = len(class_[item])
            list2 = []
            obj_cache_list = []
            for a001 in cache_dict:
                list2.append(a001)
                # 把a转换成list的格式存入list2
            for a000 in range(len(list2)):  # a000 是 range（）
                if list2[a000: a000 + length_] == list(class_[item]):
                    obj_cache_list.append([a000, a000 + length_])
            obj_cache_list.reverse()
            cache_dict = ''
            for a002 in obj_cache_list:
                del [list2[a002[0]: a002[1]]]
            for a000 in list2:
                cache_dict += a000
    if returns:
        return cache_dict, trash
    else:
        return cache_dict


def search_to_str_in_list(input_object=None, testlist=None, **kwargs):
    list_tips = kwargs.get('list_tips', '输入一个列表：')
    obj_tips = kwargs.get('obj_tips', '输入一个str')
    recursion = kwargs.get('recursion', False)
    insensitive_data = kwargs.get('insensitive_data', False)
    output_list = []
    cache_output_list = []
    if testlist is None:
        testlist = eval(input(list_tips))
    elif recursion:
        testlist = dimensional_list(testlist)
    else:
        pass

    if input_object is None:
        obj2 = input(obj_tips)
    else:
        obj2 = input_object
    # testlist 可以是(), {} 等
    # 因为 OPL(output_list)只是读取 testlist 的内容
    # 并且在读取完后要对 OPL 进行 resort
    for a000 in testlist:
        if type(a000) in [list, set, dict]:
            for _ in search_to_str_in_list(obj2, a000,
                                           recursion=recursion, list_tips=list_tips,
                                           obj_tips=obj_tips, insensitive_data=insensitive_data):
                cache_output_list.append(_)
        else:
            if ((obj2 in a000) if not insensitive_data else (str(obj2) in str(a000))) or (
                    obj2 == a000 if not insensitive_data else (str(obj2) == str(a000))):
                cache_output_list.append(a000 if not insensitive_data else str(a000))
    for a000 in cache_output_list:
        if type(a000) in [str, ]:
            if a000 == obj2:
                output_list.append([-1, a000])
            else:
                for a001 in range(0, len(a000), 1):
                    if a000[a001: a001 + len(obj2)] == obj2:
                        output_list.append([a001, a000])
                        break
        else:
            output_list.append([-1, a000])
    del cache_output_list[::]
    # ->
    cache_output_list = sorted(output_list,
                               key=lambda x: x[0])
    # cache_output_list 此时应该是 list 的形式，如果是 str 的话，就在 "->" 记号处插入一个 eval()
    del output_list[::]
    for a000 in range(len(cache_output_list)):
        output_list.append(cache_output_list[a000][1])
    # print('搜索结果：', output_list)
    del cache_output_list
    return output_list


def review(value, *args, **kwargs):
    deprecated(review, bl_properties_gen)
    print(args)
    print(kwargs)
    for i in bl_properties_gen(value):
        print(i)


def equals_list(*args: list | set | tuple):
    k_equ = True
    if not args:
        k_equ = False
    else:
        std_ch = args[0]
        for i in args:
            i_ch = list(i)
            for j in std_ch:
                if j in i_ch:
                    i_ch.pop(i_ch.index(j))
                else:
                    k_equ = False
            if i_ch:
                k_equ = False
    return k_equ


def to_bytes_auto(code: int):
    RATE = 256  # 不可随意修改，因为 \xff 最多表示 0 - 255 这 256 个数码
    i = 0
    while code // (RATE ** i) != 0:
        i += 1
    return code.to_bytes(i)


def list2bytes(seq: list):
    bytes_ret = b""
    for i in seq:
        bytes_ret += to_bytes_auto(i)

    return bytes_ret


def bytes2list(context: bytes, coding="utf-8", chunks=1):
    """虽然名为 bytes2list 但也兼具 str2list 的功能

    @param context:
    @param coding:
    @param chunks:
    @return:
    """
    text_list = []
    for ch in range(0, len(context), chunks):
        i = context[ch: ch + chunks]
        if type(i) is str:
            print("\033[0;30m尽量避免使用 str 类型，推荐 bytes 类型\033[0m;")
            text_list.append(int.from_bytes(bytes=i.encode(coding)))
        elif type(i) is int:
            text_list.append(i)
        elif type(i) is bytes:
            text_list.append(int.from_bytes(bytes=i))
            # print("skip:", i)
    # print("转列表:", text_list)
    return text_list


generate_bl_properties = bl_properties_gen
