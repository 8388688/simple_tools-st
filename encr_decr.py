from simple_tools.default import deprecated
from simple_tools.hash import get_md5
from simple_tools.data_process import list2bytes, bytes2list

__all__ = [
    'absolute_encryption', 'digital_decryption', 'file_encryption',
    'md5_encryption', 'normal_encryption', 'normal_encryption_with_bytes',
    "rsa_crypt", "rsa_crypt_easy",
]


def absolute_encryption(*args, **kwargs):
    print(args)
    print(kwargs)
    deprecated(absolute_encryption)


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


def file_encryption(*args, **kwargs):
    print(args)
    print(kwargs)
    deprecated(file_encryption)


def md5_encryption(string, encr_func=get_md5):
    """WARNING: function md5_encryption is still an Experimental Features.
    
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


def normal_encryption(*args, **kwargs):
    print(args)
    print(kwargs)
    deprecated(normal_encryption)


def normal_encryption_with_bytes(*args, **kwargs):
    print(args)
    print(kwargs)
    deprecated(normal_encryption_with_bytes)


def rsa_crypt(context: list | tuple, mode: int = 0, quiet=True):
    p, q = 8861, 9973
    n = p * q  # 88370753
    n_dd = (p - 1) * (q - 1)
    e = 29  # e 作为幂指数，应与 n_dd 互质
    # 以下为解方程 d * e == 1 (mod n - 1), 0 <= d < n - 1 的代码
    y = (e - 1), (n_dd % e)
    kk = 0
    while (y[0] - e * kk) % y[1] != 0:
        kk += 1
    y = (y[0] - e * kk) // y[1]
    d = (1 + y * n_dd) // e % n_dd
    del kk, y
    """
    条件：d * e == 1 (mod n_dd - 1), 0 <= d < n_dd - 1
    实际等价于解方程 29d == 88351920y + 1
    以 e = 29 为模，移项，得
    88351920y % 29 == -1
    y = -1/88351920 == (-1 + 29)/(88351920 % 29) == 28/27 == (28 - 29 * 5)/27 == -14
    d = (1 - 14 * 88351920)/29 == -42652651
    ∴ d = 88351920k - 42652651 == 88351920 + 45699269, y = 29k - 14 == 29k + 15
    """
    if not quiet:
        print(f"{d=}, {e=} 验证：{(d * e) % n_dd == 1}")
        print("原列表:", context)
    encr = context
    for c in range(abs(mode)):
        if mode == 0:
            pass
        if mode > 0:
            for i in range(len(encr)):
                ec_per = pow(encr[i], e, n)
                encr[i] = ec_per
            if not quiet:
                print(f"第{c}次加密后:", encr)
        if mode < 0:
            for i in range(len(encr)):
                ec_per = pow(encr[i], d, n)
                encr[i] = ec_per
            if not quiet:
                print(f"第{c}次解密后:", encr)

    return encr


def rsa_crypt_easy(byte: bytes, mode=0, coding="utf-8", quiet=True, chunks=1):
    ea = rsa_crypt(bytes2list(byte), 4)
    eb = list2bytes(rsa_crypt(ea, -4))
    print("相等？", byte == eb)
    return list2bytes(rsa_crypt(bytes2list(byte, coding=coding, chunks=chunks), mode=mode, quiet=quiet))
