import subprocess

def mtime():
    import datetime
    current_time = datetime.datetime.now()
    print("当前时间为:", current_time)
    return 0

def main():
    s_mainame = "medor-shell"
    s_ver = "23.a28w"
    print(s_mainame+" "+s_ver)
    l_in_cmd = ["exit", "mtime"]
    import os
    l_out_cmd = os.listdir("/usr/bin")
    while True:
        # 获取用户输入
        s_in = input("]>")

        # 解析输入
        d_in = {}
        ls_in = s_in.split()
        i_in_len = len(ls_in)
        for i in range(i_in_len):
            d_in[i] = ls_in[i]
        ls_cmd = ls_in[0]
        ls_arg1 = ls_in[1:]

        # 执行命令
        if d_in[0] in l_in_cmd or d_in[0] in l_out_cmd:
            if d_in[0] == "exit":
                break
            elif d_in[0] == "mtime":
                mtime()
                
            else:
                try:
                    # 调用系统命令
                    output = subprocess.check_output(s_in ,shell=True)
                    print(output.decode())
                except Exception as e:
                    print("E:", e)
                    
        else:
            print("E:", "command not found")

main()