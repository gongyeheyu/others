#include<iostream>
#include <unistd.h>
#include <filesystem>
#include <string.h>

using namespace std;
string s_mainame = "medor_env";
string i_ver = "24w";
string s_workdir;
string s_homedir;

string port(string arg1,string arg2){
    if (arg1 == "workdir"){
        const string s_homedir = arg2;}
    return "0";
}

string in_fenxi(string c_workdir){
    //分析输入命令
    char s[1024] = c_workdir;
    char * p;
    // Here, the delimiter is white space.
    p = strtok(s, " "); 
    while (p != NULL) {
        cout << p << endl;
        p = strtok(NULL, " ");
    }
}

int main(){
    cout << s_mainame + " " + i_ver << endl;
    char c_workdir[1024];
    getcwd(c_workdir, 1024);
    string s_workdir(c_workdir);
    port("workdir",s_workdir);
    while (true){
        string s_in;
        getline(cin, s_in);
        cout << s_in << endl;
        }
    return 0;
}