import subprocess

def main():
    s_mainame = "medor-shell"
    s_ver = "23.a28w"
    print(s_mainame+" "+s_ver)
    while True:
        # 获取用户输入
        s_in = input("]>")

        # 解析输入
        d_in = {}
        ls_in = s_in.split()
        i_in_len = len(ls_in)
        for i in range(i_in_len):
            d_in[i] = ls_in[i]
            print(d_in)
        ls_cmd = ls_in[0]
        ls_arg1 = ls_in[1:]

        # 执行命令
        if d_in[0] == "exit":
            break
        else:
            try:
                # 调用系统命令
                output = subprocess.check_output([d_in[0]] + ls_arg1 ,shell=True)
                print(output.decode())
            except Exception as e:
                print("Error:", e)

main()