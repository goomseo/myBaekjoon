#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a = 0, b = 1, tmp;
    for (int i = 0; i < n; ++i) {
        tmp = a;
        a = b;
        b += tmp;
    }

    cout << a;
}
