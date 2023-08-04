def sysinfo(ask):
    import platform
    
    if ask == s_platform:
        #操作系统及版本信息 eg.Linux-5.15.0-1042-azure-x86_64-with-glibc2.31
        s_platform = platform.platform()
        return s_platform
    elif ask == 's_platver':
        #获取系统版本号 eg.#49-Ubuntu SMP Tue Jul 11 17:28:46 UTC 2023
        s_platver = platform.version()
        return s_platver
    elif ask == 's_system':
        #获取系统名称 eg.Linux
        s_system = platform.system()
        return s_system
    elif ask == 't_architecture':
        #系统位数 eg.('64bit', 'ELF')
        #type=tuple
        t_architecture = platform.architecture()
        return t_architecture
    elif ask == 's_machine':
        #计算机类型 eg.x86_64
        s_machine = platform.machine()
        return s_machine
    elif ask == 's_hostname':
        #计算机名称 eg.codespaces-e8945d
        s_hostname = platform.node()
        return s_hostname
    elif ask == 's_processor':
        #处理器类型 eg.x86_64
        s_processor = platform.processor()
        return s_processor
    elif ask == 'x_uname':
        #计算机相关信息 eg.uname_result(system='Linux', node='codespaces-e8945d', release='5.15.0-1042-azure', version='#49-Ubuntu SMP Tue Jul 11 17:28:46 UTC 2023', machine='x86_64')
        #type=<class 'platform.uname_result'>
        x_uname = platform.uname()
        return x_uname
    
#调用sysinfo函数，获取系统名称
print(sysinfo(ask='s_hostname'))
