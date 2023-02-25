# 中文名: system_扩展
import os
from os.path import dirname
from sys import getdefaultencoding as gde
from builtins import open as fopen

from simple_tools.data_base import NULL, ST_WORK_SPACE, pass_
from simple_tools.times import get_time_stamp as gettime, wait
from stat import *
from traceback import format_exc

SYSTEM_EXTEND_WORK_SPACE = os.path.join(ST_WORK_SPACE, 'system_extend')

log_file_path = os.path.join(SYSTEM_EXTEND_WORK_SPACE, 'logs.txt')
log_file_entity = fopen(log_file_path, 'a')
log_file_entity.write('-' * 10 + gettime() + '-' * 10 + '\n' + 'file:' + __name__ + '\n' + 'path:' + __file__)
log_file_entity.close()

__all__ = ['File',
           'fp', 'delete', 'get_files',
           'file_pattern', 'file_remove', 'get_file_name',
           'get_file_path', 'generate_file_path',
           'get_file_size', 'get_file_suffix', 'safe_md']

fp = os.getcwd()

system_pro = 'mac-os' if os.path.join('ab', 'cd') == 'ab/cd' else \
    ('windows' if os.path.join('ab', 'cd') == 'ab\\cd' else 'unknown')


class File:
    def __init__(self, file_path):
        print(f'WARNING: function {File.__name__} is still a Experimental Features')
        if os.path.exists(file_path):
            self.file_path = os.path.abspath(file_path)
            self.fp = os.path.dirname(file_path)
            self.name = file_path.split('\\')[-1] if system_pro == 'windows' else (
                file_path.split('/')[-1] if system_pro == 'mac-os' else file_path)

            file_stat = os.stat(file_path)

            if S_ISREG(file_stat[0]):  # 判断是否一般文件
                self.file_mode = 'Regular file'
            elif S_ISLNK(file_stat[0]):  # 判断是否链接文件
                self.file_mode = 'Shortcut'
            elif S_ISSOCK(file_stat[0]):  # 判断是否套接字文件
                self.file_mode = 'Socket'
            elif S_ISFIFO(file_stat[0]):  # 判断是否命名管道
                self.file_mode = 'Named pipe'
            elif S_ISBLK(file_stat[0]):  # 判断是否块设备
                self.file_mode = 'Block special device'
            elif S_ISCHR(file_stat[0]):  # 判断是否字符设置
                self.file_mode = 'Character special device'
            elif S_ISDIR(file_stat[0]):  # 判断是否目录
                self.file_mode = 'directory'
            # 额外的两个函数
            elif S_IMODE(file_stat[0]):
                self.file_mode = 'chmod format'
            elif S_IFMT(file_stat[0]):
                self.file_mode = 'type of fiel'
            else:
                self.file_mode = 'unknown'
            # print(S_IMODE(file_stat[0]))  # 返回文件权限的chmod格式
            # print(S_IFMT(file_stat[0]))  # 返回文件的类型

            self.create_time = self.ct = os.stat(file_path).st_ctime  # 文件创建时间
            self.access_time = self.at = os.stat(file_path).st_atime  # 文件最后访问时间
            self.modification_time = self.mt = os.stat(file_path).st_mtime  # 文件最后修改时间
            self.permission = file_stat.st_mode  # 权限模式
            self.inode_number = file_stat.st_ino  # inode number
            self.device = file_stat.st_dev  # device
            self.num_link = file_stat.st_nlink  # number of hard links
            self.user_id = file_stat.st_uid  # 所有用户的user id
            self.group_id = file_stat.st_gid  # 所有用户的group id
            self.file_size = file_stat.st_size

            if os.path.isfile(file_path):
                self.size = os.path.getsize(file_path)
                self.suffix = self.name.split('.')[-1]
            else:
                # self.size = get_file_size(file_path)
                self.size = NULL
                self.suffix = NULL

            """
            stat.S_ISUID: Set user ID on execution.                      不常用
            stat.S_ISGID: Set group ID on execution.                    不常用
            stat.S_ENFMT: Record locking enforced.                                          不常用
            stat.S_ISVTX: Save text image after execution.                                在执行之后保存文字和图片
            stat.S_IREAD: Read by owner.                                                           对于拥有者读的权限
            stat.S_IWRITE: Write by owner.                                                         对于拥有者写的权限
            stat.S_IEXEC: Execute by owner.                                                       对于拥有者执行的权限
            stat.S_IRWXU: Read, write, and execute by owner.                          对于拥有者读写执行的权限
            stat.S_IRUSR: Read by owner.                                                            对于拥有者读的权限
            stat.S_IWUSR: Write by owner.                                                          对于拥有者写的权限
            stat.S_IXUSR: Execute by owner.                                                       对于拥有者执行的权限
            stat.S_IRWXG: Read, write, and execute by group.                           　　　　　　对于同组的人读写执行的权限
            stat.S_IRGRP: Read by group.                                                             对于同组读的权限
            stat.S_IWGRP: Write by group.                                                           对于同组写的权限
            stat.S_IXGRP: Execute by group.                                                        对于同组执行的权限
            stat.S_IRWXO: Read, write, and execute by others.                          对于其他组读写执行的权限
            stat.S_IROTH: Read by others.                                                           对于其他组读的权限
            stat.S_IWOTH: Write by others.                                                         对于其他组写的权限
            stat.S_IXOTH: Execute by others.                                                      对于其他组执行的权限
            """

    def read(self):
        pass

    def write(self):
        pass

    def rename(self):
        pass

    def move(self):
        pass

    def copy(self):
        pass

    def delete(self):
        pass


def file_pattern(file_path=fp, binary=True, easy_options=False):
    """判断一个 file 类型

    文件代码：
    -5 = 内存不足
    -4 = 内置错误
    -3 = 拒绝访问
    -2 = 找不到文件
    -1 = 未知的错误
    1 = 空文件夹
    2 = 不是空的文件夹
    3 = 空文件
    4 = 不是空的文件

    :param file_path: 文件路径
    :param binary: 数字返回/模拟返回，默认为数字返回
    :param easy_options: 使函数返回简单的 True/False 值而不是更高级的返回方式
    :return: 未知
    """
    key_val = {1: ('空文件夹',), 2: ('不是空的文件夹',), 3: ('空文件',), 4: ('不是空的文件',),
               -1: ('错误 - 未知的错误',), -2: ('错误 - 找不到文件',), -3: ('错误 - 拒绝访问',), -4: ('内置错误',),
               -5: ('错误 - 内存不足',), -6: ('错误 - 文件路径无法识别',)}
    nor_code = (1, 2, 3, 4,)
    problem_code = (-6, -3, -2, -1,)
    undef_code = (-4, -5)
    button = -1
    now_fp = fp
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            if os.path.getsize(file_path) <= 1:
                button = 3
            else:
                button = 4
        elif os.path.isdir(file_path):
            try:
                os.listdir(file_path)
            except PermissionError:
                button = -3
            except MemoryError:
                button = -5
            else:
                if os.listdir(file_path):
                    button = 2
                else:
                    button = 1
        else:
            button = -6
    else:
        if len(file_path) >= 255:
            button = -6
        else:
            button = -2

    if easy_options:
        if button in nor_code:
            return True
        elif button in problem_code:
            return False
        else:
            return None
    else:
        if binary:
            return button
        else:
            return key_val.get(button, key_val.get(-4))


def file_remove(file_path=fp, all_files=False, all_folders=False,
                forces=False, confirms=False, quiet=False, **kwargs):
    """删除一个或多个文件

    :param file_path: 指定的文件路径，可以是文件，也可以是文件夹。
    :param all_files: 如果 file_path 指定了一个文件夹，这个参数将会删除 file_path 中的所有指定的文件。
    :param all_folders: 如果 file_path 指定了一个文件夹，这个参数将会删除 file_path 中的所有指定的子文件夹。
    :param forces: 强制删除只读文件.
    :param confirms: 删除每一个文件之前提示确认.
    :param quiet: 安静模式(此参数与 confirms 参数不能同时为 True)。
    :return: 如果删除成功的话返回 0，否则返回非 0 值
    """

    new_path = file_path  # 文件路径
    delete_dir = True

    def only_remove(file_or_dir):
        nonlocal delete_dir
        if os.path.exists(file_or_dir):  # 如果文件存在
            if confirms:
                select = input('确定删除%s吗?(<Any> or <space>)' % file_or_dir)
            else:
                select = True
            if select:
                # 删除文件，可使用以下两种方法。
                if forces:
                    os.chmod(file_or_dir, S_IWRITE)
                if not quiet:
                    print('删除文件 - %s' % file_or_dir)
                if os.path.isfile(file_or_dir):
                    os.remove(file_or_dir)
                    # os.unlink(path)
                elif all_folders:
                    os.rmdir(file_or_dir)
                else:
                    print('跳过%s' % file_or_dir)
                    delete_dir = False
            else:
                print('操作已取消')
                delete_dir = False
        else:
            print('错误 - 找不到\"%s\"' % file_or_dir)  # 否则返回文件不存在
            delete_dir = False
            # return 1

    for a000 in generate_file_path(new_path, abspath=True, folders=all_folders, all_files=all_files,
                                   do_file=lambda f: only_remove(f), do_dir=lambda f2: only_remove(f2)):
        # print('将要删除的文件:', a000, 'Size:', os.path.getsize(a000))
        pass_()

    if delete_dir and os.path.exists(new_path):
        os.rmdir(new_path)
    return 0


def get_file_name(file_dir=fp):
    key_val = (('出错了(未知的错误)', []),
               ('出错了(内置错误: 未知)', []),
               ('出错了(内置错误: 下标越界)', []),
               ('出错了(找不到文件)', []),
               ('保留位置', []),
               ('出错了(拒绝访问)', []),
               ('出错了(unicode编码错误)', []),
               ('出错了(系统无法辨识文件名)', []))
    button = 0

    def _fprint(*args, step=' ', end='\n'):
        try:
            for string in args:
                print(str(string) + step, sep='', end='')
            print(end, end='')
        except UnicodeEncodeError:
            print('print() 函数似乎出现了错误')
            string = string.encode(gde())
            print(string)

    with fopen(os.path.join(SYSTEM_EXTEND_WORK_SPACE, 'lastrun.txt'), 'ab+') as traceback_file:
        traceback_file.write(('-' * 10 + gettime() + '-' * 10 + '\n').encode(gde()))

        if os.path.isfile(file_dir):
            return []
        else:
            try:
                return os.listdir(file_dir)
            except FileNotFoundError:
                button = 3
                _fprint('%s\"%s\"' % (key_val[button], file_dir))
                traceback_event = format_exc()
                traceback_file.write(traceback_event.encode(gde()))
                return key_val[button][1]
            except PermissionError:
                button = 5
                _fprint('%s\"%s\"' % (key_val[button], file_dir))
                traceback_event = format_exc()
                traceback_file.write(traceback_event.encode(gde()))
                return key_val[button][1]
            except UnicodeEncodeError:
                button = 6
                _fprint('%s\"%s\"' % (key_val[button], file_dir))
                traceback_event = format_exc()
                traceback_file.write(traceback_event.encode(gde()))
                return key_val[button][1]
            except IndexError:
                button = 2
                _fprint('%s\"%s\"' % (key_val[button], file_dir))
                traceback_event = format_exc()
                traceback_file.write(traceback_event.encode(gde()))
                return key_val[button][1]
            except OSError:
                button = 7
                _fprint('%s\"%s\"' % (key_val[button], file_dir))
                traceback_event = format_exc()
                traceback_file.write(traceback_event.encode(gde()))
                return key_val[button][1]
            except:
                button = 1
                _fprint('%s\"%s\"' % (key_val[button], file_dir))
                traceback_event = format_exc()
                traceback_file.write(traceback_event.encode(gde()))
                return key_val[button][1]
            finally:
                traceback_file.write('\n'.encode(gde()))
                traceback_file.close()


def get_file_path(file_path=fp, abspath=NULL, folders=False, format_list=False, **kwargs):
    """获取文件路径

    输出时检测如果是一个文件夹，就以列表的格式输出，否则以str的格式输出

    :param file_path: 目标文件或路径
    :param abspath: 使用绝对路径
    :param folders: 也输出文件夹
    :param format_list: 输出时强制转换成列表格式
    :param kwargs: 高级选项：
    \n from_size: 限制文件大小下限
    \n to_size: 限制文件大小上限
    \n suffix: 限制文件后缀名(不加“.”)
    :return: 如果是一个目录就以列表的格式输出，否则以str的格式输出

    """
    files = []
    fx = get_file_name(file_path)
    extension = kwargs
    from_size = extension.get('from_size', 0)
    to_size = extension.get('to_size', NULL)
    suffix = extension.get('suffix', NULL)
    include = extension.get('include', NULL)
    exclude = extension.get('exclude', NULL)
    case_sensitive = extension.get('case_sensitive', False)
    # extension.get('', default=NULL)

    for file in fx:
        if os.path.isfile(os.path.join(file_path, file)):
            if (to_size is NULL or os.path.getsize(os.path.join(file_path, file)) < to_size) \
                    and from_size < os.path.getsize(os.path.join(file_path, file)) and \
                    (suffix is NULL or os.path.join(file_path, file).split('.')[-1] == suffix) and \
                    (include is NULL or list(filter(
                        lambda pi: (pi in os.path.join(file_path, file)) if case_sensitive else (
                                pi.lower() in os.path.join(file_path, file).lower()), include))) and \
                    (exclude is NULL or not list(filter(
                        lambda pe: (pe in os.path.join(file_path, file)) if case_sensitive else (
                                pe.lower() in os.path.join(file_path, file).lower()), exclude))):
                if abspath:
                    files.append(str(os.path.join(os.path.abspath(file_path), file)))
                elif abspath is NULL:
                    files.append(str(os.path.join(file_path, file)))
                else:
                    files.append(str(file))
        else:
            if format_list:
                for i in get_file_path(os.path.join(file_path, file) + '\\', abspath=abspath,
                                       format_list=format_list,
                                       from_size=extension.get('from_size', 0),
                                       to_size=extension.get('to_size', NULL),
                                       suffix=extension.get('suffix', NULL),
                                       include=extension.get('include', NULL),
                                       exclude=extension.get('exclude', NULL),
                                       case_sensitive=case_sensitive):
                    files.append(i)
                if folders:
                    files.append(os.path.join(file_path, file))
            else:
                files.append(get_file_path(os.path.join(file_path, file) + '\\', abspath=abspath,
                                           format_list=format_list,
                                           from_size=extension.get('from_size', 0),
                                           to_size=extension.get('to_size', NULL),
                                           suffix=extension.get('suffix', NULL),
                                           include=extension.get('include', NULL),
                                           exclude=extension.get('exclude', NULL),
                                           case_sensitive=extension.get('case_sensitive', False)))

    if os.path.isfile(file_path):
        if abspath:
            return os.path.abspath(file_path)
        elif format_list:
            return [file_path, ]
        else:
            return file_path
    else:
        if format_list:
            return [files, ]
        else:
            return files


def generate_file_path(file_path=fp, abspath=NULL, folders=False, __deep=0, **kwargs):
    """获取文件路径

    输出时检测如果是一个文件夹，就以列表的格式输出，否则以str的格式输出
    \n from_size: 限制文件大小下限
    \n to_size: 限制文件大小上限
    \n suffix: 限制文件后缀名(不加".")
    \n include: 包含的文件夹, (未指定就是全部)
    \n exclude: 排除的文件夹, (格式: 推荐元组, 但也可以用列表)
    \n case_sensitive: [针对 include]是否区分大小写, 默认为 False(不区分)
    \n do_file: 针对每一个文件要做什么
    \n do_dir: 针对每一个文件夹要做什么

    示例:
    ```python

        for i in generate_file_path('H:/2020/Temp', folders=True,
                                do_file=lambda f: print(f, 'isfile:', os.path.isfile(f)),
                                do_dir=lambda f2: print(f2, 'isdir:', os.path.isdir(f2))):
            pass
    ```
    --------
    或者是这样
    ```python
        # 删除 `H:/2020/Temp` 中的所有文件（文件夹）
        for i in generate_file_path('H:/2020/Temp', folders=True,
                                do_file=lambda f: os.unlink(f),
                                do_dir=lambda f2: os.rmdir(f2)):
            print('Delete file:', i)
    ```

    :param file_path: 目标文件或路径
    :param abspath: 使用绝对路径
    :param folders: 也输出文件夹
    :param __deep: 文件递归深度(未使用)
    :param kwargs: 高级选项:
    :return: 如果是一个目录就以列表的格式输出，否则以str的格式输出

    """
    fx = get_file_name(file_path)

    extension = kwargs
    from_size = extension.get('from_size', -1)
    to_size = extension.get('to_size', NULL)
    suffix = extension.get('suffix', NULL)
    include = extension.get('include', NULL)
    exclude = extension.get('exclude', NULL)
    case_sensitive = extension.get('case_sensitive', False)
    do_file = extension.get('do_file', pass_)
    do_dir = extension.get('do_dir', pass_)
    # extension.get('', default=NULL)

    for file in fx:
        if os.path.isfile(os.path.join(file_path, file)):
            if (to_size is NULL or os.path.getsize(os.path.join(file_path, file)) < to_size) \
                    and from_size <= os.path.getsize(os.path.join(file_path, file)) and \
                    (suffix is NULL or os.path.join(file_path, file).split('.')[-1] == suffix) and \
                    (include is NULL or list(filter(
                        lambda pi: (pi in os.path.join(file_path, file)) if case_sensitive else (
                                pi.lower() in os.path.join(file_path, file).lower()), include))) and \
                    (exclude is NULL or not list(filter(
                        lambda pe: (pe in os.path.join(file_path, file)) if case_sensitive else (
                                pe.lower() in os.path.join(file_path, file).lower()), exclude))):
                if abspath:
                    yield str(os.path.join(os.path.abspath(file_path), file))
                elif abspath is NULL:
                    yield str(os.path.join(file_path, file))
                else:
                    yield str(file)
                do_file(str(os.path.join(os.path.abspath(file_path), file)))
        else:
            for a000 in generate_file_path(os.path.join(file_path, file) + '/', abspath=abspath, folders=folders,
                                           from_size=from_size, to_size=to_size, suffix=suffix, include=include,
                                           exclude=exclude, case_sensitive=case_sensitive, do_file=do_file,
                                           do_dir=do_dir):
                yield a000
            if folders:
                yield os.path.join(file_path, file)
                do_dir(os.path.join(file_path, file))


def get_file_size(path_var=fp, all_files=True, details=False, **kwargs):
    extension = kwargs
    from_size = extension.get('from_size', 0)
    to_size = extension.get('to_size', NULL)
    suffix = extension.get('suffix', NULL)
    include = extension.get('include', NULL)
    exclude = extension.get('exclude', NULL)
    case_sensitive = extension.get('case_sensitive', False)
    # extension.get('', default=NULL)

    size, files, folders = 0, 0, 0
    if os.path.isdir(path_var):
        for i in os.listdir(path_var):
            path_new = os.path.join(path_var, i)
            if os.path.isfile(path_new):
                if (to_size is NULL or os.path.getsize(os.path.join(path_var, i)) < to_size) \
                        and from_size < os.path.getsize(os.path.join(path_var, i)) and \
                        (suffix is NULL or os.path.join(path_var, i).split('.')[-1] == suffix) and \
                        (include is NULL or list(filter(
                            lambda pi: (pi in os.path.join(path_var, i)) if case_sensitive else (
                                    pi.lower() in os.path.join(path_var, i).lower()), include))) and \
                        (exclude is NULL or not list(filter(
                            lambda pe: (pe in os.path.join(path_var, i)) if case_sensitive else (
                                    pe.lower() in os.path.join(path_var, i).lower()), exclude))):
                    files += 1
                    size += os.path.getsize(path_new)
            elif all_files:
                folders += 1
                gfs = get_file_size(path_new, True, True, from_size=from_size, to_size=to_size,
                                    suffix=suffix, include=include, exclude=exclude,
                                    case_sensitive=case_sensitive)
                size += gfs[0]
                files += gfs[1]
                folders += gfs[2]
            else:
                print(path_new, '是文件夹')
    else:
        files += 1
        size += os.path.getsize(path_var)
    if details:
        return size, files, folders
    else:
        return size


def get_file_suffix(file_path=fp, sort=True, show_details=False):
    fp_ = file_path
    keys = []

    for i in generate_file_path(fp_, abspath=False):
        keys.append(str.lower(i.split('.')[-1]))
        if show_details:
            print(i)

    if sort:
        keys = sorted(list(set(keys)))
    log_file_entity.writelines(keys)
    return keys


def safe_md(file_name_or_file_path, quiet=False):
    lfe = fopen(log_file_path, 'a')
    try:
        tell = '%s 存在\n' % file_name_or_file_path
        os.mkdir(file_name_or_file_path) if not os.path.exists(file_name_or_file_path) else pass_()
    except FileNotFoundError:
        tell = '创建文件夹时出现错误: 指定的文件夹不存在 - %s\n正在重新创建. . .\n' % file_name_or_file_path
        # safe_md(dirname(file_name_or_file_path))
        # safe_md(file_name_or_file_path)
    except FileExistsError:
        tell = '创建文件夹时出现错误 - %s 文件已存在\n' % file_name_or_file_path
    except:
        tell = '[未知错误]错误如下:\n' + format_exc()
    else:
        tell = '%s 已成功创建\n' % file_name_or_file_path
    lfe.write(tell)
    print(tell, end='') if not quiet else pass_()

    lfe.close()


def quick_create_file(file_path, size):
    fx = open(file_path, 'wb')
    fx.seek(size - 1)
    fx.write(b'\x00')
    fx.close()


delete = file_remove
get_files = generate_file_path
