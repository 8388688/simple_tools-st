�ļ�������־
==========

[changelog]: changelog.md

[data_base]: data_base.py

[data_process]: data_process.py

[default]: default.py

[encr_decr]: encr_decr.py

[example]: example.py

[game_disposition]: game_disposition.py

[gui_extend]: gui_extend.py

[hash_values]: hash_values.py

[LICENSE]: LICENSE

[maths]: maths.py

[randoms]: randoms.py

[README]: README.md

[system_extend]: system_extend.py

[times]: times.py

[version]: version.json

[__init__]: __init__.py

* 4.x
    * 4.4 ����: [�汾�Զ���������][default]
        * Release 4.4 [2023-01-19-14-25-50] (version_code: 20230225001)
            * Rewrite of `search_to_str_in_list`, add two params named `recursion=False` and `insensitive_data=False`.
            * �� [example.py][example] �еĲ��ֳ���
            * Update `get_update()` function and rewrite the [`version.json`][version] file.
            * Update [README.md#��֪����][README] plate.
            * > Add: Release 4.4 �汾���·��治������ǰ�����а汾.
        * 4.4-beta3 [2023-01-19-14-25-50] (version_code: 20230219001)
            * Update [README.md][README].
        * 4.4-beta2 [2023-02-18-17-55-10] (version_code: 20230218001)
            * Delete ~~[passed.py](passed.py)~~(not found).
            * Delete `breakpoint()` in passed.py.
            * Update `times.wait()`.
            * Move `passed.pass_()` to [default.py][default].
        * 4.4-beta1 [2023-02-12-16-40-12] (version_code: 20230212001)
            * Update `generate_file_path`, add a **Distributed operations** option
              and supplemented its documents.
            * Fix `get_time_stamp` a serious bug that make user use preset values compulsorily.
            * Download `version.json` to local.
        * 4.4-pre2 [2023-02-03-21-35-38] (version_code: 20230203003)
            * Add some error code in `get_update()`
            * Update `get_update()` as headers and mirror source code.
        * 4.4-pre1 [2023-02-03-20-10-46] (version_code: 20230203002)
            * Owned version code (yyyymmdd\<num\>)  
              example: 20230203001
            * Auto upgrade itself
            * Publish [first release](https://github.com/8388688/simple_tools/releases/tag/4.4-pre1)
              on [GitHub](https://github.com/)
    * 4.3 ����: [�򻯸���][__init__]
        * 4.3 [2023-02-03 18:08:59] (version_code: 20230203001)
            * Remove `bl()`, `receive()`, `cacheTimes`, `money` (2 function, 2 variable).
            * Migrate `review()` as `review_2()`
            * Remove a few scripts that for test.
        * 4.3-alpha1 [2023-01-31 20:21:59]
            * Remove `bomb1()`, `bomb2()`, `create_toplevel()`,
              `draw1()`, `draw2()` (5 function).
            * Remove the tips of creating files.
            * Fix a bug: Repeat tip `<filepath> �ļ������ڻ�����\n�������ƴ��ļ�`.
              when the file `namelist.txt` was empty.
    * 4.2 ����: [maths ��ѧ��������][maths]
        * 4.2-beta3 [2023-01-26 11:11:20]
            * Update `get_hash_values`, `get_md5`, add ratio-choice.
            * Delete 5 variables in [encr_decr][encr_decr].
        * 4.2-beta2 [2023-01-24 17:53:05]
            * Add `quiet` param to `normal_encryption_with_bytes`.
            * Migrate `normal_encryption` as `normal_encryption_with_byte`(constitutional with `class bytes`).
            * Fix `generate_prime_range` a tiny bug.
        * 4.2-beta1 [2023-01-12 17:11:01]
            * �ð�����˹����ɸ����д `get_prime_range()` ������
            * ���� `is_prime()` ������ n=4 ʱ���� True �� bug.
            * ���� `generate_prime_range()` ������һ�� bug.
    * 4.1 ����: [data_process ����][data_process]
        * 4.1-pre4 [2022-12-17 19:49:40]
            * �ϲ� get_prime_range �� generate_prime_range, ���Ա��� get_prime_range ��Ϊһ������������
        * 4.1-pre3 [2022-12-10 19:49:30]
            * �����е�Ŀ¼�ں�̨��Ĭ����, �����ɹ���������¼����Ӧ���ļ���־�С�
            * ���� dec_to_r_convert() ����, ���� ǿ�ƽ��������ַ�ת���������ַ� �� bug.
        * 4.1-pre2 [2022-11-20 19:31:26]
            * ���¹���Ŀ¼Ϊ %APPDATA%\8388688\py_workspace\simple_tools (����ͼ)��
            ```
          from os import getenv, system, chdir as cd
          from os.path import join
          work_space = join(getenv('APPDATA'), '8388688', 'py_workspace', 'simple_tools')
          system('md ' + work_space)
          cd(work_space)
          ```
            * �� encr_decr �еĺ���������, ���� 'absoluteEncryption' -> 'absolute_encryption'. ͬʱ, Ϊ�˷�ֹ�ϰ汾����
              simple_tools ����������, ʹ�ñ��������
            * ���� [changelog.md] ���ļ����Ӹ�ʽ��
          >     [README.md](README.md)
          >     ->
          >     [README]: README.md
          >     [README.md][README]
        * 4.1-pre1 [2022-10-5 17:07:41]
            * ���� filter_ �е�һ�� bug.
            * filter_ �Զ��� walls.
            * ΢�� [maths.py][maths] �� saving_decomposition ������
    * 4.0 ����: \[[README.md][README] ����\] [20221003]
        * 4.0 [2022-10-5 15:26:54]
            * �����ļ���
        * 4.0-pre3[2022-10-5 10:15:55]
            * ���� [README.md][README] (�ɰ汾�������ļ��� ~~[README_old.md](README_old.md)~~ [��ɾ��])
            * �������е� `if __name__ == '__main__':` ���Խű��� [example.py][example] ��
        * 4.0-pre2[2022-10-4 09:13:20]
            * merge files such as view.py, draw.py, bomb.py etc.
            * update [README.md][README]
            * update work space of simple_tools [%appdata%/simple_tools]
        * 4.0-pre1[2022-10-3 18:20:15]
            * rename module1 to simple_tools
            * add files named [README.md][README] and [LICENSE][LICENSE]
            * upload these package to [GitHub](https://gitbub.com/)
            * �� [\_\_init\_\_][__init__] �еĸ�����־ת���� [README.md][README]
            * simple_tools ���� Beta �汾
* 3.x
    * 3.4x
        * 3.4.6 ����: [20220925]
            * rename ~~[review.py](review.py)~~[not found] to ~~[view.py](view.py)~~[not found]
            * �� [system_extend.py][system_extend] ������һ����ϸ΢�� bug (��ӡ���õĿ��е� bug)
        * 3.4.5 ����: [20220925]
            * �Ż� __all__ ����, ���������ļ�
        * 3.4.4 ����: [20220918]
            * ���� [system_extend.py][system_extend] ��һЩ����
        * 3.4.3 ����: [20220918]
            * �� [system_extend.py][system_extend] �н� `from os import *` ����Ϊ `import os`
        * 3.4.2 ����: [20220918]
            * �Ż� [data_handle.py][data_process] �� [maths.py][maths] ��������
        * 3.4.1 ����: [20220918]
            * �Ż�����ṹ[��]
        * 3.4 ����: [maths ��ѧ��������][maths] [20220918]
            * ���� getPrime ����
            * rename getPrime to getPrimeRange,
            * �� [2] �ָĳ� get_prime_range
            * ��� get_prime_range_of_generator ����
    * 3.3x
        * 3.3.8 ����: [from 20220901 to 20220912]
            * �Ż�����ṹ[��]
        * 3.3.7 ����: [20220825]
            * �� [default.py][default] �м��� clear_module1_cache ����
        * 3.3.6 ����: [20220825]
            * �Ż�����ṹ[��]
        * 3.3.5 ����: [20220824]
            * rename maths.d() to maths.is_prime()
        * 3.3.4 ����: [20220824]
            * rename [encryption.py][encr_decr] to [encr_decr.py][encr_decr]
        * 3.3.3 ����: [20220817]
            * rename get_false_unix_time to get_time_stamp
        * 3.3.2 ����: [20220817]
            * (���˸���)�� get_false_unix_time ���� 5 ��Ԥ��ֵ
        * 3.3.1 ����: [20220817]
            * �޸� [times.py][times] �� get_false_unix_time Ԥ��ֵ�±�Խ��� bug
        * 3.3 ����: [ʱ�亯������] [20220816]
            * ������� get_false_unix_time
                * ׼���� 1,133,180,928 �ֲ�ͬ��ʱ�����ʽ, �����Լ���һ�޶���ʱ���
                * (���˸���)�Զ�����Ĭ��ʱ���ʽ
                * �޸�����һ�ѹ���� bug
    * 3.2x
        * 3.2.2 ����: [20220816]
            * ���� get_false_unix_time properties ����װ�θ�ʽ
        * 3.2.1 ����: [20220815]
            * �޸� [system_extend.py][system_extend] �� get_file_name ����д����־ʱ�������Ļ���ʾ��������
        * 3.2 ����: [�ļ�ϵͳ - ����Ŀ¼����] [20220815]
            * ��ÿ���ļ�����������Ӧ�Ĺ���Ŀ¼
            * �洢�� [AppData/Roaming/module1](%appdata%/Roaming/module1) ��
            * ����ģ��ѭ������� ImportError
    * 3.1x
        * 3.1 ����: [system_ ����][system_extend] [20220815]
        * rename [system_.py][system_extend] Ϊ [system_extend.py][system_extend]
        * �� [system_extend.py][system_extend] ����� safe_md ����
    * 3.0x
        * 3.0.2 ����: [20220815]
            * ���� [maths.py][maths] �� decomposition ����
        * 3.0.1 ����: [20220814]
            * �޸� ~~[bomb.py](bomb.py)~~[not found] ��һ�� bug
        * 3.0 ����: [�ļ�ϵͳ����] [20220814]
            * ӵ�����Լ��Ĺ���Ŀ¼: [%APPDATA%/module1](%APPDATA%/module1)
            * �Զ����ɹ���Ŀ¼
            * ��� MODULE1_WORK_SPACE ����, ������������Ŀ¼
* 2.x
    * 2.9x
        * 2.9.1 ����: [20220814]
            * �޸� [game_disposition.py][game_disposition] �� Users ������� bug
        * 2.9 ����: [game_disposition ����][game_disposition] [20220813]
            * ���ģ���� [game_disposition.py][game_disposition] �е� Users ��
                * �û�
                    * �û�����
                        * �˳�ʱ���û���Ϣ�洢���ļ���
                        * ���ڵ�½ʱ��Ҫ����
                        * ���� logout �˳�����
                        * �����û����˳�ʱ�Զ���������
                * �û���ȫ
                    * topUp ��Ӧ�ú�����ܾ� temporary ��ʱ�û��ķ���
                    * __del__ ����������ܾ� self.live Ϊ False �û��ķ���
                * ��ȫ: [ʹ�ø���ȫ�� uid]
                    * ���ɷ�ʽ: ʹ�� md5 ����(ͨ���� uuid4)
                    * �ڳ������� `self.info_dict['uid']` ����ʽ�洢
                    * �����û��� name ��ΪΨһ�� ID
                    * �����洢, �� name ����ȫ
                * ����
                    * ����һЩ����
                    * �Ż�ԭ���ĳ���ṹ
                    * �޸�һ�� bug
                    * ���������ļ��Ĺ���
                    * �Զ�����𻵵��ļ�
                * ̫����, ˵��������. . .
    * 2.8x
        * 2.8.4 ����: [20220813]
            * �޸� get_file_path_of_generator ���ִ�Сд����� bug
        * 2.8.3 ����: [20220812]
            * �� get_file_path_of_generator ��� case_sensitive ��������
        * 2.8.2 ����: [20220812]
            * ���� [data_handle][data_process] �� __all__ ����
        * 2.8.1 ����: [20220812]
            * ɾ�� ~~[review.py](review.py)~~[not found] �µ� bl_generator ����
        * 2.8 ����: [����ṹ����] [20220812]
            * �½� [game_disposition.py][game_disposition] �ļ�
            * �� User �� �� Person �� �Ƶ� [game_disposition.py][game_disposition] ��
            * ɾ�� [\_\_init\_\_.py][__init__] ��һЩ���õ�����
            * ���� [\_\_init\_\_.py][__init__] ��ע��
    * 2.7x
        * 2.7.3 ����: [20220810]
            * ɾ�� [system_.py][system_extend] �е� get_file_name_of_generator ������
        * 2.7.2 ����: [20220810]
            * �� [hash_values.py][hash_values] �м��� uuid_generator ����
        * 2.7.1 ����: [20220810]
            * �� [system_.py][system_extend] ��, �� get_file_name_of_generator �� get_file_path_of_generator �ϲ�
        * 2.7 ����: [system_ ����][system_extend] [20220809]
            * ���� get_file_name
                * �������ɴ�����־�Ĺ���
                * ���� OSError ��������
            * file_pattern �����ļ�·���޷�ʶ��Ĵ�������
            * ���� get_file_path_of_generator ����, �������м��� bug
            * Ϊ get_file_path_of_generator ��� include �� exclude ��������
            * ���ģ���� File ��, ��� permission, user_id �� 10 ��������
    * 2.6x
        * 2.6.1 ����: [20220801]
            * normalEncryption �� coding ���� ���ڿ�ѡ��Ϊ `[getfilesystemencoding(), 'utf-8', 'gbk']`
        * 2.6 ����: [���ܸ���][hash_values] [20220801]
            * ���� md5_encryption
            * ���� normalEncryption �� bug
            * ���� normalEncryption, ���� coding ���� `['auto', 'f_byte', 'f_int']` ������ѡ��
    * 2.5x
        * 2.5.1 ����: [20220727]
            * ���� md5_encryption
            * ���� normal_encryption ����, �޸�һЩ bug
            * ���� [������־][changelog] ������
        * 2.5 ����: [system_ ����][system_extend] [20220404]
        * �� [system_.py][system_extend] �´��� File ��
        * ��� system_pro ����������ǰ����ϵͳ
    * 2.4x
        * 2.4.4 ����: [20220320]
            * ���� [example.py][example] �ļ�
            * [ʱ���ж�]
        * 2.4.3 ����: [20220312]
            * ���� get_file_path_of_generator �޷����������ļ��е� bug
            * ���� file_remove, get_file_name, file_pattern
        * 2.4.2 ����: [20220305]
            * ��� random_choice ����
        * 2.4.1 ����: [20220305]
            * ɾ�� create_random ����
            * ���� file_pattern ����, ��� easy_options ����
        * 2.4 ����: [times ����][times] [20220305]
            * ���� [times.py][times] �ļ�
            * �� [times.py][times] �д��� get_false_unix_time ����
            * �ƶ� wait ������ [times.py][times] ��
            * ���� [\_\_init\_\_.py][__init__] �� \_\_all\_\_ ����
    * 2.3x
        * 2.3.1 ����: [20220226]
            * ���� [hash_values.py][hash_values] �ļ�
            * �� get_md5 �����Ƶ� [hash_values.py][hash_values] ��
        * 2.3 ����: [data_handle ����][data_process] [20220226]
            * ���²����� filter_ �� other_signs ����
            * �� [data_base.py][data_base] �м��� tabs Ԫ��
            * ���� __all__ ����
    * 2.2x
        * 2.2.3 ����: [20220219]
            * ���� filter_ �� other_signs ����
            * ɾ�� test() �е� draw1 ����
        * 2.2.2 ����: [20220219]
            * ���� binarySearch ����
        * 2.2.1 ����: [20220205]
            * rename username to usernameList
        * 2.2 ����: [20220205]
            * rename str_handle to data_handle
            * ɾ�� default �е� createToplevel
            * ���� ~~[test.py](test.py)~~[not found]
    * 2.1x
        * 2.1 ����: [20220203]
            * ���� file_remove �����޷�ɾ���ļ��е� bug
            * ���� file_pattern ����.
            * �� [system_.py][system_extend] ����� fp = getcwd() ����
            * ���� dimensionalList �� [data_handle.py][data_process]
    * 2.0x
        * 2.0.1 ����: [20220203]
            * ����ģ�鳣���޷����������
        * 2.0 ����: [20220203����, ��ͬ]
            * ���� file_remove, ���ģ���� system_.py
            * ���� get_file_path_of_generator �� bug
            * ���볣�� EOF = -1, NULL = None, null = 0
            * ɾ�� [\_\_init\_\_.py][__init__] �� absoluteEncryption
            * ���� [data_base.py][data_base] ���ݿ�.
* 1.x
    * 1.8x
        * 1.8 ����:
            * ���� [system_.py][system_extend]
            * �ƶ� get_file_name, get_file_name_of_generator,get_file_path, get_file_path_of_generator,
              get_file_size,get_files, get_file_names �� [system_.py][system_extend]
    * 1.7x
        * 1.7.1 ����:
            * ���� Users,
            * pw �� md5 ����.
        * 1.7 ����:
            * ɾ�� [\_\_init\_\_.py][__init__] �� review, digitalDecryption, draw1, draw2, breakpoint_
            * ���� breakpoint_ �� exit_ �� bug
            * ���� [randoms.py][randoms] ����� createRandomList
            * ɾ�� [\_\_init\_\_.py][__init__] �� passed, EuclideanAlgorithm.
    * 1.6x
        * 1.6.13 ����:
            * ���� get_file_path �� bug.
        * 1.6.12 ����:
            * �� get_file_name ���ע��.
        * 1.6.11 ����:
            * 1.���� username �ʿ�
            * 2.�޸���������� bug.
        * 1.6.10 ����:
            * 1.���� filter_ R ���ƹ��˵� bug
            * 2.�� get_files ����Ϊ get_file_path.
        * 1.6.9 ����:
            * 1.���� EuclideanAlgorithm
            * 2.ɾ�� [\_\_init\_\_.py][__init__] �� bl.
        * 1.6.8 ����:
            * 1.�� divisionAlgorithm ��������Ϊ EuclideanAlgorithm,
            * 2.ɾ�� [\_\_init\_\_.py][__init__] �� conversionSystem.
        * 1.6.7 ����:
            * �ӽ� get_file_name �� get_files ���������� default.py ��.
