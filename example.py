from simple_tools import *


def test():
    # from __init__.py
    if __name__ == '__main__':
        human1 = Person('steve')
        user1 = Users() if random_choice() else Users('电话')
        u1 = ''
        u2 = ' '
        while not u1:
            u1 = input('输入用户名(ran表示随机)')
            if u1 == 'ran':
                u1 = Users.returnName(user1)
                c = 0
                while u2 != 'y':
                    u2 = input('%s 这个用户名您满意吗？(y/n)' % u1)
                    if u2 == 'n':
                        u1 = Users.returnName(user1)
                        c += 1
                    else:
                        c += 5
                    if c >= 250:
                        print('\033[1;31m你是存心来捣乱的吧！\033[0m')
                        times.sleep(1)
                        exit(0)
                if u2 == 'y':
                    break
        user3 = Users(u1)
        print(user1, user3, human1, sep='\n')
        mmm = {'金币': 0, '银币': 5, '铜板': 15}
        aa = ['f', 'u', [['n', 'c'], 't', ['i', 'o', 'n']]]
        b = filter_(input('输入一个大于300的数:'), ('f_dec', 'int'))
        while b <= 300:
            b = filter_(input('输入一个大于300的数:'), ('f_dec', 'int'))
        convert_system(b, cm1='money=', returns=False, precision=0.1)
        print(b, '的质因数：', decomposition(b))
        b = filter_(input('输入一个字符串:'), input('将str转换成:'))
        print('转换后:', b)
        print('加密后：', absolute_encryption((input('输入你要加密的字符串:'))))
        print('等待1秒')
        wait(1)
        review(mmm, sep='.', line_sign=1)
        lists_ = list(range(3, 15, 2))
        print('打乱顺序前:', review(lists_), sep='')
        lists2_ = create_random_list(values=lists_)
        print('打乱顺序后:', review(lists2_), sep='')
        # draw1(right_=False, max_=200, clear_=True)
        get_files('..', True)

        divisionAlgorithm(42897, 18644)
        review(aa, all_values=True)
        review(aa)
        print(get_time_stamp())

    else:
        print('This is a local function.\n                     ————8388688')


def system_of_test():
    # from system_extend.py
    for k in generate_file_path(r'C:\Users\taskmgr_agent\AppData\Local\Application Data', True, from_size=1000,
                                to_size=1000000, suffix='exe'):
        print(k)


def get_suffix():
    # from default.py
    fp_1 = '..\\'
    k = set()
    for i in generate_file_path(fp_1, False):
        try:
            k.update({i.split('.')[-1]})
        except:
            print(k)
        finally:
            print(i)
    k = sorted(list(k))
    print(k)


def file_class_test():
    # from system_extend.py
    # file_example = File(r'I:\2020\8388688\病毒隔离区\kw\kw1_2_7.bat')
    file_example = File(r'I:\2020\8388688\病毒隔离区')
    print('文件路径fp=', file_example.fp)
    print('完整路径file_path=', file_example.file_path)
    print('文件名name=', file_example.name)
    print('扩展名(后缀)suffix=', file_example.suffix)
    # print('创建时间ct=', file_example.ct)
    print('转换后的ct=', get_time_stamp(file_example.ct))
    # print('修改时间mt=', file_example.mt)
    print('转换后的mt=', get_time_stamp(file_example.at))
    # print('访问时间at=', file_example.at)
    print('转换后的at=', get_time_stamp(file_example.at))
    print('大小size=', file_example.size)


def user_registry():
    # from game_disposition.py
    user1 = Users(name='6c4f2bbf-30a2-326c-90fe-', mode=0, psd='胡')
    user1.topUp(25)
    user1.save_user_info()


def normal_encr1():
    string1 = 'ABC! I am a sorting. ~!@#$%^&*()_+}{\"|?><:,/.\';\\[]-=' \
              '中文语言字符串, 〩~！@#￥%……&……*（）{——+}|“：》《？，。、；’【、-】=ffs___    df'
    bin_test = b'\xb0\xa1\xca\xd6\xb6\xaf\xb7\xa7\xb7\xa2\xc9\xe4\xb5\xe3\xb7\xa2\xc9\xfadads\xb7\xb6\xb5\xc2\xc8\xf8' \
               b'\xb7' \
               b'\xa2\xc9\xfa\xb5\xc4 % file_c % file_c % file_c % file_c % file_c % ' \
               b'file_c\xc8\xcb\xc9\xf9\xb6\xa6\xb7\xd0\xb9\xe3\xb6\xab\xca\xa1\r\n\r\n\r\n\xb5\xab\xca\xc7 ' \
               b'\\b\\nn\\n\\\\bb\\vb\\\\\r\nvvs 23g1ewr164\xa1\xb7\xa1\xb6\xa3\xbf\xa1\xb1|\xa3\xba}{' \
               b'+\xa3\xa9\xa1\xaa\xa1\xaa*\xa3\xa8*\xa1\xad\xa1\xad%\xa1\xad\xa1\xad\xa3\xa4#@\xa3\xa1~1\xa1' \
               b'\xa423299806' \
               b'\xa3\xac\xa1\xa2\xa1\xa3\xa1\xae\xa3\xbb\xa1\xa2\xa1\xbe\xa1\xbf-4=gbhdrehg\r\n\r\n\xb5\xc3\xb5\xbd' \
               b'\r\nf' \
               b'\r\n\r\nc\r\n '
    c = normal_encryption(bin_test, False, key='123456', coding='gbk')
    # print('-' * 80, c, type(c))
    # d = normalEncryption(c, False, encode='auto', key='123456')
    # print('-' * 80, d)


if __name__ == '__main__':
    # system_of_test()
    test()
