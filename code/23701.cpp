#include <iostream>
using namespace std;
#include <string>
#include <ctime>
#include <cstdlib>

string random_string(int length) {
    string a = "abcdefghijklmnopqrstuvwxyz";
    string b = "0123456789";
    string c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string d = "!@#$%^&*()-_=+[]{}|;:'\",<.>/?`~";
    string f = a + b + c + d;

    string p = "";
    srand(time(0));
    for (int i = 0; i < length; ++i) {
        p += f[rand() % (f.size() - 1)];
    }
    return p;
}

int main() {
    cout << "请输入需要生成的字符长度：";
    int n;
    cin >> n;
    string p = random_string(n);
    cout << "生成的字符为：" << p << endl;
    cout << "生成的字符长度为：" << p.size() << endl;
    return 0;
}
