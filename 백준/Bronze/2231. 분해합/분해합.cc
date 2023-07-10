#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;

    int digitGenerator, tmp, count = 0;
    for (int i = 1; i < n + 1; ++i) {
        count += 1;

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
            break;
        }
    }

    if (count == n)
        cout << 0;
}
