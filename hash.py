from time import time
from hashlib import md5, sha1, sha224, sha256, sha384, sha512, \
    blake2b, blake2s, \
    sha3_224, sha3_256, sha3_384, sha3_512
from uuid import uuid1, uuid3, uuid4, uuid5, NAMESPACE_DNS

from simple_tools.data_base import EMPTY_UUID
from simple_tools.maths import dec_to_r_convert

__all__ = ['get_md5', 'get_hash_values', 'uuid_generator']


def get_md5(string, encoding='utf-8', ratios=16):
    return get_hash_values(string, encoding, 0, ratios)


def get_hash_values(string, encoding='utf-8', pattern=0, ratios=16):  # 此处0不能换成 null，因为它是一个索引而非空值。
    base = (md5,
            sha1, sha224, sha256, sha384, sha512,
            blake2b, blake2s,
            sha3_224, sha3_256, sha3_384, sha3_512,)
    choice = base[pattern % len(base)]
    data_bytes = choice(string.encode(encoding=encoding)).digest()
    return dec_to_r_convert(int.from_bytes(data_bytes, byteorder='big'), ratios)


def uuid_gen(mode='time_mac', string=None, numeric=False):
    mode_c = str(mode)
    if string is None:
        string = get_md5(str(time()))
    if mode_c == 'time_mac' or mode_c == '1':
        ret = uuid1()
    elif mode_c == 'md5' or mode_c == '3':
        ret = uuid3(NAMESPACE_DNS, string)
    elif mode_c == 'random' or mode_c == '4':
        ret = uuid4()
    elif mode_c == 'sha-1' or mode_c == '5':
        ret = uuid5(NAMESPACE_DNS, string)
    else:
        print('无效的模式 - %s' % mode_c)
        ret = EMPTY_UUID

    if numeric:
        ret = str(ret.hex)
    else:
        ret = str(ret)

    return ret


uuid_generator = uuid_gen
