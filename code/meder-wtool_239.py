# -*- coding: utf-8 -*-
import sys  # 220716 GONGYE Heyu
import os
from time import time, localtime, sleep
import random
import string
import socket
from os import system


def t0():
    # 获取现在时间戳
    import time
    t0 = time.time()
    return t0


ti0 = t0()

ver = '23.9'
mainame = 'medor-tools'


def sysinfo(ask):
    import platform

    if ask == 's_platform':
        # 操作系统及版本信息 eg.Linux-5.15.0-1042-azure-x86_64-with-glibc2.31
        s_platform = platform.platform()
        return s_platform
    elif ask == 's_platver':
        # 获取系统版本号 eg.#49-Ubuntu SMP Tue Jul 11 17:28:46 UTC 2023
        s_platver = platform.version()
        return s_platver
    elif ask == 's_system':
        # 获取系统名称 eg.Linux
        s_system = platform.system()
        return s_system
    elif ask == 't_architecture':
        # 系统位数 eg.('64bit', 'ELF')
        # type=tuple
        t_architecture = platform.architecture()
        return t_architecture
    elif ask == 's_machine':
        # 计算机类型 eg.x86_64
        s_machine = platform.machine()
        return s_machine
    elif ask == 's_hostname':
        # 计算机名称 eg.codespaces-e8945d
        s_hostname = platform.node()
        return s_hostname
    elif ask == 's_processor':
        # 处理器类型 eg.x86_64
        s_processor = platform.processor()
        return s_processor
    elif ask == 'x_uname':
        # 计算机相关信息 eg.uname_result(system='Linux', node='codespaces-e8945d', release='5.15.0-1042-azure', version='#49-Ubuntu SMP Tue Jul 11 17:28:46 UTC 2023', machine='x86_64')
        # type=<class 'platform.uname_result'>
        x_uname = platform.uname()
        return x_uname
    elif ask == 's_py_ver':
        # 获取python版本
        s_py_ver = platform.python_version()
        return s_py_ver


def start():
    cls()
    print(mainame + " " + ver + 
    '''
    0.退出
    1.应用程序
    2.时钟''')
    startcho = int(input("请输入数字来执行你的操作"))
    if startcho == 0:
        cls()  # 220701 GONGYE Heyu
        print("感谢使用,再见")
    elif startcho == 1:
        cls()  # 220701 GONGYE Heyu
        apps()
    elif startcho == 2:
        cls()  # 220701 GONGYE Heyu
        clock()
    else:
        input("输入错误")
        cls()
        start()


def apps():
    cls()
    print('''
    1.系统信息
    2.网络信息
    3.清理垃圾
    4.文件编辑
    5.Windows修复
    6.随机字符生成 
    7.时钟           
    0.开始
    00.关于
    ''')
    # “时钟” 220701 GONGYE Heyu
    appscho = int(input("请输入"))
    if appscho == 1:
        系统信息()
    elif appscho == 2:
        # 本地连接()
        网络信息()  # 220701 GONGYE Heyu
    elif appscho == 3:
        清理垃圾()
    elif appscho == 4:
        # 写入文件()
        文件编辑()  # 220701 GONGYE Heyu
    elif appscho == 5:
        Windows修复()
    elif appscho == 6:
        随机字符生成()
    elif appscho == 7:
        clock()  # 220701 GONGYE Heyu    
    elif appscho == 0:
        start()
    elif appscho == 00:
        关于()
    
    else:
        input("输入错误")
        cls()
        apps()


def 系统信息():
    cls()
    print(sysinfo("s_platform"))
    print(sysinfo("s_platver"))
    print(sysinfo("s_system"))
    print(sysinfo("t_architecture"))
    print(sysinfo("s_machine"))
    print(sysinfo("s_hostname"))
    print(sysinfo("s_machine"))
    print(sysinfo("s_processor"))
    print(sysinfo("x_uname"))
    print("Python版本 " + sysinfo("s_py_ver"))
    back(1)  # 220716 GONGYE Heyu


def 网络信息():
    cls()
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    print("主机名" + hostname)
    print("IP地址" + ip)
    if sysinfo("s_system") == "Windows":
        print(os.system('netstat -sera'))
        print(os.system('ipconfig /all'))
    back(1)  # 220716 GONGYE Heyu
# 220701 GONGYE Heyu


def 清理垃圾():
    print("开发中...")
    back(1)


def 文件编辑():
    cls()
    w = input("请输入路径")
    i = input('''
    n.新建文件
    o.读取文件
    l.列出文件
    d.删除文件
    b.返回''')
    if i == 'n':
        f = open(w, 'w')
        f.close()
        print("文件创建完成")
        文件编辑()
    elif i == 'o':
        f = open(w, 'r')
        print(f.read())
        f.close()
        文件编辑()
    elif i == 'l':
        print(os.system('dir ' + w))
        文件编辑()
    elif i == 'd':
        os.remove(w)
        print("文件删除完成")
        文件编辑()
    elif i == 'b':
        back(1)  # 220716 GONGYE Heyu
    else:
        print("输入错误")
        文件编辑()
    # 220701 GONGYE Heyu


def Windows修复():
    cls()
    s_system = sysinfo("s_system")
    if s_system == "Linux":
        print("不可用")
    elif s_system == "Windows":
        os.system("sfc /scannow")
    back(1)


def 随机字符生成():
    cls()
    # 生成字典a-z
    a = string.ascii_lowercase
    # 生成字典0-9
    b = string.digits
    # 生成字典A-Z
    c = string.ascii_uppercase
    # 生成字典符号
    d = string.punctuation
    # 生成字典所有
    f = a+b+c+d
    # 输入需要生成的字符长度
    n = int(input('请输入需要生成的字符长度：'))
    # 生成
    p = ''
    for i in range(n):
        p += f[random.randint(0, len(f)-1)]
    # 输出字符
    print('生成的字符为：', p)
    # 输出字符长度
    print('生成的字符长度为：', len(p))
    back(1)  # 220716 GONGYE Heyu


def clock():
    cls()

    class Clock(object):
        """数字时钟"""

        def __init__(self, hour=0, minute=0, second=0):
            """
            构造器
            :param hour: 时
            :param minute: 分
            :param second: 秒
            """
            self._hour = hour
            self._minute = minute
            self._second = second

        @classmethod
        def now(cls):
            ctime = localtime(time())
            return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

        def run(self):
            """走字"""
            self._second += 1
            if self._second == 60:
                self._second = 0
                self._minute += 1
                if self._minute == 60:
                    self._minute = 0
                    self._hour += 1
                    if self._hour == 24:
                        self._hour = 0
        """时钟打印"""

        def __str__(self):
            cls()
            return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

    def main():
        clock = Clock.now()
        while True:
            print(clock)
            sleep(1)
            clock.run()
    if __name__ == '__main__':
        main()

def debuginfo():
    print("版本:" + str(ver))
    print("加载耗时:" + str(ti-ti0))
    import time
    print("时间:" + str(time.time()))
    print("系统信息:" + str(sysinfo("x_uname")))
    print("python信息:" + str(sysinfo("s_py_ver")))


def 关于():
    cls()
    print('''
    medor-ltools
    Copyright 2020-2022 GONGYE Heyu
    版本23
    gongyeheyu@outlook.com
    
    a.查看许可证
    b.更新日志
    c.加载耗时
    d.调试信息
    z.返回''')
    i = input()
    if i == 'a':
        cls()
        print(license)
        back(3)  # 220716 GONGYE Heyu
    elif i == 'b':
        cls()
        print(uplog)
        back(3)  # 220716 GONGYE Heyu
    elif i == 'c':
        global ti0
        global ti
        cls()
        print(ti-ti0)
        back(3)
    elif i == 'd':
        cls()
        debuginfo()
        back(3)
    else:
        back(0)  # 220716 GONGYE Heyu


def cls():
    system('clear')


def back(where):
    w = sys._getframe(1).f_code.co_name
    # where=0为直接返回主菜单，where=1为询问后返回主菜单#
    # where=2为直接返回上一级菜单,where=3为询问后返回上一级菜单
    if where == 0:
        cls()
        apps()
    elif where == 1:
        input("按任意键返回")
        cls()
        apps()
    elif where == 2:
        cls()
        # 调用w中的函数名
        globals()[w]()
    elif where == 3:
        input("按任意键返回")
        cls()
        globals()[w]()
    else:
        print("输入错误")
        back(3)
# 220716 GONGYE Heyu


uplog = '''
更新日志：
2023.7.12
1.弃用软件查询
2.将原“IP地址”合并到“网络信息”，改“IP地址”为“系统信息”
3.这个版本专门移植到Linux
4.“Windows修复”不可用
5.撤销许可证

2022.07.17
1.在你们看不见的地方优化了代码，但应该是个负优化，因为优化后比没有优化更慢

2022.07.16
1.修改了back函数，使其可以直接返回上一级菜单
2.改“本地连接”为“网络信息”
3.新增加载时间
4.新增无数BUG  qwq

2022.07.01
1.新增网络信息，文件编辑，时钟，开源许可证
2.新增无数BUG  qwq'''

license = "已撤销"


def t():
    import time
    t = time.time()
    return t


ti = t()

start()
