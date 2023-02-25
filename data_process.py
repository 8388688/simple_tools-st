from simple_tools.data_base import NULL

__all__ = ['binary_search', 'bl_properties', 'generate_bl_properties',
           'dimensional_list', 'filter_', 'search_to_str_in_list',
           'bl', 'review', 'review']


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


def bl_properties(seqs, line_num=False, truly_number=False, __deep=0, __lines='', __numbers=(), **kwargs):
    """bl 装饰

    kwargs: title = None, 对于大列表套小列表的情况时的自定义表头

    提出时间：202204051955xx
    创建时间：20220406080946
    最后修改时间：20230126113413
    最后运行时间：20230126113422

    :param seqs: 要遍历的元素
    :param line_num: 是否加行号，默认为 False
    :param truly_number: 使用常规编号，而不是索引编号
    :param __deep: 遍历深度
    :param __lines:
    :param __numbers:
    :return:
    """

    def convert_list_to_str(lists, step=' '):
        """

        前置一个列表转换 str 的函数
        """
        if type(lists) in {list, set, tuple}:
            seq_armor = ''
            for a001 in lists:
                seq_armor += str(a001) + step
            return seq_armor
        else:
            print('输入类型不正确')
            return lists

    fill_name = '<List>'
    values = list(seqs) if type(seqs) == set else seqs
    sequence_class_list = {set, list, tuple, dict}
    special_list = {dict, }
    signs = __lines

    title = kwargs.get('title', NULL)

    for x in range(len(values)):
        if type(values) in special_list:
            bl_properties(seqs=tuple(zip(values.keys(), values.values())), line_num=line_num,
                          truly_number=truly_number, __deep=__deep, __lines=__lines, __numbers=__numbers,
                          title='dict')
            return type(values)
        elif type(values[x]) in sequence_class_list:  # 大列表套小列表（大数组套小数组）
            if line_num:
                cb = convert_list_to_str(__numbers, '>') + str(x + 1 if truly_number else x) + ':'
            else:
                cb = ''
            print(signs + ('└-' if x == len(values) - 1 else '├-') + cb + type(values[x]).__name__)
            if x == len(values) - 1:
                cb = '  '
            else:
                cb = '│ '
            if truly_number:
                cb2 = x + 1
            else:
                cb2 = x
            bl_properties(seqs=values[x], line_num=line_num, truly_number=truly_number, __deep=__deep + 1,
                          __lines=signs + cb, __numbers=tuple(list(__numbers) + [cb2, ]), title=title)
        else:
            if x == len(values) - 1:
                cb = '└-'
            else:
                cb = '├-'
            if line_num:
                cb2 = convert_list_to_str(__numbers, '>') + str(x + 1 if truly_number else x) + ':'
            else:
                cb2 = ''
            print(signs + cb, cb2, values[x], sep='')


def generate_bl_properties(seqs, line_num=False, truly_number=False, __deep=0, __lines='', __numbers=()):
    """bl 装饰

    提出时间：20220423174418
    创建时间：20220423175444
    最后修改时间：20220423200512
    最后运行时间：20220423200623

    :param seqs: 要遍历的元素
    :param line_num: 是否加行号，默认为 False
    :param truly_number: 使用常规编号，而不是索引编号
    :param __deep: 遍历深度
    :param __lines: 行标
    :param __numbers: 索引编号
    :return:
    """

    def convert_list_to_str(lists, step=' '):
        """

        前置一个列表转换 str 的函数
        """
        if type(lists) in {list, set, tuple}:
            seq_armor = ''
            for a001 in lists:
                seq_armor += str(a001) + step
            return seq_armor
        else:
            print('输入类型不正确')
            return lists

    fill_name = '<List>'
    sequence_class_list = {list, tuple, set, dict}
    values = list(seqs) if type(seqs) == set else seqs
    signs = __lines
    if type(values) == dict:
        for x in values:
            if type(values[x]) in sequence_class_list:
                if line_num:
                    cb = convert_list_to_str(__numbers, '>') + str(x + 1 if truly_number else x) + ':'
                else:
                    cb = ''
                yield signs + ('└-' if x == list(values.keys())[-1] else '├-') + cb + str(x)
                if x == list(values.keys())[-1]:
                    cb = '  '
                else:
                    cb = '│ '
                if truly_number:
                    cb2 = x + 1
                else:
                    cb2 = x
                for t in generate_bl_properties(seqs=values[x], line_num=line_num, truly_number=truly_number,
                                                __deep=__deep + 1, __lines=signs + cb,
                                                __numbers=tuple(list(__numbers) + [cb2, ])):
                    yield t
            else:
                if x == len(values) - 1:
                    cb = '└-'
                else:
                    cb = '├-'
                if line_num:
                    cb2 = convert_list_to_str(__numbers, '>') + str(x + 1 if truly_number else x) + ':'
                else:
                    cb2 = ''
                yield signs + cb + cb2 + (str(x) + ':' + str(values[x])
                                          if type(values) == dict else str(values[x]))
    else:
        for x in range(len(values)):
            if type(values[x]) in sequence_class_list:
                if line_num:
                    cb = convert_list_to_str(__numbers, '>') + str(x + 1 if truly_number else x) + ':'
                else:
                    cb = ''
                yield signs + ('└-' if x == len(values) - 1 else '├-') + cb + type(values[x]).__name__
                if x == len(values) - 1:
                    cb = '  '
                else:
                    cb = '│ '
                if truly_number:
                    cb2 = x + 1
                else:
                    cb2 = x
                for t in generate_bl_properties(seqs=values[x], line_num=line_num, truly_number=truly_number,
                                                __deep=__deep + 1, __lines=signs + cb,
                                                __numbers=tuple(list(__numbers) + [cb2, ])):
                    yield t
            else:
                if x == len(values) - 1:
                    cb = '└-'
                else:
                    cb = '├-'
                if line_num:
                    cb2 = convert_list_to_str(__numbers, '>') + str(x + 1 if truly_number else x) + ':'
                else:
                    cb2 = ''
                yield signs + cb + cb2 + (str(values[x]) + ':' + str(values[x].values())
                                          if type(values) == dict else str(values[x]))


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
        if type(base_string) == int or type(base_string) == float:
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
        if type(base_string) == int or type(base_string) == float:
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
        if type(base_string) == int or type(base_string) == float:
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


def search_to_str_in_list(input_object=NULL, testlist=NULL, **kwargs):
    list_tips = kwargs.get('list_tips', '输入一个列表：')
    obj_tips = kwargs.get('obj_tips', '输入一个str')
    recursion = kwargs.get('recursion', False)
    insensitive_data = kwargs.get('insensitive_data', False)
    output_list = []
    cache_output_list = []
    if testlist is NULL:
        testlist = eval(input(list_tips))
    elif recursion:
        testlist = dimensional_list(testlist)
    else:
        pass

    if input_object is NULL:
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


def bl(value, sep=':', line_sign=0, lines=False, all_values=False):
    """WARNING: `bl` has stopped supporting in simple_tools 4.3-alpha2+"""
    print('\033[0;31m' + bl.__doc__ + '\033[0m')
    review(value, sep, line_sign, lines, all_values)
    return -1


def review(value, sep=':', line_sign=0, lines=False, all_values=True, deep=0, decorate=True, dict_sign=':'):
    """review是检视的意思，它的作用等价于bl

    line_sign 和 decorate 互相冲突，line_sign 的优先级高于 decorate
    检视优先级中，dictionary 的优先级为 1，list，tuple，set，str 的优先级为 2，其他类型的优先级为 3

    :param line_sign: 加行号标志
    :param value: 判断输入的是什么类型
    :param sep: 第n项和第n+1项之间的分隔符
    :param lines: 空行，默认为 False
    :param all_values: 全部遍历
    :param deep: 递归深度，不要更改这个参数
    :param decorate: 装饰
    :param dict_sign: 字典分隔符
    :return: void
    """

    count = cache_count = 0
    deeps = deep
    if type(value) == dict:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                review(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=all_values, deep=deep + 1,
                       decorate=decorate)
            elif line_sign:
                count += 1
                print(str(count) + sep + str(a000) + dict_sign + str(value[a000]))
            elif decorate:
                if a000 == value[-1]:
                    print('├ ' * (deeps - 1) + '└ ', str(a000) + dict_sign + str(value[a000]), sep='')
                else:
                    print('├ ' * deeps, str(a000) + dict_sign + str(value[a000]), sep='')
            else:
                print(str(a000) + dict_sign + str(value[a000]))
    elif type(value) == str or type(value) == list or type(value) == tuple or type(value) == set:
        if lines:
            print()
        for a000 in value:
            if type(a000) == list or type(a000) == tuple or type(a000) == set or type(a000) == dict:
                review(a000, sep=sep, line_sign=line_sign, lines=lines, all_values=all_values, deep=deep + 1,
                       decorate=decorate)
            elif line_sign:
                count += 1
                print(count, sep, str(a000), sep='')
            elif decorate:
                if a000 == value[-1]:
                    print('├ ' * (deeps - 1) + '└ ', a000, sep='')
                else:
                    print('├ ' * deeps, a000, sep='')
            else:
                print(a000)
    else:
        print('输入类型不正确')
        return 1
    del cache_count
