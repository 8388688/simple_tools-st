from time import time, localtime, strftime, sleep
from simple_tools.data_base import NULL, null

__all__ = ['get_time_stamp', 'wait']


def get_time_stamp(v_time=NULL, busy=False, **kwargs) -> str:
    """获取美化的时间

    在 module1 v3.3 更新的版本上，我们准备了 23,529,242,880 种不同的时间戳格式以及 5 个预设值，打造属于自己的时间戳。
    注意: kwargs 中 presets 可选项是一个 int 值:
    > 为 0 表示不使用预设值
    > 大于 0 时使用预设值的第 (presets - 1) 个值
    > 不设置或设置为负数时则使用默认预设值
    no_beauty: 不使用任何装饰

    @param v_time: 要转换的 unix 时间戳
    @param busy: 精确到小数点后的时间
    @param kwargs: 高级选项
    @return: 一个字符串
    """
    prop_seconds = ('', '%S', '%S ', '%SZ', '%S秒', '%S秒 ')
    prop_minutes = ('', '%M', '%M ', '%M,', '%M-', '%M.', '%M/', '%M:', '%M\\', '%M_', '%M分', '%M分 ')
    prop_hours = ('', '%H', '%H ', '%H,', '%H-', '%H.', '%H/', '%H:', '%H\\', '%H_', '%H时', '%H时 ',
                  '%I', '%I ', '%I,', '%I-', '%I.', '%I/', '%I:', '%I\\', '%I_', '%I时', '%I时 ')
    prop_local_12_hours = ('', ' %p', '%p', '%p ', '%p:', ':%p')
    prop_days = ('', '%d', '%d ', '%d,', '%d-', '%d.', '%d/', '%d:', '%dT', '%d\\', '%d_', '%d日', '%d日 ')
    prop_months = ('', '%m', '%m ', '%m,', '%m-', '%m.', '%m/', '%m:', '%m\\', '%m_', '%m月', '%m月 ')
    prop_years = ('', '%Y', '%Y ', '%Y,', '%Y-', '%Y.', '%Y/', '%Y:', '%Y\\', '%Y_', '%Y年', '%Y年 ',
                  '%y', '%y ', '%y,', '%y-', '%y.', '%y/', '%y:', '%y\\', '%y_', '%y年', '%y年 ')
    prop_weeks = ('', ' %A', ' %a', ' %w', '%A', '%A ', '%a', '%a ', '%w', '%w ')
    prop_time_presets = (
        (
            prop_years[4], prop_months[4], prop_days[2], prop_weeks[0],
            prop_local_12_hours[0], prop_hours[7], prop_minutes[7], prop_seconds[1]
        ),  # 经典时间格式, example: "yyyy-mm-dd hh-mm-ss"
        (
            prop_years[10], prop_months[10], prop_days[12], prop_weeks[5],
            prop_local_12_hours[3], prop_hours[10], prop_minutes[10], prop_seconds[5]
        ),  # 详细时间, example: "week yyyy年mm月dd日 (am|pm) hh时mm分ss秒"
        (
            prop_years[9], prop_months[9], prop_days[10], prop_weeks[0],
            prop_local_12_hours[0], prop_hours[9], prop_minutes[9], prop_seconds[1]
        ),  # 文本时间, example: "yyyy_mm_dd_hh_mm_ss"
        (
            prop_years[1], prop_months[1], prop_days[1], prop_weeks[0],
            prop_local_12_hours[0], prop_hours[1], prop_minutes[1], prop_seconds[1]
        ),  # 纯数字时间, example: "yyyymmddhhmmss"
        (
            prop_years[1], prop_months[1], prop_days[8], prop_weeks[0],
            prop_local_12_hours[0], prop_hours[1], prop_minutes[1], prop_seconds[3]
        ),  # 通用 unix 时间, example: "yyyymmddThhmmssZ"
    )

    properties_format = kwargs
    if 'presets' not in properties_format:
        pv_year, pv_month, pv_day, pv_week, pv_hour_12, pv_hour, pv_minute, pv_second = \
            prop_years[properties_format.get('pf_year', 0)], \
                prop_months[properties_format.get('pf_month', 0)], \
                prop_days[properties_format.get('pf_day', 0)], \
                prop_weeks[properties_format.get('pf_week', 0)], \
                prop_local_12_hours[properties_format.get('pf_hour_12', 0)], \
                prop_hours[properties_format.get('pf_hour', 0)], \
                prop_minutes[properties_format.get('pf_minute', 0)], \
                prop_seconds[properties_format.get('pf_second', 0)]
    elif properties_format.get('presets', -1) < 0:
        pv_year, pv_month, pv_day, pv_week, pv_hour_12, pv_hour, pv_minute, pv_second = prop_time_presets[0]
    else:
        pv_year, pv_month, pv_day, pv_week, pv_hour_12, pv_hour, pv_minute, pv_second = \
            prop_time_presets[properties_format.get('presets', -1)]
    properties = (
        pv_year + pv_month + pv_day + pv_week + pv_hour_12 + pv_hour + pv_minute + pv_second,
        pv_week + pv_year + pv_month + pv_day + pv_hour_12 + pv_hour + pv_minute + pv_second,
        pv_month + pv_year + pv_day + pv_week + pv_hour_12 + pv_hour + pv_minute + pv_second,
        pv_week + pv_month + pv_year + pv_day + pv_hour_12 + pv_hour + pv_minute + pv_second,
        pv_day + pv_month + pv_year + pv_week + pv_hour_12 + pv_hour + pv_minute + pv_second,
        pv_week + pv_day + pv_year + pv_month + pv_hour_12 + pv_hour + pv_minute + pv_second,
    )  # 时间格式

    properties_beauty = properties[properties_format.get('pf_format', 1)]  # 未装饰前的时间格式

    prop_des = (
        properties_beauty,
        '\n' + '-' * 10 + properties_beauty + '-' * 10 + '\n',
        '-' * 10 + ' ' + properties_beauty + ' ' + '-' * 10 + '\n',
        '-' * 20 + ' ' + properties_beauty + ' ' + '-' * 20 + '\n',
        '~' * 10 + ' ' + properties_beauty + ' ' + '~' * 10 + '\n',
        '~' * 20 + ' ' + properties_beauty + ' ' + '~' * 20 + '\n',
        '*' * 10 + ' ' + properties_beauty + ' ' + '*' * 10 + '\n',
        '*' * 20 + ' ' + properties_beauty + ' ' + '*' * 20 + '\n',
        '#' * 10 + ' ' + properties_beauty + ' ' + '#' * 10 + '\n',
        '#' * 20 + ' ' + properties_beauty + ' ' + '#' * 20 + '\n',
        '=' * 10 + ' ' + properties_beauty + ' ' + '=' * 10 + '\n',
        '=' * 20 + ' ' + properties_beauty + ' ' + '=' * 20 + '\n',
    )  # 装饰格式

    __all_format = (
        len(prop_years) * len(prop_months) * len(prop_days) * len(prop_local_12_hours) * len(prop_hours) * len(
            prop_minutes) * len(prop_seconds) * len(prop_weeks) * len(properties) * len(prop_des),
        len(prop_time_presets)
    )
    # print(__all_format) # 统计共生成了多少种不同格式的时间戳

    if properties_format.get('no_beauty', False):
        properties_finally = prop_des[properties_format.get('pf_beauty', 0)]
    else:
        properties_finally = prop_des[properties_format.get('pf_beauty', 2)]

    if v_time == NULL:
        v_time = time()
    format_time = properties_finally
    if busy:
        return strftime(format_time, localtime(v_time)) + '.' + str(v_time).split('.')[-1]
    else:
        return strftime(format_time, localtime(v_time))


def wait(seconds=null, busy_loop=NULL):
    """等待

    具体略

    :param seconds: 等待的秒数。
    :param busy_loop: 精确等待，默认为 NULL（自动判断）。
    \n 如果 busy_loop 为 True，则精确更新，如果为 False，则只用 sleep() 函数。
    \n 当 busy_loop 被启用时，如果 seconds 的值很大，将会非常占用系统资源，所以除非对精确度要求很高，否则一般不建议启用 busy_loop。
    """
    cache_times = time()
    if busy_loop is NULL:
        if seconds == null:
            pass
        else:
            sleep(seconds)
            while time() - cache_times < seconds % 1:
                pass
    elif busy_loop:
        while time() - cache_times < seconds:
            pass
    else:
        sleep(seconds)
    return seconds
