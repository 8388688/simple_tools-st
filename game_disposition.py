from simple_tools.data_base import NULL
from random import randint
from time import time
from os import getenv, mkdir as md, system
from os.path import exists, join

from simple_tools.data_base import usernameList, EMPTY_UUID
from simple_tools.hash_values import get_md5, uuid_generator
from simple_tools.system_extend import file_remove, safe_md

__all__ = ['Person', 'Users']


class Person:
    INITIAL_PERSON = {'life': 100, 'hunger': 0, 'experience': 0, 'physicalStrength': 30, 'defense': 30,
                      'foods': {'food': {'土豆': 5, '面包': 3, '胡萝卜': 3, '牛奶': 3},
                                'fruits': {'苹果': 2, '香蕉': 2, '葡萄': 2, '梨': 2, '菠萝': 2},
                                'meats': {'生羊肉': 5, '生猪肉': 5, '生牛肉': 3, '生鱼': 3}}
                      }

    def __init__(self, name):
        self.name = name
        self.live = True  # 这个变量表示 "这个 entity 应该存在吗"
        self.life = Person.INITIAL_PERSON['life']
        self.hunger = Person.INITIAL_PERSON['hunger']
        self.experience = Person.INITIAL_PERSON['experience']
        self.physicalStrength = Person.INITIAL_PERSON['physicalStrength']
        self.defense = Person.INITIAL_PERSON['defense']
        self.foods = Person.INITIAL_PERSON['foods']

    def __str__(self):
        return self.name + '的资料：\n生命值:' + str(self.life) + '\n饥饿值:' + str(self.hunger) \
            + '\n经验值:' + str(self.experience) + '\n体力:' + str(self.physicalStrength) \
            + '\n防御值:' + str(self.defense)

    def __del__(self):
        del self.life, self.hunger, self.experience, self.physicalStrength, self.defense, self.foods
        print(self.name, '已死亡')
        del self.name


class Users:
    USER_INIT_INFO = {'diamond': 60, 'money': 500, 'live': True, 'state': 0}
    CAPABLE_USER_TYPE_LIST = ('register', 'vip_register')
    WORK_SPACE = join(getenv('APPDATA'), 'module1', 'game_disposition', 'class_users')
    TEMP_USER_NAME = '临时用户'

    safe_md(WORK_SPACE, quiet=True)
    SERVER_WORK_SPACE = join(WORK_SPACE, 'server')
    safe_md(SERVER_WORK_SPACE, quiet=True)
    USER_WORK_SPACE = join(WORK_SPACE, 'users')
    safe_md(USER_WORK_SPACE, quiet=True)

    USER_INFO_FILE_NAME = 'info.txt'
    NAME_LIST_FILE_NAME = join(SERVER_WORK_SPACE, 'namelist.txt')
    open(NAME_LIST_FILE_NAME, 'a').close()
    cache_naf = open(NAME_LIST_FILE_NAME, 'r')
    try:
        UserNameList = eval(cache_naf.read())
    except SyntaxError:
        print(NAME_LIST_FILE_NAME, '文件不存在或已损坏\n正在重制此文件')
        cache_naf = open(NAME_LIST_FILE_NAME, 'w')
        cache_naf.write('[]')

        UserNameList = []
    finally:
        cache_naf.close()
        del cache_naf

    def __init__(self, name=NULL, mode=0, psd='', encoding='UTF-8'):  # mode: 0 = register, 1 = login
        if mode == 0:
            if name is NULL:
                name = usernameList[0][randint(0, len(usernameList[0]))] + '的' + usernameList[3][
                    randint(0, len(usernameList[3]))] + usernameList[1][randint(0, len(usernameList[1]))]
            if name not in Users.UserNameList:
                self.info_dict = {'diamond': Users.USER_INIT_INFO['diamond'],
                                  'live': Users.USER_INIT_INFO['live'],
                                  'money': Users.USER_INIT_INFO['money'],
                                  'name': name,
                                  'password': get_md5(psd, encoding=encoding),
                                  'state': Users.USER_INIT_INFO['state'],
                                  'user_type': 'register',
                                  'uid': uuid_generator('md5')}
                # self.state: 0 = 正常离线, 1 = 在线, -1 = 不允许上线, -2 = 冻结状态
                self.live = True
                Users.UserNameList.append(self.info_dict['uid'])
                self.USER_PERSONAL_SPACE = join(Users.USER_WORK_SPACE, self.info_dict['uid'])
                md(self.USER_PERSONAL_SPACE)
                self.USER_INFO_FILE_PATH = join(self.USER_PERSONAL_SPACE, Users.USER_INFO_FILE_NAME)
                self.info_dict['state'] = 1
                print('用户成功创建 - %s' % self.info_dict['uid'])
                self.save_user_info()
            else:
                print(name, '- 用户名已存在！')
                self.live = False
                self.info_dict = {'user_type': 'temporary'}
                self.name = Users.TEMP_USER_NAME
                # del self
        elif mode == 1:
            self.login(name=name, password=psd)
        else:
            print('参数 mode 错误', mode)

    def __str__(self):
        return '当前用户：' + self.info_dict.get('name')

    def __del__(self):
        if self.info_dict.get('live', False) and self.info_dict.get(
                'user_type', 'temporary') in Users.CAPABLE_USER_TYPE_LIST:
            print('__del__: 保存用户信息. . .')
        else:
            print('删除', self.name, '的信息')
            if self.name in Users.UserNameList and self.name != Users.TEMP_USER_NAME:
                Users.UserNameList.remove(self.name)
                file_remove(join(Users.USER_WORK_SPACE, self.name),
                            all_files=True, all_folders=True, forces=True)
            else:
                print('试图删除 %s 用户时出现错误' % self.name)
                return
        print('正在断开', self.info_dict['name'], '用户的连接...')
        del self.info_dict
        print('完成...')

    def topUp(self, number=10):
        if self.info_dict.get('user_type', 'temporary') == 'register':
            if self.info_dict['state']:
                self.info_dict['money'] += number
                self.info_dict['diamond'] -= number / 10
                print('充值 %d 金币' % number)
                self.save_user_info()
            else:
                print(f'topUp: 拒绝访问 - 离线的用户')
        else:
            print('topUp: 拒绝访问 - 非正式用户')

    def returnName(self):
        """返回一个随机名字

        返回一个随机名字, 与 User 配对使用
        """

        u = usernameList[0][randint(0, len(usernameList[0]) - 1)] + '的' + usernameList[3][
            randint(0, len(usernameList[3]) - 1)] + usernameList[1][randint(0, len(usernameList[1]) - 1)] + \
            usernameList[3][randint(0, len(usernameList[3]) - 1)]
        return u

    def save_user_info(self):
        if self.live and self.info_dict.get('user_type', 'temporary') in Users.CAPABLE_USER_TYPE_LIST:
            if self.info_dict['state']:
                id_list_file = open(join(Users.SERVER_WORK_SPACE, Users.NAME_LIST_FILE_NAME), 'w')
                id_list_file.write(str(Users.UserNameList))
                id_list_file.close()
                del id_list_file
                self.user_info_file = open(self.USER_INFO_FILE_PATH, 'w')
                self.user_info_file.write(str(self.info_dict))
                self.user_info_file.close()
                del self.user_info_file
                print('保存', self.info_dict['name'], '的信息')
            else:
                print('save_user_info: 拒绝访问 - 离线用户')
        else:
            print(self, '不属于正式用户')

    def login(self, name, password=NULL, encoding='utf-8'):
        if name in Users.UserNameList:
            # self.info_dict = {}
            # self.info_dict.update({'name': name})
            print('已找到 ID 为 %s 的用户' % name)
            self.USER_INFO_FILE_PATH = join(Users.USER_WORK_SPACE, name, Users.USER_INFO_FILE_NAME)

            open(self.USER_INFO_FILE_PATH, 'a').close()
            self.user_info_file = open(self.USER_INFO_FILE_PATH, 'r')

            try:
                self.info_dict = eval(self.user_info_file.read())
            except SyntaxError:
                self.user_info_file.close()
                print(name, '的', self.USER_INFO_FILE_PATH, '文件已损坏\n正在重制此文件')
                self.user_info_file = open(self.USER_INFO_FILE_PATH, 'w')

                self.info_dict = {'diamond': Users.USER_INIT_INFO['diamond'],
                                  'live': Users.USER_INIT_INFO['live'],
                                  'money': Users.USER_INIT_INFO['money'],
                                  'name': self.returnName(),
                                  'password': get_md5(password, encoding=encoding),
                                  'state': Users.USER_INIT_INFO['state'],
                                  'user_type': 'register',
                                  'uid': name}
                self.user_info_file.write(str(self.info_dict))
                self.user_info_file.close()
                print('login正在重新登录')
                self.login(name=self.info_dict.get('uid', EMPTY_UUID),
                           password=self.info_dict['password'])
            else:
                self.user_info_file.close()
                print('完成读取')
            finally:
                self.live = True
                # del self.user_info_file

            if password == self.info_dict.get('password', ''):
                self.info_dict['state'] = 1
                self.save_user_info()
                print('登陆成功')
            else:
                print('登录失败 - 密码错误')
                self.info_dict['state'] = 0
        else:
            print('用户提供的 uid 不存在!')
            self.name = self.returnName()
            self.info_dict = {'diamond': Users.USER_INIT_INFO['diamond'],
                              'live': Users.USER_INIT_INFO['live'],
                              'money': Users.USER_INIT_INFO['money'],
                              'name': name,
                              'password': get_md5(password, encoding=encoding),
                              'state': Users.USER_INIT_INFO['state'],
                              'user_type': 'register',
                              'uid': uuid_generator('md5')}

            Users.UserNameList.append(self.info_dict.get(
                'uid', EMPTY_UUID))
            del self.name
            self.USER_PERSONAL_SPACE = join(Users.USER_WORK_SPACE, self.info_dict['uid'])
            md(self.USER_PERSONAL_SPACE)
            self.live = True
            self.USER_INFO_FILE_PATH = join(self.USER_PERSONAL_SPACE, Users.USER_INFO_FILE_NAME)
            self.save_user_info()
            self.login(name=self.info_dict['uid'], password=self.info_dict['password'])
            print('随机 ID 成功创建')

    def register(self):
        pass

    def rename(self, newname=NULL):
        if self.info_dict['state'] == 1:
            if newname is NULL:
                pass
            else:
                self.info_dict['name'] = newname
        else:
            print('rename拒绝访问 - 离线用户')

    def logout(self):
        self.info_dict['state'] = 0
