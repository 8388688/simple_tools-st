from simple_tools import *


def test():
    # from __init__.py
    if __name__ == '__main__':
        print(timestamp(presets=3))
        human1 = Person('steve')
        user1 = Users() if random_choice_old() else Users('电话')
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
                        c += 5
                    else:
                        c += 1
                    if c >= 250:
                        print('\033[1;31m你是存心来捣乱的吧！\033[0m')
                        times.sleep(1)
                        exit(0)
                if u2 == 'y':
                    break
        user3 = Users(u1)
        print(user1, user3, human1, sep='\n')
        aa = ['f', 'u', [['n', 'c'], 't', ['i', 'o', 'n'], {'金币': 0, '银币': 5, '铜板': 15}]]
        b = 0
        while b <= 300:
            b = filter_(input('输入一个大于300的数:'), ('f_dec', 'int'))
        print(b, '的质因数：', decomposition(b))
        print("科学计数法(1000)：", scientific_notate(b))
        print("科学计数法(1024)：",
              scientific_notate(b, rate=1024, custom_seq=("Byte", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB")))
        b = filter_(input('输入一个字符串:'), input('将str转换成:'))
        print('转换后:', b)
        print('等待3秒')
        wait(3)
        lists_ = list(range(3, 15, 2))
        print('打乱顺序前:', lists_)
        lists2_ = create_random_list(values=lists_)
        print('打乱顺序后:', lists2_)
        wait(1)
        for i in tree_fp_gen('../simple_tools', 1):
            print(i)

        print(gcd(42897, 18644))
        for i in bl_properties_gen(aa):
            print(i)

    else:
        print('This is a local function.\n%s————8388688' % " " * 20)


def file_class_test():
    # from system_extend.py
    # file_example = File(r'I:\2020\8388688\病毒隔离区\kw\kw1_2_7.bat')
    file_example = File(r'I:\2020\8388688\病毒隔离区')
    print('文件路径fp=', file_example.fp)
    print('完整路径file_path=', file_example.file_path)
    print('文件名name=', file_example.name)
    print('扩展名(后缀)suffix=', file_example.suffix)
    # print('创建时间ct=', file_example.ct)
    print('转换后的ct=', timestamp(file_example.ct))
    # print('修改时间mt=', file_example.mt)
    print('转换后的mt=', timestamp(file_example.at))
    # print('访问时间at=', file_example.at)
    print('转换后的at=', timestamp(file_example.at))
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
    c = rsa_crypt_easy(bin_test, 2, quiet=False, chunks=1)
    # =========================
    print("原始的:", bin_test)
    print("加密后:", c)
    d = rsa_crypt_easy(c, -2, quiet=False, chunks=1)
    print("解密后:", d)
    print("相等?", bin_test == d)
    print(rsa_crypt([132456489765465464984499, ], 2))


if __name__ == '__main__':
    # test()
    normal_encr1()
