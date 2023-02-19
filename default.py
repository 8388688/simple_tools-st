from http.client import RemoteDisconnected
from os.path import join
from requests import get
from requests.exceptions import ConnectTimeout, ConnectionError
from traceback import format_exc
from webbrowser import open as webbopen  # web browser open

from simple_tools.data_base import ST_WORK_SPACE, fp, null
from simple_tools.system_extend import delete

__all__ = ['clear_module_cache', 'get_update', 'pass_']
__version__ = '4.4-beta2'
version_code = 202302018001

LOG_FILE_PATH = join(ST_WORK_SPACE, 'default', 'get_update.txt', )
log_file_entity = open(LOG_FILE_PATH, 'a')
log_file_entity.close()


def clear_module_cache():
    delete(ST_WORK_SPACE)


def get_update():
    global log_file_entity
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/107.0.0.0 Safari/537.36',
        # 'Connection': 'close'  # 不使用持久连接
    }
    new_info = get(r'https://raw.githubusercontent.com/8388688/simple_tools/data/version.json', headers=headers).json()

    if new_info['version_code'] > version_code:
        print('有新版本可用：', new_info['version'], '（当前版本', __version__, '），更新内容：')
        for v in new_info['updatecontent']:  # 输出更新内容
            if new_info['updatecontent'][v][0] <= version_code:
                break
            print('└- ' + v + '：' + new_info['updatecontent'][v][1])
        if input('自动更新？（y/n）') == 'y':
            try:
                req = get(new_info['downloadurl'], stream=True)  # 这里需要对 url 更新
            except ConnectionRefusedError:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('[WinError 10061] 似乎 github.com 已拒绝连接。[ConnectionRefusedError]')

            except ConnectTimeout:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('github.com 加载缓慢。[ConnectTimeout]')
            except TimeoutError:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('github.com 连接超时。[TimeoutError]')
            except ConnectionError:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('无法连接 github.com。[ConnectionError]')
            except RemoteDisconnected:
                accident_is_happen = True
                traceback_exc = format_exc()
                print('请求头的 User-Agent 错误。[RemoteDisconnected]')
            else:
                accident_is_happen = False

            if accident_is_happen:
                print('是否打开镜像源（gitee.com）手动更新？(y/n)')
                log_file_entity = open(LOG_FILE_PATH, 'a')
                log_file_entity.write(traceback_exc + '\n')
                log_file_entity.close()

                if input() == 'y':
                    webbopen("https://gitee.com/meadeyetoe/simple_tools/releases/tag/v4.4-pre1")
                    return 1
                else:
                    return -3
            else:
                with open(f"simple_tools-{new_info['version']}.zip", 'wb') as package:
                    package.write(req.content)
        else:
            print('自动更新已取消\n你可以稍后进行手动更新\nGitHub: https://github.com/8388688/simple_tools\n'
                  'Gitee: https://gitee.com/meadeyetoe/simple_tools/releases/tag/v4.4-pre1\n'
                  '蓝奏云: \n1. https://imagine-8.lanzoue.com/ie3SB0mjnlsj\n'
                  '2. https://lanzoux.com/ie3SB0mjnlsj')


def pass_(returns=null):
    """没用的函数

    :return: returns
    """
    return returns


if __name__ == '__main__':
    get_update()
