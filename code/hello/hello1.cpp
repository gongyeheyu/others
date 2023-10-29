#include <iostream>
using namespace std;
int guess(int a);
int main(){
	cout << "guess the number" << endl;
	int b;
	cin >> b;
	int c;
	c = guess(b);
	if (!c) {
	cout << "you are right";
	}
	if (c) {
	cout << "you are wrong";
	}
	return 0;
}

int guess(int a){
	if (a == 10) {
        return 0;
        }
        if (a != 10) {
        return 1;
        }
}
