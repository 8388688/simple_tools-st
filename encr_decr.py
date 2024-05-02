from random import randint
from sys import byteorder, getfilesystemencoding

from simple_tools.data_process import filter_
from simple_tools.hash import get_md5

__all__ = [
    'absolute_encryption', 'digital_decryption', 'file_encryption',
    'md5_encryption', 'normal_encryption', 'normal_encryption_with_bytes',
]


def absolute_encryption(value1, print_=False, steps=',', pattern=None, signed=True):
    """绝对加密

    :param value1: 加密的字符串
    :param print_: 是否打印
    :param steps: 分隔符
    :param pattern: 强制使用 pattern 进制转换，如果未指定，则为随机
    :param signed: 是否添加 "0b", "0x" 等前缀，默认为 True
    :return: 加密后的 str
    """
    record = ''
    cache_count = 0
    for a000_1 in value1:
        cache_count += 1
        cache_encryption = ord(a000_1)
        if pattern == 8:
            cache_encryption = oct(cache_encryption)
        elif pattern == 2:
            cache_encryption = bin(cache_encryption)
        elif pattern == 10:
            pass  # 此代码不可删除
        elif pattern == 16:
            cache_encryption = hex(cache_encryption)
        elif pattern is None:
            a = randint(0, 3)
            if a == 0:
                cache_encryption = bin(cache_encryption)
            elif a == 1:
                cache_encryption = oct(cache_encryption)
            elif a == 2:
                pass  # 此代码不可删除
            elif a == 3:
                cache_encryption = hex(cache_encryption)
        else:
            print('%s - 输入值非法' % pattern)
        if print_:
            print(cache_encryption, end=steps)
        if cache_count != 1:
            record += steps + str(cache_encryption)
        else:
            record += str(cache_encryption)
    del cache_count, cache_encryption
    return record


def digital_decryption(value1, print_=False, steps='\\'):  # 数字解密
    a = str(value1).split(steps)
    decrypt = ''
    d_list = ('0b', '0B', '0o', '0O', '0x', '0X')
    for i in a:
        if i[0: 2] in d_list:
            decrypt += chr(eval(i))
        else:
            decrypt += chr(int(i[0: len(i)]))
            if print_:
                print(decrypt)
    # cache_str = 0
    # for a000 in range(len(value1)):
    #     a001 = a000
    #     if value1[a000] == '\\':
    #         a001 += 1
    #         while value1[a001] == '\\':
    #             cache_str += a000
    #     jieMi = chr(int(bin(float(cache_str))))
    #     if print_:
    #         print(jieMi, end='')
    return decrypt


def file_encryption(string, mode):
    """from [zifan.site](https://zifan.site/)

    @param string:
    @param mode:
    @return:
    """
    old_str = string
    old_list = []
    new_str = ''
    KEY = ''

    for i in range(50):
        KEY += str(randint(0, 9))  # 因为这里使用的KEY是随机生成的，所以每次启动产生的KEY都不一样
        # 这样只能在运行程序时加密再解密才能成功，否则，如果你启动一次程序加密后再启动一次程序进行解密是无效的
        # 因为用来解密的的key已经不是原来加密用的key了，所以这里可以暂时用一个固定的KEY代替
    KEY = '62848193761722270825649193715922465178611568554478'  # 这样加密后关闭程序再启动也能进行解密,当然使用随机的也可以

    print(old_str)

    for i in old_str:
        if ord(i) > 255:
            j = absolute_encryption(i)
            for k in j:
                old_list.append(ord(k))
        else:
            old_list.append(ord(i))

    now = 0
    # 以字节为单位读写文件，不用考虑读取到非打印字符问题，无差别的二进制，无论是文本文件还是二进制文件都可以加解密
    for a000 in old_list:  # 这里的i不再是字符，而是读取到的一个字节的整数值
        # 由于一个字节的整数范围只在0到255这256个整数，假如读到原文件的一个字节值为253，key为9，253+9就超出了一个字节表示的范围
        # 所以可以将加密后超过255的字节值环形回到开始的数值，比如253+9=262=256+7，可以将加密的值存为6
        # 在解密时，这个加密后得到的数值7还要区别于比如原来2+5得到的7
        # 只需要对加密函数对256取余数就能解决上面的两个问题
        # 比如(7-9) % 256 == 254,(7-5) % 256 == 2,无论加密数值是否超过255都可以正确地加解密
        if mode:  # 加密
            # 此处对加密函数取余，按字节存储
            # new_str += str(((a000 + int(KEY[now])) % 256).to_bytes(1, byteorder='big'))
            new_str += chr(ord(((a000 + int(KEY[now])) % 256).to_bytes(1, byteorder='big')))

        else:  # 解密
            # 此处对加密函数取余，按字节存储
            new_str += chr(ord(((a000 - int(KEY[now])) % 256).to_bytes(1, byteorder='big')))

        now += 1
        if now == len(KEY):
            now = 0  # KEY序列结束后再从头开始，环形回到开始处

    if not mode:
        new_str = digital_decryption(new_str)

    return new_str


def md5_encryption(string, encr_func=get_md5):
    """WARNING: function md5_encryption is still a Experimental Features.
    
    :param string: 
    :param encr_func: 
    :return: 
    """
    print('\033[1;31m' + md5_encryption.__doc__ + '\033[0m')
    v_str = list(string)
    a_str = []
    for a000 in range(0, len(v_str), 1):
        a_str.append(encr_func(v_str[a000]))

    return a_str


def normal_encryption(string, mode, key=None, key_length=16, details=False, coding=getfilesystemencoding(), **kwargs):
    """`normal_encryption` has been stopped supporting in 4.2-beta2+"""
    print('\033[1;31m' + normal_encryption.__doc__ + '\033[0m')
    string_transit = string.encode(coding)
    return normal_encryption_with_bytes(string_transit, mode, key, key_length, details, coding,
                                        quiet=kwargs.get('quiet', True)).decode(coding)


def normal_encryption_with_bytes(string: bytes, mode, key=None, key_length=16, details=False,
                                 coding=getfilesystemencoding(), **kwargs):
    """普通的加密

    :param string: 加密的字节串 (废话)。
    :param mode: 指定是加密还是解密：True 是加密，False 是解密。
    :param key: 指定加密所用的 KEY，不指定或指定为 None 就是自动生成密码，[注1]
    :param key_length: 密钥长度：只有在 key 形参被指定为 None 的时候才被执行，[注2]
    :param details: 详细返回 [注3]
    :param coding: 三个取值 [getfilesystemencoding(), 'utf-8', 'gbk',] 默认为 getfilesystemencoding
    :return: 详见 details

    kwargs: quiet: 默认为 True

    \n 注1: 注意：key 的长度不能小于4位。
    \n 注2: 当 len(key) 和 key_length 不一致时，以 len(key) 的长度为准。
    \n 注3: 此参数为 True 的时候以元组的形式返回(加密/解密)后的字符串和 key，否则只返回(加密/解密)后的字符串。

    """

    if key is None:
        KEY = ''
        lengthening = max(key_length, 4)
        # 生成 KEY
        for a001 in range(0, lengthening, 1):
            KEY += str(randint(0, 9))
    elif len(str(key)) <= 4:
        print('输入key长度不能小于4。已为你自动生成一个随机的 KEY.')
        KEY = ''
        lengthening = max(key_length, 4)
        # 生成 KEY
        for a002 in range(0, lengthening, 1):
            KEY += str(randint(0, 9))
    else:
        KEY = str(key)
        lengthening = len(KEY)

    v_str = string
    a_str = b''  # 输出目录
    code = coding
    quiet = kwargs.get('quiet', True)
    if mode:
        pattern = 1
    else:
        pattern = -1
    if code.lower() in ['utf-8', 'gbk', 'utf-16', 'utf-32', 'gb2312', 'gb18030']:
        if not quiet:
            print(f'准备加密/解密，校验：{string=},{mode=},{key=},{key_length=},{details=},{coding=},{kwargs=}')
        else:
            pass
    else:
        print('未知 - encode 键入了一个错误的值:', coding)
        raise ValueError
    '''
    # 原始加密代码核心 (str)
    for a001 in range(0, len(v_str), 1):
        a_str += chr(ord(v_str[a001]) + filter_(KEY[a001 % lengthening], ('unsigned', 'f_dec', 'int')) * pattern)
    '''
    # 以下为 bytes 模式加密的代码
    key_index = -1
    for a001 in v_str:
        key_index = (key_index + 1) % len(KEY)
        a_str += ((a001 + filter_(KEY[key_index % lengthening], ('unsigned', 'f_dec', 'int')) * pattern) % 256) \
            .to_bytes(1, byteorder='big', signed=False)
        # If you set `signed = True` you will set `length = 2` in `to_bytes()` together,
        # Otherwise return `OverflowError`

    if details:
        return a_str, KEY
    else:
        return a_str
