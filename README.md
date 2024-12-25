# simple_tools - 一个用 python 写的简易工具包

-----
<a id="_menu">索引:</id>

1. [索引](#_menu)
2. [概述](#_summary)
3. [依赖的插件](#_depend_on)
4. [bug追踪](#_bug_report)
5. [下一个版本的预告](#_next_version)
6. [更新日志](#_changelog)
7. [文件历史记录](#_file_history)
8. [其他](#_others)
9. [你知道吗](#_do_you_know)

-----
<a id="_summary">概述</id>

[回到顶部](#_menu)

## 概述

作者: 8388688

最后修改时间：2024-06-27
~~(以此证明我还活着)~~

-----
<a id="_depend_on">依赖的插件</id>

[回到顶部](#_menu)

## 依赖的插件

* python.io
* python.math
* python.os
* python.random
* python.stat
* python.sys
* python.uuid
*
* python.requests
* . . . . . .

-----
<a id="_bug_report">bug追踪</id>

[回到顶部](#_menu)

## bug 追踪

- [ ] = 未解决
- [x] = 已解决

-----

- [ ] st-000001. 简化 filter_()
- [ ] st-000002. fp_gen() 遍历文件夹时 include 参数不起作用
- [ ] st-000003. ...

-----
<a id="_next_version">下一个版本</id>

[回到顶部](#_menu)

## 下一个版本的预告

Release-4.6

- 更新 [system_extend.py](system_extend.py) 的一些功能

-----
<a id="_changelog">更新日志</id>

[-> 传送门 <-](changelog.md)

[回到顶部](#_menu)

-----
<a id="_file_history">文件历史记录</id>

[回到顶部](#_menu)

### 保存的历史版本(按照时间顺序排序)

-----
<a id="_others">其他</id>

[回到顶部](#_menu)

- 函数命名规则
    - 尾部带有 "_gen" / "_generator" 后缀的 **[函数](https://zh.wikipedia.org/wiki/子程序)** 为生成器（such
      as `get_fp_gen()`）。
    - 尾部带有 "_fp"(**f**ile **p**ath) 的变量为存储文件路径的 **变量**（such as `top10file_fp`）。
    - 尾部带有 "_fiet"(**fi**le **e**n**t**ity) 的变量为存储文件实例的 **变量**（such as `top10file_fiet`）。

-----
<a id="_do_you_know">你知道吗</id>

[回到顶部](#_menu)

### 你知道吗

1. 在 1.6x 版本之前，simple_tools 的文件名叫作 `[中文名\素材大本营`，在 2.0 版本之后改为 module1
2. 在 [GitHub](https://github.com/) 上，也有一个同名的
   [simple_tools](https://www.github.com/afriemann/simple_tools.git)，但和这个 simple_tools 之间没有任何关系。
3. 1.6.6 以前的版本全部损坏，无法读取。
4. 2.0.1 以前的版本创建、修改和访问时间间隔太长，损坏严重，无法读取。
5. 在 3.x 之前的版本，自述文件的行数被规定不能超过 270 行，此条目已在 2022-10-01 被废除。
6. 在作者创建 simple_tools 项目时，当时不知道 Public 和 Public Template 的区别，
   结果把 simple_tools 整成了一个 Public Templeate 公共模板，这个错误直到 2023-02-19 才改正。
   但我仍然保留了 [Public Template simple_tools](https://github.com/8388688/simple_tools) 的最后一个版本。
