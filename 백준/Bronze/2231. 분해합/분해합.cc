#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int digitGenerator, tmp;
    for (int i = 1; i < n + 1; ++i) {
        tmp = i;
        digitGenerator = tmp;
        while (true) {
            if (tmp == 0)
                break;

            digitGenerator += tmp % 10;
            tmp /= 10;
        }

        if (digitGenerator == n) {
            cout << i;
            return 0;
        }
    }

    cout << 0;
}
