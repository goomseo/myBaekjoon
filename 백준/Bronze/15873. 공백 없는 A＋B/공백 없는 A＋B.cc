#include <iostream>

using namespace std;

int main() {
    int input;
    cin >> input;
    cout << ((input % 10 == 0) ? input / 100 + input % 100 : input / 10 + input % 10);
}