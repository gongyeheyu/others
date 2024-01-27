#include <iostream>
#include <string>
#include <cstring>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    using namespace std;
    string command;
    while (true) {
        cout << "shell> ";
        getline(cin, command);
        
        // 将std::string转换为C风格的字符串
        char *args[256];
        char *token = strtok(const_cast<char*>(command.c_str()), " ");
        int i = 0;
        while (token != nullptr) {
            args[i] = token;
            ++i;
            token = strtok(nullptr, " ");
        }
        args[i] = nullptr;
        
        // 创建子进程执行命令
        pid_t pid = fork();
        if (pid == 0) {
            // 子进程
            execvp(args[0], args);
            cerr << "无法执行命令" << endl;
            return 1;
        } else if (pid > 0) {
            // 父进程
            waitpid(pid, nullptr, 0);
        } else {
            // fork失败
            cerr << "无法创建子进程" << endl;
            return 1;
        }
    }
    
    return 0;
}