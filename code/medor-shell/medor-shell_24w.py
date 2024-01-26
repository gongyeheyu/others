import subprocess
import os

d_in = {}
g_d_in = {}
s_mainame = "medor-shell"
s_ver = "24w"
s_in = None
ls_in = None

s_work_dir = os.getcwd()
s_home_dir = s_work_dir #锁定s_home_dir
s_user = os.getlogin()
import datetime
current_time = datetime.datetime.now()

def mtime():
    print("当前时间为:", current_time)
    return 0

def history(s_in):
   with open(s_home_dir + "history.txt", "a") as f:
       f.write(str(current_time) + " " + s_in + "\n")
   return 0

def clear():
   import os
   os.system("clear")
   return 0

def help():
   print("这是一个简单的命令行界面，具有以下功能：")
   print("1. history - 显示命令历史")
   print("2. clear - 清空屏幕")
   print("3. help - 显示帮助信息")
   print("4. set - 设置全局变量")
   print("5. export - 设置环境变量")
   print("6. unset - 删除环境变量")
   print("7. echo - 输出字符串")
   print("8. pwd - 显示当前目录")
   print("9. cd - 切换目录")
   print("10. ls - 列出目录内容")
   print("11. cat - 显示文件内容")
   print("12. grep - 搜索文件内容")
   print("13. awk - 对文件内容进行处理")
   print("14. sed - 编辑文件内容")
   print("15. sort - 对文件内容进行排序")
   print("16. uniq - 删除文件中的重复行")
   print("17. wc - 统计文件中单词数、行数等")
   print("18. chmod - 更改文件权限")
   print("19. chown - 更改文件所有者")
   print("20. rename - 重命名文件或目录")
   print("21. mkdir - 创建目录")
   print("22. rm - 删除文件或目录")
   print("23. cp - 复制文件或目录")
   print("24. mv - 移动文件或目录")
   return 0

def cd():
   global g_d_in
   while True:
       #if g_d_in[1] == "..":
       #    os.chdir("..")
       #elif g_d_in[1] == "~":
       #    os.chdir("~")
       #elif g_d_in[1] == ".":
       #    os.chdir(".")
       #else:
       #    os.chdir(g_d_in[1])
       break
   return 0

def main():
    print(s_mainame+" "+s_ver)
    l_in_cmd = ["exit", "mtime", "history", "clear", "help", "cd",]
    d_in_cmd = {1:exit, 2:mtime, 3:history, 4:clear, 5:help, 6:cd, }
    import os
    l_out_cmd = os.listdir("/usr/bin")
    
    while True:
        # 获取用户输入
        s_work_dir = os.getcwd()
        s_in = input(s_work_dir + "]>")
        if s_in == "":
            continue
        history(s_in)

        # 解析输入
        d_in = {}
        ls_in = s_in.split()
        i_len_in = len(ls_in)
        for i in range(i_len_in):
            d_in[i] = ls_in[i]
        #global g_d_in
        #g_d_in = d_in

        k = 1
        for k in d_in_cmd:
            if d_in_cmd[k] == ls_in[0]:
                continue

        # 执行命令
        if d_in[0] in l_in_cmd:
            d_in_cmd[k]()
       
        elif ls_in[0] in l_out_cmd:
            try:
                # 调用系统命令
                output = subprocess.check_output(s_in ,shell=True)
                print(output.decode())
            except Exception as e:
                print("E:", e)
                    
        else:
            print("E:", "command not found")

main()