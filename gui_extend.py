# 空空如也。
# 以后可能会加进一些东西（可能得等到 2024 年以后，目前不要抱太大希望）。

from os import system
from os.path import join
from sys import executable

from simple_tools.data_base import ST_WORK_SPACE
from simple_tools.system_extend import safe_md

__all__ = ['check_and_install_package']

LOCAL_WORK_SPACE = join(ST_WORK_SPACE, 'gui_extend')

safe_md(join(LOCAL_WORK_SPACE, 'pip-cache'))


def check_and_install_package(*args):
    print(
        '\033[0;31m' + check_and_install_package.__name__ + ' 目前主要问题：无法检测过时升级的包，也无法自动升级这些包。\033[0m')
    pip_freeze_path = join(LOCAL_WORK_SPACE, 'pip-cache', 'pipfreeze.txt')
    system(executable + f" -m pip freeze>{pip_freeze_path}")
    pip_freeze_log = open(pip_freeze_path, 'r')
    pkg_list = pip_freeze_log.readlines()
    pip_freeze_log.close()
    pkg_list = map(lambda x: x.strip('\n').split('==')[0], pkg_list)

    for pkg in args:
        '''
        try:
            import "pkg"
        except ModuleNotFoundError:
            print(f"\n您没有安装 {pkg} 库，正在为您自动安装！")
            system(executable + f" -m pip install {pkg}")
            print("安装完成！")
            import "pkg"
        '''
        if pkg not in pkg_list:
            print(f"\n您没有安装 {pkg} 库，正在为您自动安装。")
            system(executable + f" -m pip install {pkg}")
            print(f"安装完成。执行以下语句以导入 {pkg} 库（目前无法自动导入）。\n    import {pkg}")
        else:
            print(f'You have already installed \"{pkg}\" package.')
